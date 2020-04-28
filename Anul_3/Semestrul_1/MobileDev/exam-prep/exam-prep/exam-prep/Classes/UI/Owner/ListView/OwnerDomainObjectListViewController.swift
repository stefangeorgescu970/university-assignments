//
//  OwnerDomainObjectListViewController.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import UIKit

class OwnerDomainObjectListViewController: UIViewController {
    
    private let cellReuseIdentifier = "owner-domain-obj-list"
    private let tableView: UITableView
    
    private var domainObjects = [DomainObject]()
    
    init() {
        self.tableView = UITableView(frame: UIScreen.main.bounds)
        
        super.init(nibName: nil, bundle: nil)
        
        self.tableView.delegate = self
        self.tableView.dataSource = self
        self.tableView.register(OwnerDomainObjectCell.self, forCellReuseIdentifier: cellReuseIdentifier)
        self.tableView.separatorStyle = .none
        
        self.tableView.backgroundView = LoadingView(frame: tableView.bounds)
        
        AppServices.domainObjectService.getAllDomainObjects { (domainObjects: [DomainObject]?, error: NSError?) in
            if let domainObjects = domainObjects {
                self.domainObjects.append(contentsOf: DomainObjectUtils.orderDomainObjects(domainObjects))
            }
            
            self.tableView.backgroundView = nil
            self.tableView.reloadData()
        }
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func loadView() {
        self.view = tableView
    }
    
    override var navigationItem: UINavigationItem {
        let navigationItem = UINavigationItem(title: "Parking Spots List")
        
        navigationItem.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .add, target: self, action: #selector(OwnerDomainObjectListViewController.didRequestAddDomainObject))
        navigationItem.rightBarButtonItem?.tintColor = AppColors.white
        
        return navigationItem
    }
    
    @objc func didRequestAddDomainObject() {
        let vc = AddDomainObjectViewController()
        vc.delegate = self
        
        self.navigationController?.pushViewController(vc, animated: true)
    }
}

extension OwnerDomainObjectListViewController: UITableViewDelegate {
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 100
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        self.tableView.deselectRow(at: indexPath, animated: false)
    }
    
    func tableView(_ tableView: UITableView, canEditRowAt indexPath: IndexPath) -> Bool {
        return true
    }
    
    func tableView(_ tableView: UITableView, commit editingStyle: UITableViewCell.EditingStyle, forRowAt indexPath: IndexPath) {
        if (editingStyle == .delete) {
            let domainObject = self.domainObjects[indexPath.row]
            AppServices.domainObjectService.deleteDomainObject(domainObject) { (error: NSError?) in
                if let error = error {
                    let message = UIAlertController(title: "MD - Exam", message: "There was an error when deleting the song: \(error.userInfo["description"] ?? "")", preferredStyle: .alert)
                    message.addAction(UIAlertAction(title: "OK", style: .default))
                    self.present(message, animated: true)
                } else {
                    self.domainObjects.remove(at: indexPath.row)
                    self.tableView.deleteRows(at: [indexPath], with: .fade)
                }
            }
        }
    }
}

extension OwnerDomainObjectListViewController: UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return domainObjects.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: cellReuseIdentifier, for: indexPath) as! OwnerDomainObjectCell
        
        cell.syncView(domainObject: domainObjects[indexPath.row])
        
        return cell
    }
}

extension OwnerDomainObjectListViewController: AddDomainObjectViewControllerDelegate {
    func addDomainObjectViewControllerDidRequestAdd(_ domainObject: DomainObject) {
        self.domainObjects.append(domainObject)
        self.domainObjects = DomainObjectUtils.orderDomainObjects(self.domainObjects)
        self.navigationController?.popViewController(animated: true)
        self.tableView.reloadData()
    }
}
