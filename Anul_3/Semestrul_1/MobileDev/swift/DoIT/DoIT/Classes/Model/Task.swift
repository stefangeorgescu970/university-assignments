//
//  Task.swift
//  DoIT
//
//  Created by Georgescu Stefan on 25/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation

class Task: NSCoding {
    func encode(with aCoder: NSCoder) {
        aCoder.encode(id, forKey: "id")
        aCoder.encode(name, forKey: "name")
    }
    
    required init?(coder aDecoder: NSCoder) {
        id = aDecoder.decodeObject(forKey: "id") as! String
        name = aDecoder.decodeObject(forKey: "name") as! String
        description = aDecoder.decodeObject(forKey: "description") as? String
        isCompleted = aDecoder.decodeObject(forKey: "isCompleted") as! Bool
        dueDate = aDecoder.decodeObject(forKey: "dueDate") as! Date
        completedDate = aDecoder.decodeObject(forKey: "completedDate") as? Date
        project = aDecoder.decodeObject(forKey: "project") as! Project
    }
    

    var id: String
    var name: String
    var dueDate: Date
    var description: String?
    var isCompleted = false
    var completedDate: Date?
    var project: Project
    
    convenience init(name: String, dueDate: Date, project: Project) {
        self.init(id: "unassinged", name: name, dueDate: dueDate, description: nil, project: project)
    }
    
    convenience init(name: String, dueDate: Date, description: String?, project: Project) {
        self.init(id: "unassinged", name: name, dueDate: dueDate, description: description, project: project)
    }
    
    convenience init(id: String, name: String, dueDate: Date, project: Project) {
        self.init(id: id, name: name, dueDate: dueDate, description: nil, project: project)
    }
    
    convenience init(id: String, name: String, dueDate: Date, description: String?, isCompleted: Bool, completedDate: Date?, project: Project) {
        self.init(id: id, name: name, dueDate: dueDate, description: description, project: project)
        self.isCompleted = isCompleted
        self.completedDate = completedDate
    }
    
    init(id: String, name: String, dueDate: Date, description: String?, project: Project) {
        self.id = id
        self.name = name
        self.dueDate = dueDate
        self.project = project
        self.description = description
    }
    
    func getDueDateFormatted() -> String {
        return DateUtils.getString(fromDate: dueDate)
    }
}

extension Task: Equatable {
    static func == (lhs: Task, rhs: Task) -> Bool {
        return lhs.name == rhs.name
    }
}
