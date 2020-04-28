//
//  PersistedDomainObjectsListView.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 27/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import UIKit

class PersistedDomainObjectsListView: UIViewController {
    
    private let cellReuseIdentifier = "client-domain-persisted-obj-list"
    private let tableView: UITableView
    
    private var domainObjects = [DomainObject]()
    
    init() {
        self.tableView = UITableView(frame: UIScreen.main.bounds)
        
        super.init(nibName: nil, bundle: nil)
        
        self.tableView.delegate = self
        self.tableView.dataSource = self
        self.tableView.register(ClientDomainObjectCell.self, forCellReuseIdentifier: cellReuseIdentifier)
        self.tableView.separatorStyle = .none
        
        self.domainObjects = AppServices.persistantDomainObjectService.getAllDomainObjects() ?? [DomainObject]()
        self.tableView.reloadData()
        
        self.title = "Favourites"
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func loadView() {
        self.view = tableView
    }
}

extension PersistedDomainObjectsListView: UITableViewDelegate {
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 80
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        self.tableView.deselectRow(at: indexPath, animated: false)
        
        let vc = DomainObjectDetailsViewController(domainObject: domainObjects[indexPath.row])
        vc.delegate = self
        
        self.navigationController?.pushViewController(vc, animated: true)
    }
}

extension PersistedDomainObjectsListView: UITableViewDataSource {
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return domainObjects.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: cellReuseIdentifier, for: indexPath) as! ClientDomainObjectCell
        
        cell.syncView(domainObject: domainObjects[indexPath.row])
        
        return cell
    }
}

extension PersistedDomainObjectsListView: DomainObjectDetailsViewControlelrDelegate {
    func didPerformPositiveActionOn(_ domainObject: DomainObject) {
        self.domainObjects.append(domainObject)
        self.tableView.reloadData()
    }
    
    func didPerformNegativeActionOn(_ domainObject: DomainObject) {
        let index = self.domainObjects.firstIndex(where: { $0.id == domainObject.id })
        if let index = index {
           self.domainObjects.remove(at: index)
        }
        self.tableView.reloadData()
    }
}
