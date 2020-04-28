//
//  SideBarTopView.swift
//  DoIT
//
//  Created by Stefan Georgescu on 30/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import UIKit

class SideBarTopView: UIView {
    
    let titleLabel: UILabel = {
        let label = UILabel()
        label.textColor = .white
        label.font = UIFont.boldSystemFont(ofSize: 16)
        return label
    }()
    
    init(frame: CGRect, user: UserRole) {
        super.init(frame: frame)
        
        titleLabel.text = user.rawValue
        titleLabel.sizeToFit()
        
        titleLabel.frame = CGRect(x: 20, y: self.frame.height / 2, width: titleLabel.frame.width, height: titleLabel.frame.height)
        
        addSubview(titleLabel)
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
