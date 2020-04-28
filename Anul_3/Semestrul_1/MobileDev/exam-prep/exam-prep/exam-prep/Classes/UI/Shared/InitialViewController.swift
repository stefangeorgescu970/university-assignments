//
//  InitialViewController.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation
import UIKit

class InitialViewController: UIViewController {
    
    var buttons = [UIButtonWithStringInfo]()
    
    override func loadView() {
        self.view = UIView(frame: UIScreen.main.bounds)
        view.backgroundColor = AppColors.white
        for role in UserRole.getAllUserRoles() {
            let button = UIButtonWithStringInfo(type: .custom)
            button.stringInfo = role
            buttons.append(button)
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        var currentY: CGFloat = 300
        
        for button in buttons {
            button.setTitle("\(button.stringInfo ?? "") Section", for: .normal)
            button.sizeToFit()
            button.backgroundColor = AppColors.darkBlue
            button.setTitleColor(.white, for: .normal)
            button.frame.size = CGSize(width: 250, height: 40)
            button.center = CGPoint(x: self.view.center.x, y: currentY)
            currentY += 100
            button.layer.cornerRadius = 8
            button.addTarget(self, action: #selector(InitialViewController.handleButtonTap(sender:)), for: .touchUpInside)
            self.view.addSubview(button)
        }

    }
    
    @objc func handleButtonTap(sender: UIButton) {
        if let sender = sender as? UIButtonWithStringInfo {
            if let userRole = UserRole.init(rawValue: sender.stringInfo ?? "") {
                MainFlowManager.navigateTo(userRole: userRole)
            }
        }
    }
}
