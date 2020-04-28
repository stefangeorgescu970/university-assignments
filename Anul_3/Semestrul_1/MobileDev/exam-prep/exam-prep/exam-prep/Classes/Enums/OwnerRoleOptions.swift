//
//  OwnerRoleOptions.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation

enum OwnerRoleOptions: String, CaseIterable {
    case viewDomainObject = "Parking"
    case goBack = "Go Back"
    
    static func getAllOwnerRoleOptions() -> [String] {
        return OwnerRoleOptions.allCases.map({ $0.rawValue })
    }
}
