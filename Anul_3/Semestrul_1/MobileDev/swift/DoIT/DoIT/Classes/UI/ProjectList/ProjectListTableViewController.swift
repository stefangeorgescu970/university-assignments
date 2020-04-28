//
//  ProjectListTableViewController.swift
//  DoIT
//
//  Created by Georgescu Stefan on 26/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import UIKit

protocol ProjectListTableViewControllerDelegate: class {
    func didSelectProject(project: Project)
}

class ProjectListTableViewController: UITableViewController {

    var delegate: ProjectListTableViewControllerDelegate?
    var projects: [Project] = []
    
    func syncData() {
        GlobalData.sharedInstance.getProjectService().getAllProjects { [unowned self] (projects: [Project]?, error: NSError?) in
            if let projects = projects {
                self.projects = projects
                self.tableView.reloadData()
            } else {
                // handle some error
            }
        }
    }
    
    init(frame: CGRect) {
        super.init(nibName: nil, bundle: nil)
        
        self.tableView = UITableView(frame: frame)
        self.tableView.register(ProjectListTableViewCell.self, forCellReuseIdentifier: "cell-id")
        self.tableView.backgroundColor = AppColors.lightGray
        self.tableView.separatorStyle = .none
        
        syncData()
    }
    
    func updateForProject(_ project: Project) {
        self.projects.append(project)
        self.tableView.reloadData()
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }

    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return projects.count
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "cell-id", for: indexPath) as! ProjectListTableViewCell
        
        cell.syncView(project: projects[indexPath.row])

        return cell
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        self.delegate?.didSelectProject(project: projects[indexPath.row])
    }
}
