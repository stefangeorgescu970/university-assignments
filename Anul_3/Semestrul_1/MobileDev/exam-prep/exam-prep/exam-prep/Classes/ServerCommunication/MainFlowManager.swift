//
//  MainFlowManager.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation
import UIKit

class MainFlowManager {
    static func navigateTo(userRole: UserRole) {
        performNavigation(toVC: SandBox.instance.buildInitialViewController(forRole: userRole))
    }
    
    static func goBackToMain() {
        performNavigation(toVC: InitialViewController())
    }
    
    private static func performNavigation(toVC: UIViewController) {
        let appDelegate = UIApplication.shared.delegate as! AppDelegate
        let window = appDelegate.window!
        
        UIView.transition(with: window, duration: 0.3, options: [.transitionFlipFromLeft, .preferredFramesPerSecond60], animations: {
            window.rootViewController = toVC
        })
    }
}
