//
//  SideBarTableViewController.swift
//  DoIT
//
//  Created by Georgescu Stefan on 25/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import UIKit

protocol SideBarViewControllerDelegate: class {
    func didSelectOption(_ option: String)
}

class SideBarViewController: UIViewController {
    
    var delegate: SideBarViewControllerDelegate?
    
    private var tableView: UITableView
    
    private var userRole: UserRole
    private var options: [String]
    private let cellID = "option-cell"
    
    init(frame: CGRect, forUserRole: UserRole) {
        self.userRole = forUserRole
        self.options = SideBarUtils.getOptionSet(forUserRole: forUserRole)
        self.tableView = UITableView(frame: CGRect(x: 0, y: 20, width: frame.width, height: frame.height))
        
        super.init(nibName: nil, bundle: nil)
        
        self.view = UIView(frame: frame)
        self.view.backgroundColor = AppColors.darkBlue
        
        tableView.isScrollEnabled = false
        tableView.dataSource = self
        tableView.delegate = self
        tableView.register(SideBarTableCellTableViewCell.self, forCellReuseIdentifier: cellID)
        tableView.backgroundColor = AppColors.darkBlue
        tableView.separatorStyle = .none
        
        self.view.addSubview(tableView)
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        tableView.reloadData()
    }
}

extension SideBarViewController: UITableViewDataSource {
    func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return options.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        guard let cell = tableView.dequeueReusableCell(withIdentifier: cellID, for: indexPath) as? SideBarTableCellTableViewCell else {
            fatalError()
        }
        cell.syncView(option: options[indexPath.row])
        return cell
    }
    
    func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 80
    }
    
    func tableView(_ tableView: UITableView, heightForHeaderInSection section: Int) -> CGFloat {
        return 130
    }
    
    func tableView(_ tableView: UITableView, viewForHeaderInSection section: Int) -> UIView? {
        let view = SideBarTopView(frame: CGRect(x: 0, y: 50, width: tableView.frame.width, height: 80), user: userRole)
        return view
    }
}

extension SideBarViewController: UITableViewDelegate {
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        delegate?.didSelectOption(options[indexPath.row])
    }
}
