//
//  PersistantDomainObjectService.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation
import SQLite

class PersistantDomainObjectService {
    let fileURL = try! FileManager.default.url(for: .documentDirectory, in: .userDomainMask, appropriateFor: nil, create: false)
        .appendingPathComponent("DBExam.sqlite")
    
    private var db: Connection
    let domainObjects = Table("Parkings")
    let id = Expression<Int>("id")
    let name = Expression<String>("name")
    let type = Expression<String>("type")
    let status = Expression<String>("status")
    let power = Expression<Int>("power")
    
    private func createDatabase() {
        do {
            print("Accessing database")
            
            try db.run(domainObjects.create(ifNotExists: true) { t in
                t.column(id)
                t.column(name)
                t.column(type)
                t.column(status)
                t.column(power)
            })
        } catch let error {
            print(error)
        }
    }
    
    init() {
        db = try! Connection(fileURL.path)
        createDatabase()
    }
    
    func getAllDomainObjects() -> [DomainObject]? {
        print("LOG - Fetching all objects from database.")
        
        var local = [DomainObject]()
        
        do {
            for domainObject in try db.prepare(domainObjects) {
                let obj = DomainObject(id: domainObject[id],
                                       name: domainObject[name],
                                       type: domainObject[type],
                                       status: domainObject[status],
                                       power: domainObject[power])
                
                local.append(obj)
            }
            
            
            print("LOG - Fetching all objects from database complete.")
            return local
        } catch {
            print("LOG - Fetching all objects from database failed.")
            return nil
        }
    }
    
    func persistDomainObject(_ domainObject: DomainObject) -> Bool {
        do {
            print("LOG - Adding domain object to database.")
            try db.run(domainObjects.insert(id <- domainObject.id,
                                            name <- domainObject.name,
                                            type <- domainObject.type,
                                            status <- domainObject.status,
                                            power <- domainObject.power))
            print("LOG - Adding domain object to database complete.")
            return true
        } catch {
            print("LOG - Adding domain object to database failed.")
            return false
        }
    }

    func deleteDomainObject(_ domainObject: DomainObject) -> Bool {
        do {
            print("LOG - Deleting domain object from database.")
            let domainObjectToDelete = domainObjects.filter(id == domainObject.id)
            try db.run(domainObjectToDelete.delete())
            
            print("LOG - Deleting domain object from database complete.")
            return true
        } catch {
            print("LOG - Deleting domain object from database failed.")
            return false
        }
    }
    
    func isDomainObjectPersisted(_ domainObject: DomainObject) -> Bool {
        let domainObjectFiltered = domainObjects.filter(domainObject.id == id)
        do {
            if try db.scalar(domainObjectFiltered.count) == 1 {
                return true
            }
        } catch {
            return false
        }
        
        return false
    }
}

