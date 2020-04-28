//
//  DomainObject.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation

class DomainObject {
    
    // Always present attributes
    var id: Int
    var name: String
    
    // Attributes depending on the task
    var type: String
    var status: String
    var power: Int
    
    init(id: Int, name: String, type: String, status: String, power: Int) {
        self.id = id
        self.name = name
        
        self.type = type
        self.status = status
        self.power = power
    }
}
