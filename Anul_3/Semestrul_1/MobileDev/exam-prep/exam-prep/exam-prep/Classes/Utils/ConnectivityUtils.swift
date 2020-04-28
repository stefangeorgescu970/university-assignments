//
//  ConnectivityUtils.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 27/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation
import Alamofire

class ConnectivityUtils {
    class var isConnectedToInternet:Bool {
        return NetworkReachabilityManager()!.isReachable
    }
}
