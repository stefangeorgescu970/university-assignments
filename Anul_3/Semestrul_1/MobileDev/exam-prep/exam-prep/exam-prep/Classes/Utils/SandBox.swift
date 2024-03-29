//
//  SandBox.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation
import UIKit

class SandBox {
    static var instance = SandBox()
    
    func buildInitialViewController(forRole: UserRole) -> UIViewController {
        return ContainerViewController(forUserRole: forRole)
    }
}
