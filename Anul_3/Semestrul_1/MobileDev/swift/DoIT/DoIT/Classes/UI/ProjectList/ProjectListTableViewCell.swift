//
//  ProjectListTableViewCell.swift
//  DoIT
//
//  Created by Georgescu Stefan on 26/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import UIKit

class ProjectListTableViewCell: UITableViewCell {
    
    let nameLabel: UILabel = {
        let label = UILabel()
        label.textColor = AppColors.orange
        return label
    }()
    
    let separator: UIView = {
        let separator = UIView()
        separator.backgroundColor = AppColors.almostBlack
        return separator
    }()

    func syncView(project: Project) {
        self.backgroundColor = AppColors.lightGray
        
        nameLabel.text = project.name
        nameLabel.sizeToFit()
        nameLabel.frame = CGRect(x: 20, y: (frame.height  - nameLabel.frame.height) / 2, width: nameLabel.frame.width, height: nameLabel.frame.height)
        addSubview(nameLabel)
        
        separator.frame = CGRect(x: 0, y: self.frame.height - 0.5, width: self.frame.width + 2000, height: 0.5)
        addSubview(separator)
    }
}
