//
//  TaskService.swift
//  DoIT
//
//  Created by Georgescu Stefan on 24/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation

protocol TaskService {
    func getAllTasks(callback: @escaping(([Task]?, NSError?) -> ()))
    
    func saveTask(_ task: Task, callback: ((String?) -> ())?)
    
    func completeTask(_ task: Task, callback: ((Bool) -> ())?)
    
    func deleteTask(_ task: Task, callback: ((Bool) -> ())?)
    
    func updateTask(_ task: Task, newTask: Task, callback: ((Bool) -> ())?)
}
