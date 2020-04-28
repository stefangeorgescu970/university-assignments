//
//  MockProjectService.swift
//  DoIT
//
//  Created by Georgescu Stefan on 25/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation
import SQLite

class MockProjectService {
    
    let fileURL = try! FileManager.default.url(for: .documentDirectory, in: .userDomainMask, appropriateFor: nil, create: false)
        .appendingPathComponent("DoITDatabaseOfflineV2.sqlite")
    var db: Connection
    let projects = Table("Projects")
    let id = Expression<String>("project_id")
    let name = Expression<String>("name")
    
    init() {
        db = try! Connection(fileURL.path)
        createDatabase()
    }
    
    func publishIfNecessary() {
        do {
            let count = try db.scalar(projects.count)
            if count > 0 {
                for project in getAllUtil() {
                    GlobalData.sharedInstance.getProjectService().saveProject(project, callback: nil)
                }
            }
        } catch {
            
        }
    }
    
    private func createDatabase() {

        do {
            db = try Connection(fileURL.path)
            print("Connected to database")
        
            try db.run(projects.create(ifNotExists: true) { t in
                t.column(id, primaryKey: true)
                t.column(name)
            })

        } catch let error {
            print(error)
        }
    }
    
    func clearStorage() {
        do {
            try db.run(projects.delete())
        } catch {
            
        }
    }
    
    private func getAllUtil() -> [Project] {
        var localProjects: [Project] = []
        
        do {
            for project in try db.prepare(projects) {
                let newProj = Project(id: project[id], name: project[name])
                    
                localProjects.append(newProj)
                
            }
            
            return localProjects
        } catch {
            return [Project]()
        }
    }
    
    func getAllProjects(callback: @escaping (([Project]) -> ())) {
        callback(getAllUtil())
    }
    
    func saveProject(_ project: Project, callback: ((Bool) -> ())?) {
        do {
            try db.run(projects.insert(name <- project.name, id <- project.id))
            callback?(true)
        } catch {
            callback?(false)
        }
    }
    
    func getProject(_ byId: String) -> Project? {
        let project = projects.filter(id == byId)
        
        do {
            for project in try db.prepare(project) {
                return Project(id: project[id], name: project[name])
            }
        } catch {
            return nil
        }
        
        return nil
        
    }
}
