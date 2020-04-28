//
//  DomainObjectService.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation

class DomainObjectService {
    func getAvailableDomainObjects(callback: @escaping ([DomainObject]?, NSError?) -> ()) {
        let request = ServerRequest(endpoint: "places")
        
        let callback = SimpleServerCallback(successBlock: { (data) in
            print("LOG - Call for available domain objects complete.")
            callback(data as? [DomainObject], nil)
        }, errorBlock: { (error) in
            let error = error as! NSError
            print("LOG - Call for availalbe domain objects ended with error.")
            callback(nil, error)
        })
        
        Server.sharedInstance.send(request, parser: DomainObjectListParser(), callback: callback, method: .get)
    }
    
    func getAllDomainObjects(callback: @escaping ([DomainObject]?, NSError?) -> ()) {
        let request = ServerRequest(endpoint: "allPlaces")
        
        let callback = SimpleServerCallback(successBlock: { (data) in
            print("LOG - Call for all domain objects complete.")
            callback(data as? [DomainObject], nil)
        }, errorBlock: { (error) in
            let error = error as! NSError
            print("LOG - Call for all domain objects ended with error.")
            callback(nil, error)
        })
        
        Server.sharedInstance.send(request, parser: DomainObjectListParser(), callback: callback, method: .get)
    }
    
    func getPartOfDomainObjects(callback:  @escaping ([String]?, NSError?) -> ()) {
        let request = ServerRequest(endpoint: "genres")
        
        let callback = SimpleServerCallback(successBlock: { (data) in
            print("LOG - Call for restricted domain objects complete.")
            callback(data as? [String], nil)
        }, errorBlock: { (error) in
            let error = error as! NSError
            print("LOG - Call for restricted domain objects ended with error.")
            callback(nil, error)
        })
        
        Server.sharedInstance.send(request, parser: StringListParser(), callback: callback, method: .get)
    }
    
    func addDomainObject(_ domainObject: DomainObject, callback: @escaping (DomainObject?, NSError?) -> ()) {
        let request = ServerRequest(endpoint: "place")
        
        request.addParameter(key: "name", value: domainObject.name)
        request.addParameter(key: "type", value: domainObject.type)
        request.addParameter(key: "status", value: domainObject.status)
        request.addParameter(key: "power", value: domainObject.power)
        
        let callback = SimpleServerCallback(successBlock: { (data) in
            print("LOG - Call for adding a domain objects complete.")
            callback(data as? DomainObject, nil)
        }, errorBlock: { (error) in
            let error = error as! NSError
            print("LOG - Call for adding a domain objects ended with error.")
            callback(nil, error)
        })
        
        Server.sharedInstance.send(request, parser: DomainObjectParser(), callback: callback, method: .post)
    }
    
    func deleteDomainObject(_ domainObject: DomainObject, callback: @escaping (NSError?) -> ()) {
        let request = ServerRequest(endpoint: "place")
        
        request.setPathArgument(pathArg: "\(domainObject.id)")
        
        let callback = SimpleServerCallback(successBlock: { (data) in
            print("LOG - Call for deleting a domain object complete.")
            callback(nil)
        }, errorBlock: { (error) in
            let error = error as! NSError
            print("LOG - Call for deleting a domain object ended with error.")
            callback(error)
        })
        
        Server.sharedInstance.send(request, parser: ServerResponseParser(), callback: callback, method: .delete)
    }
    
    func freeParkingPlace(_ domainObject: DomainObject, callback: @escaping (NSError?) -> ()) {
        let request = ServerRequest(endpoint: "free")
        
        request.addParameter(key: "id", value: domainObject.id)
        
        let callback = SimpleServerCallback(successBlock: { (data) in
            print("LOG - Call for freeing a domain object complete.")
            callback(nil)
        }, errorBlock: { (error) in
            let error = error as! NSError
            print("LOG - Call for freeing a domain object ended with error.")
            callback(error)
        })
        
        Server.sharedInstance.send(request, parser: ServerResponseParser(), callback: callback, method: .post)
    }
    
    func takeParkingSpot(_ domainObject: DomainObject, callback: @escaping (NSError?) -> ()) {
        let request = ServerRequest(endpoint: "take")
        
        request.addParameter(key: "id", value: domainObject.id)
        
        let callback = SimpleServerCallback(successBlock: { (data) in
            print("LOG - Call for freeing a domain object complete.")
            callback(nil)
        }, errorBlock: { (error) in
            let error = error as! NSError
            print("LOG - Call for freeing a domain object ended with error.")
            callback(error)
        })
        
        Server.sharedInstance.send(request, parser: ServerResponseParser(), callback: callback, method: .post)
    }
}
