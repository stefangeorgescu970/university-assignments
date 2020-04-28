//
//  TasksDataParser.swift
//  DoIT
//
//  Created by Stefan Georgescu on 24/11/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation
import SwiftyJSON

class TasksDataParser: ServerResponseParser {
    private var tasks: [Task] = []
    
    override func doParse(content: JSON) {
        if let tasksList = content["tasks"].array {
            for task in tasksList {
                let task = parseTask(content: task)
                if let task = task {
                    tasks.append(task)
                }
            }
        }
    }
    
    override func getResult() -> AnyObject? {
        return tasks as AnyObject
    }
    
    private func parseTask(content: JSON) -> Task? {
        guard let id = content["id"].string,
            let name = content["name"].string,
            let isCompleted = content["isCompleted"].bool,
            let dueDate = content["dueDate"].string,
            let project = content["project"].dictionary,
            let description = content["description"].string else {
                return nil
        }
        
        let projectObj = ProjectsDataParser.parseProject(content: JSON(rawValue: project))
        if let projectObj = projectObj {
            
            let task = Task(id: id, name: name, dueDate: DateUtils.getDateFromServer(fromString: dueDate)!, description: description, isCompleted: isCompleted, completedDate: nil, project: projectObj)
            
            let completedDate = content["completedDate"].string
            if let completedDate = DateUtils.getDateFromServer(fromString: completedDate ?? "") {
                task.completedDate = completedDate
            }
            
            return task
        }
        return nil
    }
}
