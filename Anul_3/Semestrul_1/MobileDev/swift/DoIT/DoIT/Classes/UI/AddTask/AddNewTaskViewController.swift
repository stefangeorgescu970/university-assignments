//
//  AddNewTaskViewController.swift
//  DoIT
//
//  Created by Georgescu Stefan on 26/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import UIKit

protocol AddNewTaskViewControllerDelegate: class {
    func saveNewTask(_ task: Task)
}

protocol UpdateTaskViewControllerDelegate: class {
    func updateTask(_ task: Task, newTask: Task)
}

class AddNewTaskViewController: UIViewController {
    
    var newTaskView: AddNewTaskView!
    var delegate: AddNewTaskViewControllerDelegate?
    var delegateUpdate: UpdateTaskViewControllerDelegate?
    var task: Task?
    
    init(frame: CGRect, task: Task? = nil) {
        
        self.task = task
        super.init(nibName: nil, bundle: nil)
        
        self.title = "Add New Task"
        
        if let task = task {
            
            self.title = "Edit Task Details"
            newTaskView = AddNewTaskView(frame: frame, task: task)
            self.view = newTaskView
            newTaskView.delegate = self
            
            self.navigationItem.rightBarButtonItem = UIBarButtonItem(title: "Update", style: .done, target: self, action: #selector(self.tapUpdate))
            
        } else {
            
            newTaskView = AddNewTaskView(frame: frame)
            self.view = newTaskView
            newTaskView.delegate = self
            
            self.navigationItem.rightBarButtonItem = UIBarButtonItem(title: "Save", style: .done, target: self, action: #selector(self.tapSave))
        }
        
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        self.view.endEditing(true)
    }

    @objc func tapUpdate() {
        let newTask = newTaskView.getNewTask()
        
        if let newTask = newTask {
            delegateUpdate?.updateTask(task!, newTask: newTask)
        } else {
            let alert = UIAlertController(title: "DoIT", message: "Please enter correct data.", preferredStyle: UIAlertController.Style.alert)
            alert.addAction(UIAlertAction(title: "OK", style: UIAlertAction.Style.default, handler: nil))
            self.present(alert, animated: true, completion: nil)
        }
    }
    
    @objc func tapSave() {
        let newTask = newTaskView.getNewTask()
        
        if let newTask = newTask {
            delegate?.saveNewTask(newTask)
        } else {
            let alert = UIAlertController(title: "DoIT", message: "Please enter correct data.", preferredStyle: UIAlertController.Style.alert)
            alert.addAction(UIAlertAction(title: "OK", style: UIAlertAction.Style.default, handler: nil))
            self.present(alert, animated: true, completion: nil)
        }
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

extension AddNewTaskViewController: AddNewTaskViewDelegate {
    
    func didRequestSelectProject() {
        let newVC = ProjectListTableViewController(frame: self.view.frame)
        newVC.delegate = self
        self.navigationController?.pushViewController(newVC, animated: true)
    }
}

extension AddNewTaskViewController: ProjectListTableViewControllerDelegate {
    func didSelectProject(project: Project) {
        print("Did select project with name \(project.name)")
        newTaskView.selectedProject = project
        self.navigationController?.popViewController(animated: true)
    }
}
