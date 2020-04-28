//
//  DefaultTaskService.swift
//  DoIT
//
//  Created by Stefan Georgescu on 24/11/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation
import FirebaseDatabase

class DefaultTaskService: TaskService {
    var ref: DatabaseReference = Database.database().reference()
    
    func getAllTasks(callback: @escaping (([Task]?, NSError?) -> ())) {
        ref.child("tasks").observeSingleEvent(of: .value) { (snapshot) in
            let postDict = snapshot.value as? [String : AnyObject] ?? [:]
            var taskList: [Task] = []
            
            for (key, data) in postDict {
                let dataDict = data as? [String : AnyObject] ?? [:]
                let projDataDict = dataDict["project"] as? [String : AnyObject] ?? [:]
                
                let project = Project(id: projDataDict["key"] as! String, name: projDataDict["name"] as! String)
                
                let task = Task(id: key,
                                name: dataDict["name"] as! String,
                                dueDate: DateUtils.getDateFromServer(fromString: dataDict["dueDate"] as! String)!,
                                description: dataDict["description"] as? String,
                                isCompleted: dataDict["isCompleted"] as! Bool,
                                completedDate: DateUtils.getDateFromServer(fromString: dataDict["dueDate"] as! String),
                                project: project)
                taskList.append(task)
            }
            
            callback(taskList, nil)
        }
    }
    
    func saveTask(_ task: Task, callback: ((String?) -> ())?) {
        let key = ref.child("tasks").childByAutoId().key!

        let projectDetails = ["key": task.project.id, "name": task.project.name]
        
        var taskDetails = ["name": task.name,
                           "dueDate": DateUtils.getDateStringForServer(fromDate: task.dueDate),
                           "isCompleted": task.isCompleted,
                           "project": projectDetails] as [String : Any]
        
        if let descr = task.description {
            taskDetails["description"] = descr
        }
        
        if let complDate = task.completedDate {
            taskDetails["completedDate"] = DateUtils.getDateStringForServer(fromDate: complDate)
        }
                           
        
        let updates = ["/tasks/\(key)": taskDetails]
        
        ref.updateChildValues(updates)
        
        callback?(key)
    }
    
    func completeTask(_ task: Task, callback: ((Bool) -> ())?) {
        task.isCompleted = true
        task.completedDate = Date()
        self.updateTask(task, newTask: task, callback: callback)
    }
    
    func deleteTask(_ task: Task, callback: ((Bool) -> ())?) {
        ref.child("tasks").child(task.id).removeValue()
        
        callback?(true)
    }
    
    func updateTask(_ task: Task, newTask: Task, callback: ((Bool) -> ())?) {
       let key = task.id
        
        let projectDetails = ["key": newTask.project.id, "name": newTask.project.name]
        
        var taskDetails = ["name": newTask.name,
                           "dueDate": DateUtils.getDateStringForServer(fromDate: newTask.dueDate),
                           "isCompleted": newTask.isCompleted,
                           "project": projectDetails] as [String : Any]
        
        if let descr = newTask.description {
            taskDetails["description"] = descr
        }
        
        if let complDate = newTask.completedDate {
            taskDetails["completedDate"] = DateUtils.getDateStringForServer(fromDate: complDate)
        }
        
        
        let updates = ["/tasks/\(key)": taskDetails]
        
        ref.updateChildValues(updates)
        
        callback?(true)
    }
}
