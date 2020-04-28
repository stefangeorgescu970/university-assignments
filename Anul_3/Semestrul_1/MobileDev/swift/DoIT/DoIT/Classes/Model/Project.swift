//
//  Project.swift
//  DoIT
//
//  Created by Georgescu Stefan on 25/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation

class Project: NSCoding {
    func encode(with aCoder: NSCoder) {
        
    }
    
    required init?(coder aDecoder: NSCoder) {
        id = aDecoder.decodeObject(forKey: "id") as! String
        name = aDecoder.decodeObject(forKey: "name") as! String
    }
    
    
    let name: String
    var id: String
    
    convenience init( name: String) {
        self.init(id: "unassinged", name: name)
    }
    
    init(id: String, name: String) {
        self.id = id
        self.name = name
    }
    
    func getJson() -> [String: Any] {
        var dict = [String: Any]()
        
        dict["id"] = id
        dict["name"] = name
        
        return dict
    }
}
