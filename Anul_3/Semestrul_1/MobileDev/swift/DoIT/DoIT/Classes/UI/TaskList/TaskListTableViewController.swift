//
//  TaskListTableViewController.swift
//  DoIT
//
//  Created by Georgescu Stefan on 25/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import UIKit


class TaskListTableViewController: UITableViewController {
    
    var tasks: [Task] = []
    var shouldDisplayCompleted = false
    
    init(frame: CGRect) {
        super.init(nibName: nil, bundle: nil)
        
        self.title = "Tasks"
        self.tableView = UITableView(frame: frame)
        self.tableView.register(TaskListTableViewCell.self, forCellReuseIdentifier: "task-list-cell")
        self.tableView.backgroundColor = AppColors.lightGray
        tableView.separatorStyle = .none
        
        self.shouldDisplayCompletedTasks(false)
    }
    
    func syncView() {
        self.tasks = []
        
        if Connectivity.isConnectedToInternet {
            GlobalData.sharedInstance.getTaskService().getAllTasks{ [unowned self] (tasks: [Task]?, error: NSError?) in
    
                var projectIdsSaved: [String] = []
    
                GlobalData.sharedInstance.getLocalProjectStorage().clearStorage()
                GlobalData.sharedInstance.getLocalTaskStorage().clearStorage()
                
                for task in tasks! {
                    GlobalData.sharedInstance.getLocalTaskStorage().saveTask(task, callback: nil)
                    
                    if !projectIdsSaved.contains(task.project.id) {
                        projectIdsSaved.append(task.project.id)
                        GlobalData.sharedInstance.getLocalProjectStorage().saveProject(task.project, callback: nil)
                    }
                    
                    if task.isCompleted == self.shouldDisplayCompleted {
                        self.tasks.append(task)
                    }
                }
                self.tableView.reloadData()
            }
        } else {
            GlobalData.sharedInstance.getLocalTaskStorage().getAllTasks { (tasks) in
                
                for task in tasks {
                    if task.isCompleted == self.shouldDisplayCompleted {
                        self.tasks.append(task)
                    }
                }
                
                self.tableView.reloadData()
            }
        }
    }
    
    func shouldDisplayCompletedTasks(_ should: Bool) {
        shouldDisplayCompleted = should
        self.syncView()
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override func tableView(_ tableView: UITableView, leadingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration? {
        let complete = completeAction(at: indexPath)
        return shouldDisplayCompleted ? nil : UISwipeActionsConfiguration(actions: [complete])
    }
    
    func completeAction(at indexPath: IndexPath) -> UIContextualAction {
        let action = UIContextualAction(style: .destructive, title: "Complete") { [unowned self] (action, view, completion) in
            let task = self.tasks[indexPath.row]
            
            if Connectivity.isConnectedToInternet {
                GlobalData.sharedInstance.getTaskService().completeTask(task) { (didComplete) in
                    self.tasks.remove(at: indexPath.row)
                    self.tableView.deleteRows(at: [indexPath], with: .automatic)
                }
                completion(true)
            } else {
                completion(false)
            }
        }
        action.backgroundColor = .green
        return action
    }
    
    override func tableView(_ tableView: UITableView, trailingSwipeActionsConfigurationForRowAt indexPath: IndexPath) -> UISwipeActionsConfiguration? {
        let delete = deleteAction(at: indexPath)
        return shouldDisplayCompleted ? nil : UISwipeActionsConfiguration(actions: [delete])
    }
    
    func deleteAction(at indexPath: IndexPath) -> UIContextualAction {
        let action = UIContextualAction(style: .destructive, title: "Delete") { [unowned self] (action, view, completion) in
            let task = self.tasks[indexPath.row]
            
            if Connectivity.isConnectedToInternet {
                GlobalData.sharedInstance.getTaskService().deleteTask(task) { (didRemove) in
                    self.tasks.remove(at: indexPath.row)
                    self.tableView.deleteRows(at: [indexPath], with: .automatic)
                }
                completion(true)
            } else {
                completion(false)
            }
        }
        action.backgroundColor = .red
        return action
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        self.tableView.backgroundColor = UIColor(displayP3Red: 1 / 255 * 56, green: 1 / 255 * 56, blue: 1 / 255 * 56, alpha: 1)
    }
    
    override func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return tasks.count
    }
    
    override func numberOfSections(in tableView: UITableView) -> Int {
        return 1
    }
    
    override func tableView(_ tableView: UITableView, heightForRowAt indexPath: IndexPath) -> CGFloat {
        return 80
    }
    
    override func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        guard let cell = tableView.dequeueReusableCell(withIdentifier: "task-list-cell", for: indexPath) as? TaskListTableViewCell else {
            fatalError()
        }
        
        cell.syncView(task: tasks[indexPath.row])
    
        return cell
    }
    
    override func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        let task = tasks[indexPath.row]
        let vc = TaskDetailsViewController(frame: self.view.frame, task: task)
        vc.delegate = self
        self.navigationController?.pushViewController(vc, animated: true)
    }

}

extension TaskListTableViewController: AddNewTaskViewControllerDelegate {
    func saveNewTask(_ task: Task) {
        
        if Connectivity.isConnectedToInternet {
            GlobalData.sharedInstance.getTaskService().saveTask(task) { [unowned self] (newId: String?) in
                if let newId = newId {
                    task.id = newId
                    self.tasks.append(task)
                    self.navigationController?.popViewController(animated: true)
                    self.tableView.reloadData()
                }
            }
        } else {
            self.tasks.append(task)
            self.tableView.reloadData()
            GlobalData.sharedInstance.getLocalTaskStorage().saveTask(task, callback: nil)
        }
        
        self.navigationController?.popViewController(animated: true)
    }
}

extension TaskListTableViewController: TaskDetailsViewControllerDelegate {
    func didCompleteTask(_ task: Task) {
        let index = self.tasks.firstIndex(of: task)
        if let index = index {
            self.tasks.remove(at: index)
            self.tableView.reloadData()
            self.navigationController?.popViewController(animated: true)
        } else {
            // handle some internal error
        }
    }
    
    func didUpdateTask(_ newTask: Task) {
        for (index, task) in self.tasks.enumerated() {
            if task.id == newTask.id {
                self.tasks[index] = newTask
                break
            }
        }
        self.tableView.reloadData()
        self.navigationController?.popViewController(animated: true)
    }
    
    func didRemoveTask(_ task: Task) {
        let index = self.tasks.firstIndex(of: task)
        if let index = index {
            self.tasks.remove(at: index)
            self.tableView.reloadData()
            self.navigationController?.popViewController(animated: true)
        } else {
            // handle some internal error
        }
    }
}
