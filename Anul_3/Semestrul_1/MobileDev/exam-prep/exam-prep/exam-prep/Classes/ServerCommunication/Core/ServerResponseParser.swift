//
//  ServerResponseParser.swift
//  EasyHelp
//
//  Created by Georgescu Stefan on 16/09/2018.
//  Copyright © 2018 EasyHelp. All rights reserved.
//

import Foundation
import SwiftyJSON

class ServerResponseParser {
    func doParse(content: JSON) {
        
    }
    
    func getResult() -> AnyObject? {
        return nil
    }
    
    func parseError(content: JSON) -> AnyObject? {
        if let description = content["text"].string {
            return NSError(domain: "MD-Exam", code: 500, userInfo: ["description": description])
        }
        return NSError(domain: "MD-Exam", code: 500, userInfo: nil)
    }
    
    func parse(_ body: JSON) -> AnyObject? {
        doParse(content: body)

        return getResult()
    }
}
