//
//  StringListParser.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation
import SwiftyJSON

class StringListParser: ServerResponseParser {
    private var strings = [String]()
    
    override func doParse(content: JSON) {
        if let array = content.array {
            for string in array {
                if let stringValue = string.string {
                    strings.append(stringValue)
                }
            }
        }
    }
    
    override func getResult() -> AnyObject? {
        return strings as AnyObject
    }
}
