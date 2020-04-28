//
//  ClientRestrictedListViewController.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import UIKit

class ClientRestrictedListViewController: UIViewController {
    private let cellReuseIdentifier = "students-cell"
    private var tableView: UITableView
    private var restrictedInfo = [String]()
    
    init() {
        self.tableView = UITableView(frame: UIScreen.main.bounds)
        
        super.init(nibName: nil, bundle: nil)
        
        self.tableView.delegate = self
        self.tableView.dataSource = self
        self.tableView.register(UITableViewCell.self, forCellReuseIdentifier: cellReuseIdentifier)
        
        self.tableView.backgroundView = LoadingView(frame: tableView.bounds)
    
        loadData()
        
        self.title = "Genres"
    }
    
    private func loadData() {
        if ConnectivityUtils.isConnectedToInternet {
            AppServices.domainObjectService.getPartOfDomainObjects { (restrictedInfo: [String]?, error: NSError?) in
                if let restrictedInfo = restrictedInfo {
                    self.restrictedInfo = restrictedInfo
                }
                
                self.tableView.separatorStyle = .singleLine
                self.tableView.backgroundView = nil
                self.tableView.reloadData()
            }
        } else {
            let errorView = ErrorView(frame: UIScreen.main.bounds, errorMessage: "No internet connection")
            self.tableView.backgroundView = errorView
            self.tableView.separatorStyle = .none
            errorView.delegate = self
        }
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func viewDidLoad() {
        self.view = tableView
    }
}

extension ClientRestrictedListViewController: UITableViewDelegate {
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 60
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let param = restrictedInfo[indexPath.row]
        let vc = ClientDomainObjectListViewController(withParam: param)
        vc.title = param
        
        self.navigationController?.pushViewController(vc, animated: true)
    }
}

extension ClientRestrictedListViewController: UITableViewDataSource {
    func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return restrictedInfo.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: cellReuseIdentifier, for: indexPath)
        
        cell.textLabel?.text = restrictedInfo[indexPath.row]
        
        return cell
    }
}

extension ClientRestrictedListViewController: ErrorViewDelegate {
    func errorViewDidRequestTryAgain(_ errorView: ErrorView) {
        loadData()
    }
}
