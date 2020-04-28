//
//  ProfileView.swift
//  DoIT
//
//  Created by Stefan Georgescu on 30/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import UIKit

class ProfileView: UIView {
    
    let nameLabel: UILabel = {
        let label = UILabel()
        label.textColor = .white
        label.font = UIFont.boldSystemFont(ofSize: 16)
        return label
    }()
    
    let emailLabel: UILabel = {
        let label = UILabel()
        label.textColor = .white
        label.font = UIFont.systemFont(ofSize: 12)
        return label
    }()
    
    init(frame: CGRect, profile: ProfileData) {
        super.init(frame: frame)
        
        nameLabel.text = profile.name
        emailLabel.text = profile.email
        
        nameLabel.sizeToFit()
        emailLabel.sizeToFit()
        
        nameLabel.frame = CGRect(x: 20, y: self.frame.height / 3, width: nameLabel.frame.width, height: nameLabel.frame.height)
        emailLabel.frame = CGRect(x: 20, y: self.frame.height * 2 / 3, width: emailLabel.frame.width, height: emailLabel.frame.height)
        
        addSubview(nameLabel)
        addSubview(emailLabel)
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
