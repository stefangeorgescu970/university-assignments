//
//  IntegerResponseParser.swift
//  DoIT
//
//  Created by Stefan Georgescu on 24/11/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation
import SwiftyJSON

class IntegerResponseParser: ServerResponseParser {
    var result: Int?
    
    override func doParse(content: JSON) {
        if let newId = content.int {
            result = newId
        }
    }
    
    override func getResult() -> AnyObject? {
        return result as AnyObject
    }
}
