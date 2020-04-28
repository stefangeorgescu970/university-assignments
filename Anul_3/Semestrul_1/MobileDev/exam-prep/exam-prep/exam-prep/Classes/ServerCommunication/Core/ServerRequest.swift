//
//  ServerRequest.swift
//  EasyHelp
//
//  Created by Georgescu Stefan on 16/09/2018.
//  Copyright © 2018 EasyHelp. All rights reserved.
//

import Foundation

class ServerRequest {
    private var apiEndpoint: String
    private var parameters = [String:Any]()
    private var pathArgument: String?
    
    init(endpoint: String) {
        apiEndpoint = ServerUtils.buildEndpointAddress(endpoint: endpoint)
    }
    
    func getEndpoint() -> String {
        return apiEndpoint + (pathArgument != nil ? "/\(pathArgument!.replacingOccurrences(of: " ", with: "%20"))" : "")
    }
    
    func setPathArgument(pathArg: String) {
        self.pathArgument = pathArg
    }

    func addParameter(key: String, value: Any) {
        parameters[key] = value
    }
    
    func getParameters() -> [String : Any] {
        return parameters
    }
}
