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
        if let description = content.string {
            return NSError(domain: "AcademicInfo", code: 500, userInfo: ["description": description])
        }
        return NSError(domain: "AcademicInfo", code: 500, userInfo: nil)
    }
    
    func parse(_ body: JSON) -> AnyObject? {
        let success = body["status"].boolValue
        
        if success {
            let response = body["object"]
            if response.exists(){
                doParse(content: response)
            } else {
                return success as AnyObject
            }
        } else {
            let error = body["exception"]
            if error.exists() {
                return parseError(content: error)
            } else {
                return success as AnyObject
            }
        }
        return getResult()
    }
}
