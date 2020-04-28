//
//  Server.swift
//  EasyHelp
//
//  Created by Georgescu Stefan on 16/09/2018.
//  Copyright © 2018 EasyHelp. All rights reserved.
//

import Foundation
import Alamofire
import SwiftyJSON

class Server {
    static let sharedInstance = Server()
    
    private struct Constants {
        static let backgroundSessionIdentifier: String = "md - exam - backgroundTask"
    }
    
    lazy private var networkManager: SessionManager = {
        let config = URLSessionConfiguration.background(withIdentifier: Constants.backgroundSessionIdentifier)
        config.httpAdditionalHeaders = Alamofire.SessionManager.defaultHTTPHeaders
        let manager = SessionManager(configuration: config)
        return manager
    }()
    
    func send(_ request: ServerRequest, parser: ServerResponseParser?, callback: SimpleServerCallback?, method: HTTPMethod = .get, encoding: ParameterEncoding = URLEncoding.default) {
        print("LOG - Sending server request to \(request.getEndpoint())")
        self.networkManager.request(request.getEndpoint(), method: method,  parameters: request.getParameters(), encoding: encoding).responseString { response in
            switch response.result {
            case .success(let value):
                let json = JSON(parseJSON: value)
                if let status = response.response?.statusCode {
                    if status != 200 {
                        if let error = parser?.parseError(content: json) as? NSError {
                            callback?.onError(error)
                        }
                    } else {
                        if let parsedData = parser?.parse(json) {
                            callback?.onSuccess(parsedData)
                        } else {
                            callback?.onSuccess(nil)
                        }
                    }
                }
            case .failure(let error):
                callback?.onError(error)
            }
        }
    }
}
