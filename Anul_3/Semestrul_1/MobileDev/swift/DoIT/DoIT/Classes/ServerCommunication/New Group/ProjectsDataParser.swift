//
//  ProjectsDataParser.swift
//  DoIT
//
//  Created by Stefan Georgescu on 24/11/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation
import SwiftyJSON

class ProjectsDataParser: ServerResponseParser {
    private var projects: [Project] = []
    
    override func doParse(content: JSON) {
        if let projectsArray = content["projects"].array {
            for project in projectsArray {
                let project = ProjectsDataParser.parseProject(content: project)
                if let project = project {
                    projects.append(project)
                }
            }
        }
    }
    
    override func getResult() -> AnyObject? {
        return projects as AnyObject
    }
    
    public static func parseProject(content: JSON?) -> Project? {
        guard let id = content?["id"].string, let name = content?["name"].string else {
            return nil
        }
        
        return Project(id: id, name: name)
    }
}
