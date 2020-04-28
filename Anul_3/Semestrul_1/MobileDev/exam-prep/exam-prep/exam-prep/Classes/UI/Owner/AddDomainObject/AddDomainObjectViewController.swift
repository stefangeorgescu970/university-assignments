//
//  AddDomainObjectViewController.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import UIKit

protocol AddDomainObjectViewControllerDelegate: class {
    func addDomainObjectViewControllerDidRequestAdd(_ domainObject: DomainObject)
}

class AddDomainObjectViewController: UIViewController {
    private var addObjectView: AddDomainObjectView
    
    weak var delegate: AddDomainObjectViewControllerDelegate?
    
    init() {
        addObjectView = AddDomainObjectView(frame: UIScreen.main.bounds)
        
        super.init(nibName: nil, bundle: nil)
        
        addObjectView.delegate = self
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func loadView() {
        self.view = addObjectView
    }
}

extension AddDomainObjectViewController: AddDomainObjectViewDelegate {
    func addDomainObjectViewDidRequestAdd(_ domainObject: DomainObject) {
        self.addObjectView.setButtonLoading(isLoading: true)
        
        AppServices.domainObjectService.addDomainObject(domainObject) { (domainObject: DomainObject?, error: NSError?) in
            if let domainObject = domainObject {
                self.addObjectView.setButtonLoading(isLoading: false)
                self.delegate?.addDomainObjectViewControllerDidRequestAdd(domainObject)
            } else if let error = error {
                self.addObjectView.setButtonLoading(isLoading: false)
                self.addObjectView.showError(withText: error.userInfo["description"] as? String ?? "An error occured")
            }
        }
    }
}
