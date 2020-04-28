//
//  ServerUtils.swift
//  AcademicInfo
//
//  Created by Stefan Georgescu on 15/11/2018.
//  Copyright © 2018 Stefan Georgescu. All rights reserved.
//

import Foundation

class ServerUtils {
    static let port = "2029"
    static let host = "localhost"
    
    static func buildEndpointAddress(endpoint: String) -> String {
        return "http://\(host):\(port)/\(endpoint)"
    }
}
