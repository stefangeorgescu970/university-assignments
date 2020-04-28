//
//  DomainObjectDetailsView.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import UIKit

protocol DomainObjectDetailsViewDelegate: class {
    func domainObjectDetailsRequestedActionOn(_ domainObject: DomainObject)
}

class DomainObjectDetailsView: UIView {
    private let domainObject: DomainObject
    weak var delegate: DomainObjectDetailsViewDelegate?
    
    private let rowSpacing: CGFloat = 15
    private let marginSpacing: CGFloat = 20
    private let separatorSpacingAbove: CGFloat = 10
    
    let actionButton: ButtonWithActivity = {
        let button = ButtonWithActivity()
        button.setTitleColor(.white, for: .normal)
        button.backgroundColor = AppColors.darkBlue
        button.layer.cornerRadius = 8
        
        button.addTarget(self, action: #selector(DomainObjectDetailsView.didPressActionButton), for: .touchUpInside)
        return button
    }()
    
    init(domainObject: DomainObject, isPersisted: Bool) {
        self.domainObject = domainObject
        super.init(frame: UIScreen.main.bounds)
        self.backgroundColor = AppColors.white
        var currentOffsetY: CGFloat = 100
       
        var rowHeigth = addDefaultInfoRow(toView: self, leftText: "Id", rightText: "\(domainObject.id)", marginSpacing: 20, yOffset: currentOffsetY)
        currentOffsetY += rowHeigth + separatorSpacingAbove
        addSeparator(view: self, yOffset: currentOffsetY)
        currentOffsetY += rowSpacing + 1
        
        rowHeigth = addDefaultInfoRow(toView: self, leftText: "Title", rightText: domainObject.name, marginSpacing: 20, yOffset: currentOffsetY)
        currentOffsetY += rowHeigth + separatorSpacingAbove
        addSeparator(view: self, yOffset: currentOffsetY)
        currentOffsetY += rowSpacing + 1
        
        rowHeigth = addDefaultInfoRow(toView: self, leftText: "Type", rightText: domainObject.type, marginSpacing: 20, yOffset: currentOffsetY)
        currentOffsetY += rowHeigth + separatorSpacingAbove
        addSeparator(view: self, yOffset: currentOffsetY)
        currentOffsetY += rowSpacing + 1
        
        rowHeigth = addDefaultInfoRow(toView: self, leftText: "Status", rightText: domainObject.status, marginSpacing: 20, yOffset: currentOffsetY)
        currentOffsetY += rowHeigth + separatorSpacingAbove
        addSeparator(view: self, yOffset: currentOffsetY)
        currentOffsetY += rowSpacing + 1
        
        rowHeigth = addDefaultInfoRow(toView: self, leftText: "Power", rightText: "\(domainObject.power)", marginSpacing: 20, yOffset: currentOffsetY)
        currentOffsetY += rowHeigth + separatorSpacingAbove
        addSeparator(view: self, yOffset: currentOffsetY)
        currentOffsetY += rowSpacing + 1
        
        actionButton.setTitle(isPersisted ? "Free Parking Spot" : "Reserve Parking Spot", for: .normal)
        actionButton.frame = CGRect(x: 20 * 2,
                                    y: currentOffsetY,
                                    width: frame.width - 4 * 20,
                                    height: 40)
        addSubview(actionButton)
    
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    @objc func didPressActionButton() {
        actionButton.showLoading()
    
        self.delegate?.domainObjectDetailsRequestedActionOn(self.domainObject)
    }
    
    private func addDefaultInfoRow(toView: UIView, leftText: String, rightText: String, marginSpacing: CGFloat, yOffset: CGFloat) -> CGFloat {
        let leftLabel = UILabel()
        leftLabel.font = UIFont.boldSystemFont(ofSize: 16)
        leftLabel.text = leftText
        leftLabel.sizeToFit()
        leftLabel.textColor = AppColors.darkBlue
        leftLabel.frame = CGRect(x: marginSpacing,
                                 y: yOffset,
                                 width: leftLabel.frame.width,
                                 height: leftLabel.frame.height)
        toView.addSubview(leftLabel)
        
        let rightLabelMaximumWidth = toView.frame.width - leftLabel.frame.width - 3 * marginSpacing
        
        let rightLabel = UILabel()
        rightLabel.textColor = AppColors.darkBlue
        rightLabel.text = rightText
        rightLabel.sizeToFit()
        rightLabel.lineBreakMode = .byTruncatingMiddle
        rightLabel.frame = CGRect(x: max(toView.frame.width - marginSpacing - rightLabel.frame.width, toView.frame.width - marginSpacing - rightLabelMaximumWidth),
                                  y: yOffset,
                                  width: min(rightLabelMaximumWidth, rightLabel.frame.width),
                                  height: rightLabel.frame.height)
        toView.addSubview(rightLabel)
        
        return rightLabel.frame.height
    }
    
    private func addSeparator(view: UIView, yOffset: CGFloat) {
        let sep = UIView(frame: CGRect(x: 20, y: yOffset, width: view.frame.width - 40, height: 0.5))
        sep.backgroundColor = .black
        view.addSubview(sep)
    }
    
}
