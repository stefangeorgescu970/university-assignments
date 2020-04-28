//
//  SideBarUtils.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation

class SideBarUtils {
    static func getOptionSet(forUserRole: UserRole) -> [String] {
        switch forUserRole {
        case .clientUser:
            return ClientRoleOptions.getAllOwnerRoleOptions()
        case .ownerUser:
            return OwnerRoleOptions.getAllOwnerRoleOptions()
        }
    }
}
