//
//  ClientRoleOptions.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation

enum ClientRoleOptions: String, CaseIterable {
    case viewPartOfDomainObject = "Parking"
    case viewSavedDomainObject = "My Places"
    case goBack = "Go Back"
    
    static func getAllOwnerRoleOptions() -> [String] {
        return ClientRoleOptions.allCases.map({ $0.rawValue })
    }
}

