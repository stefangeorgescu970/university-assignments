//
//  UserDefaultsUtil.swift
//  DoIT
//
//  Created by Stefan Georgescu on 24/11/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation

class UserDefaultsUtil {
    static private let didKey = "userdefs-did-update-list"
    static private let defaults = UserDefaults.standard
    
    static func didPerformOfflineUpdate() -> Bool {
        let did = defaults.bool(forKey: didKey)
        return did
    }
    
    static func markPerformOfflineUpdate() {
        defaults.set(true, forKey: didKey)
    }
    
    static func clearOfflineUpdateFlag() {
        defaults.set(false, forKey: didKey)
    }
}
