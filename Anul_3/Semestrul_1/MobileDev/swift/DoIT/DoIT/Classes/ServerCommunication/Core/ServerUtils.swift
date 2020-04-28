//
//  ServerUtils.swift
//  AcademicInfo
//
//  Created by Stefan Georgescu on 15/11/2018.
//  Copyright © 2018 Stefan Georgescu. All rights reserved.
//

import Foundation

class ServerUtils {
    struct Holder {
        static var serverProtocol: String?
        static var serverBaseUrl: String?
    }
    
    static var serverProtocol: String {
        get {
            return Holder.serverProtocol ?? "http"
        }
        set {
            Holder.serverProtocol = newValue
        }
    }
    
    static var serverBaseUrl: String {
        get {
            return Holder.serverBaseUrl ?? "localhost:8080"
        }
        set {
            Holder.serverBaseUrl = newValue
        }
    }
    
    static var serverAddress: String {
        return serverProtocol + "://" +  serverBaseUrl
    }
    
    static func getEndpointAddress(withEndpointPath endpoint: String) -> String {
        return serverAddress + "/" + endpoint
    }
}
