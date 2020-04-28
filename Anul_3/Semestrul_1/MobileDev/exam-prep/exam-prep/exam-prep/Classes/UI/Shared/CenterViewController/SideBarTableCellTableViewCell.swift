//
//  SideBarTableCellTableViewCell.swift
//  DoIT
//
//  Created by Georgescu Stefan on 25/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import UIKit

class SideBarTableCellTableViewCell: UITableViewCell {

    var nameLabel: UILabel = {
        let label = UILabel()
        label.textColor = AppColors.white
        return label
    }()
    
    var separator: UIView = {
        let separator = UIView()
        separator.backgroundColor = AppColors.almostBlack
        return separator
    }()
    
    
    func syncView(option: String) {
        nameLabel.text = option
        nameLabel.sizeToFit()
        
        nameLabel.center.y = frame.height / 2
        nameLabel.center.x = nameLabel.center.x + 20
        
        addSubview(nameLabel)
        
        separator.frame = CGRect(x: 0, y: self.frame.height - 0.5, width: self.frame.width, height: 0.5)
        addSubview(separator)
        
        self.backgroundColor = AppColors.darkBlue
    }
}
