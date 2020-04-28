//
//  TaskDetailsViewController.swift
//  DoIT
//
//  Created by Georgescu Stefan on 26/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import UIKit

protocol TaskDetailsViewControllerDelegate {
    func didUpdateTask(_ newTask: Task)
    func didRemoveTask(_ task: Task)
    func didCompleteTask(_ task: Task)
}

class TaskDetailsViewController: UIViewController {
    
    var delegate: TaskDetailsViewControllerDelegate?
    var taskDetailsView: TaskDetailsView!
    var task: Task
    
    init(frame: CGRect, task: Task) {
        self.task = task
        super.init(nibName: nil, bundle: nil)
        
        self.title = task.name
        self.taskDetailsView = TaskDetailsView(frame: frame, task: task)
        self.taskDetailsView.delegate = self
        self.view.addSubview(taskDetailsView)
        
        if !task.isCompleted {
            self.navigationItem.rightBarButtonItem = UIBarButtonItem(title: "Edit", style: .done, target: self, action: #selector(self.tapEdit))
        }
    }
    
    @objc func tapEdit() {
        if Connectivity.isConnectedToInternet {
            let vc = AddNewTaskViewController(frame: self.view.frame, task: task)
            vc.delegateUpdate = self
            self.navigationController?.pushViewController(vc, animated: false)
        } else {
            // display alert
        }
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

extension TaskDetailsViewController: UpdateTaskViewControllerDelegate {
    func updateTask(_ task: Task, newTask: Task) {
        
        if Connectivity.isConnectedToInternet {
            GlobalData.sharedInstance.getTaskService().updateTask(task, newTask: newTask) { (didUpdate) in
                if didUpdate {
                    newTask.id = task.id
                    self.taskDetailsView.task = newTask
                    self.taskDetailsView.syncView()
                    self.delegate?.didUpdateTask(newTask)
                } else {
                    // handle errors on update
                }
            }
        } else {
            // display alert
        }
    }
}

extension TaskDetailsViewController: TaskDetailsViewDelegate {
    func deleteTask(_ task: Task) {
        
        if Connectivity.isConnectedToInternet {
            GlobalData.sharedInstance.getTaskService().deleteTask(task) { [unowned self] (didRemove: Bool) in
                if didRemove {
                    self.delegate?.didRemoveTask(task)
                } else {
                    // handle error on delete
                }
            }
        } else {
            // display alert
        }
    }
    
    func completeTask(_ task: Task) {
        
        if Connectivity.isConnectedToInternet {
            GlobalData.sharedInstance.getTaskService().completeTask(task) { [unowned self] (didUpdate: Bool) in
                if didUpdate {
                    self.delegate?.didCompleteTask(task)
                } else {
                    // handle error on complete
                }
            }
        } else {
            // display alert
        }
    }
}
