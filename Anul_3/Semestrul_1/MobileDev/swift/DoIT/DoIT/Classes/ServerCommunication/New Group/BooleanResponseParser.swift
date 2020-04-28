//
//  BooleanResponseParser.swift
//  DoIT
//
//  Created by Stefan Georgescu on 24/11/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation
import SwiftyJSON

class BooleanResponseParser: ServerResponseParser {
    var result: Bool?
    
    override func doParse(content: JSON) {
        if let result = content.bool {
            self.result = result
        }
    }
    
    override func getResult() -> AnyObject? {
        return result as AnyObject
    }
}
