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
        static let backgroundSessionIdentifier: String = "academicInfo - backgroundTask"
    }
    
    lazy private var networkManager: SessionManager = {
        let config = URLSessionConfiguration.background(withIdentifier: Constants.backgroundSessionIdentifier)
        config.httpAdditionalHeaders = Alamofire.SessionManager.defaultHTTPHeaders
        let manager = SessionManager(configuration: config)
        return manager
    }()
    
    func send(_ request: ServerRequest, parser: ServerResponseParser?, callback: SimpleServerCallback?) {
        self.networkManager.request(request.getEndpoint(), method: .post,  parameters: request.getParameters(), encoding: JSONEncoding.default).responseString { response in
            switch response.result {
            case .success(let value):
                let json = JSON(parseJSON: value)
                if let parsedData = parser?.parse(json) {
                    if let error = parsedData as? NSError {
                        callback?.onError(error)
                    } else {
                        callback?.onSuccess(parsedData)
                    }
                } else {
                    callback?.onError(nil)
                }
            case .failure(let error):
                let myError = NSError(domain: "AcademicInfo", code: 500, userInfo: ["description": error.localizedDescription])
                callback?.onError(myError)
            }
        }
    }
}
