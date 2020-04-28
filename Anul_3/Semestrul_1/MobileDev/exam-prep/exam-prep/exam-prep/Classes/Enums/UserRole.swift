//
//  UserRoles.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation

enum UserRole: String, CaseIterable {
    case clientUser = "Client"
    case ownerUser = "Owner"
    
    static func getAllUserRoles() -> [String] {
        return UserRole.allCases.map({ $0.rawValue })
    }
}
