//
//  ProjectService.swift
//  DoIT
//
//  Created by Georgescu Stefan on 25/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation

protocol ProjectService {
    func getAllProjects(callback: @escaping(([Project]?, NSError?) -> ()))
    
    func saveProject(_ project: Project, callback: ((String?) -> ())?)
    
    func getProject(_ byId: Int64) -> Project?
}
