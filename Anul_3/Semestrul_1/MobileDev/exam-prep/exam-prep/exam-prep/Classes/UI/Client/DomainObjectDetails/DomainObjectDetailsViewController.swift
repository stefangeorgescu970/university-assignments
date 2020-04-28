//
//  DomainObjectDetailsViewController.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import UIKit

protocol DomainObjectDetailsViewControlelrDelegate: class {
    func didPerformPositiveActionOn(_ domainObject: DomainObject)
    func didPerformNegativeActionOn(_ domainObject: DomainObject)
}

class DomainObjectDetailsViewController: UIViewController {
    private let domainObjectDetailsView: DomainObjectDetailsView
    private let domainObject: DomainObject
    private var isPersisted: Bool
    weak var delegate: DomainObjectDetailsViewControlelrDelegate?
    
    init(domainObject: DomainObject) {
        self.isPersisted = AppServices.persistantDomainObjectService.isDomainObjectPersisted(domainObject)
        domainObjectDetailsView = DomainObjectDetailsView(domainObject: domainObject, isPersisted: self.isPersisted)
        self.domainObject = domainObject
        
        super.init(nibName: nil, bundle: nil)
        
        domainObjectDetailsView.delegate = self
        self.title = "Parking Spot Details"
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func loadView() {
        self.view = domainObjectDetailsView
    }
}

extension DomainObjectDetailsViewController: DomainObjectDetailsViewDelegate {
    func domainObjectDetailsRequestedActionOn(_ domainObject: DomainObject) {
        if isPersisted {
            AppServices.domainObjectService.freeParkingPlace(domainObject) { (err: NSError?) in
                if let error = err {
                    let message = UIAlertController(title: "MD - Exam", message: "There was an error when booking the spot: \(error.userInfo["description"] ?? "")", preferredStyle: .alert)
                    message.addAction(UIAlertAction(title: "OK", style: .default))
                    self.present(message, animated: true)
                } else {
                    let result = AppServices.persistantDomainObjectService.deleteDomainObject(self.domainObject)
                    
                    if result {
                        self.domainObjectDetailsView.actionButton.setTitle("Reserve Parking Spot", for: .normal)
                        self.domainObjectDetailsView.actionButton.hideLoading()
                        self.isPersisted = false
                        self.delegate?.didPerformNegativeActionOn(self.domainObject)
                    }
                }
            }
        } else {
            AppServices.domainObjectService.takeParkingSpot(domainObject) { (err: NSError?) in
                if let error = err {
                    let message = UIAlertController(title: "MD - Exam", message: "There was an error when freeing the spot: \(error.userInfo["description"] ?? "")", preferredStyle: .alert)
                    message.addAction(UIAlertAction(title: "OK", style: .default))
                    self.present(message, animated: true)
                } else {
                    let result = AppServices.persistantDomainObjectService.persistDomainObject(self.domainObject)
                    
                    if result {
                        self.domainObjectDetailsView.actionButton.setTitle("Free Parking Spot", for: .normal)
                        self.domainObjectDetailsView.actionButton.hideLoading()
                        self.isPersisted = true
                        self.delegate?.didPerformPositiveActionOn(self.domainObject)
                    }
                }
            }
        }
    }
}
