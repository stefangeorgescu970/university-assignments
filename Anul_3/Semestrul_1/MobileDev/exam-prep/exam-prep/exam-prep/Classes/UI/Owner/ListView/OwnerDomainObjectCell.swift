//
//  OwnerDomainObjectCell.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import UIKit

class OwnerDomainObjectCell: ClientDomainObjectCell {
    
    private let extraInfoLabel: UILabel = {
        let label = UILabel()
        label.textColor = AppColors.darkBlue
        label.font = UIFont.systemFont(ofSize: 14)
        return label
    }()
    
    override func syncView(domainObject: DomainObject) {
        super.syncView(domainObject: domainObject)
        
        extraInfoLabel.text = "\(domainObject.power)"
        extraInfoLabel.sizeToFit()
        extraInfoLabel.frame.origin = CGPoint(x: 20, y: frame.height / 2)
        addSubview(extraInfoLabel)
    }
}
