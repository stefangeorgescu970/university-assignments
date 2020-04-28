//
//  MockTaskService.swift
//  DoIT
//
//  Created by Georgescu Stefan on 24/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation
import SQLite

class MockTaskService {
    
    let fileURL = try! FileManager.default.url(for: .documentDirectory, in: .userDomainMask, appropriateFor: nil, create: false)
        .appendingPathComponent("DoITDatabaseOfflineV2.sqlite")
    
    private var db: Connection
    let projects = Table("Projects")
    let tasks = Table("Tasks")
    let id = Expression<String>("task_id")
    let name = Expression<String>("name")
    let dueDate = Expression<Date>("due_date")
    let description = Expression<String?>("description")
    let isCompleted = Expression<Bool>("is_completed")
    let completedDate = Expression<Date?>("completed_date")
    let projectId = Expression<String>("project_id")
    
    private func createDatabase() {
        do {
            print("Connected to database")
            
            try db.run(tasks.create(ifNotExists: true) { t in
                t.column(id, primaryKey: true)
                t.column(name)
                t.column(dueDate)
                t.column(description)
                t.column(isCompleted)
                t.column(completedDate)
                t.column(projectId)
                t.foreignKey(projectId, references: projects, id)
            })
            
            
        } catch let error {
            print(error)
        }
    }
    
    init() {
        db = try! Connection(fileURL.path)
        createDatabase()
    }
    
    func clearStorage() {
        do {
            try db.run(tasks.delete())
        } catch {
            
        }
    }
    
    func publishIfNecessary() {
        do {
            let count = try db.scalar(tasks.count)
            if count > 0 {
                for task in getAllUtil() {
                    GlobalData.sharedInstance.getTaskService().saveTask(task, callback: nil)
                }
            }
        } catch {
            
        }
    }
    
    private func getAllUtil() -> [Task] {
        var localTasks:[Task] = []
        
        do {
            for task in try db.prepare(tasks) {
                let project = GlobalData.sharedInstance.getLocalProjectStorage().getProject(task[projectId])
                
                if let project = project {
                    let newTask = Task(id: task[id], name: task[name], dueDate: task[dueDate], description: task[description],
                                       isCompleted: task[isCompleted], completedDate: task[completedDate], project: project)
                    
                    
                    localTasks.append(newTask)
                }
                
            }
            
            return localTasks
        } catch {
            return [Task]()
        }
    }
    
    func getAllTasks(callback: @escaping (([Task]) -> ())) {
        callback(getAllUtil())
    }
    
    func saveTask(_ task: Task, callback: ((Bool) -> ())?) {
        do {
            try db.run(tasks.insert(id <- task.id, name <- task.name, dueDate <- task.dueDate, description <- task.description, isCompleted <- task.isCompleted, completedDate <- task.completedDate, projectId <- task.project.id))
            UserDefaultsUtil.markPerformOfflineUpdate()
            callback?(true)
        } catch {
            callback?(false)
        }
    }
}
