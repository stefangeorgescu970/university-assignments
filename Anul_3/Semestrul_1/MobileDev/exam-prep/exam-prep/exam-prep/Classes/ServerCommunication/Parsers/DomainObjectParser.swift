//
//  DomainObjectParser.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation
import SwiftyJSON

class DomainObjectParser: ServerResponseParser {
    private var domainObject: DomainObject?
    
    override func doParse(content: JSON) {
        if let domainObject = ParserUtils.parseDomainObject(content: content) {
            self.domainObject = domainObject
        }
    }
    
    override func getResult() -> AnyObject? {
        return domainObject as AnyObject
    }

}
