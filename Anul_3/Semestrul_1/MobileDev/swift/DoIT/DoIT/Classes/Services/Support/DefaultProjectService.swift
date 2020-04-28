//
//  DefaultProjectService.swift
//  DoIT
//
//  Created by Stefan Georgescu on 24/11/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation
import FirebaseDatabase

class DefaultProjectService: ProjectService {
    var ref: DatabaseReference = Database.database().reference()
    
    func getAllProjects(callback: @escaping (([Project]?, NSError?) -> ())) {
        ref.child("projects").observeSingleEvent(of: .value) { (snapshot) in
            let postDict = snapshot.value as? [String : AnyObject] ?? [:]
            var projList: [Project] = []
            
            for (key, data) in postDict {
                let dataDict = data as? [String : AnyObject] ?? [:]
                let project = Project(id: key, name: dataDict["name"] as! String)
                projList.append(project)
            }
            
            callback(projList, nil)
        }
    }
    

    func saveProject(_ project: Project, callback: ((String?) -> ())?) {
        let key = ref.child("projects").childByAutoId().key!
        
        let projectDetails = ["name": project.name]
        
        let updates = ["/projects/\(key)": projectDetails]
        
        ref.updateChildValues(updates)
        
        callback?(key)
    }
    
    func getProject(_ byId: Int64) -> Project? {
        return nil
    }
}
