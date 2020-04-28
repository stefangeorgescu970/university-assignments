//
//  ClientDomainObjectCell.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import UIKit

class ClientDomainObjectCell: UITableViewCell {
    
    internal let nameLabel: UILabel = {
        let label = UILabel()
        label.textColor = AppColors.darkBlue
        label.font = UIFont.boldSystemFont(ofSize: 18)
        return label
    }()

    internal let leftDetailLabel: UILabel = {
        let label = UILabel()
        label.textColor = AppColors.almostBlack
        label.font = UIFont.systemFont(ofSize: 14)
        return label
    }()
    
    internal let rightDetailLabel: UILabel = {
        let label = UILabel()
        label.textColor = AppColors.almostBlack
        label.font = UIFont.systemFont(ofSize: 14)
        return label
    }()
    
    internal var separator: UIView = {
        let separator = UIView()
        separator.backgroundColor = AppColors.almostBlack
        return separator
    }()
    
    func syncView(domainObject: DomainObject) {
        self.backgroundColor = .white
        
        nameLabel.text = domainObject.name
        nameLabel.sizeToFit()
        nameLabel.frame.origin = CGPoint(x: 20, y: (frame.height - nameLabel.frame.height) / 3)
        addSubview(nameLabel)
        
        leftDetailLabel.text = domainObject.type
        leftDetailLabel.sizeToFit()
        leftDetailLabel.frame.origin = CGPoint(x: 20, y: frame.height * 2 / 3)
        addSubview(leftDetailLabel)
        
        rightDetailLabel.text = domainObject.status
        rightDetailLabel.sizeToFit()
        rightDetailLabel.frame.origin = CGPoint(x: frame.width - 20 - rightDetailLabel.frame.width, y: frame.height * 2 / 3)
        addSubview(rightDetailLabel)
        
        separator.frame = CGRect(x: 0, y: frame.height - 0.7, width: frame.width, height: 0.7)
        addSubview(separator)
    }
    
}

