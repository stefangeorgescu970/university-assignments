//
//  ParserUtils.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation
import SwiftyJSON

class ParserUtils {
    static func parseDomainObject(content: JSON) -> DomainObject? {
        guard let id = content["id"].int,
            let name = content["name"].string,
            let type = content["type"].string,
            let status = content["status"].string else {
                return nil
        }
        
        if let power = content["power"].int {
            return DomainObject(id: id, name: name, type: type, status: status, power: power)
        } else if let power = content["power"].string {
            if let power = Int(power) {
                return DomainObject(id: id, name: name, type: type, status: status, power: power)
            }
        }
        
        return nil
    }
}
