//
//  DomainObjectListParser.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation
import SwiftyJSON

class DomainObjectListParser: ServerResponseParser {
    private var domainObjects = [DomainObject]()
    
    override func doParse(content: JSON) {
        if let domainObjectList = content.array {
            for domainObject in domainObjectList {
                if let domainObject = ParserUtils.parseDomainObject(content: domainObject) {
                    domainObjects.append(domainObject)
                }
            }
        }
    }
    
    override func getResult() -> AnyObject? {
        return domainObjects as AnyObject
    }
}
