//
//  LoadingView.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import UIKit

class LoadingView: UIView {
    
    private let actInd: UIActivityIndicatorView = UIActivityIndicatorView()
    
    init(frame: CGRect, withBgColor: UIColor? = .clear) {
        super.init(frame: frame)
        actInd.frame = CGRect(x: 0, y: 0, width: 60, height: 60)
        actInd.center = self.center
        actInd.hidesWhenStopped = true
        actInd.style = .whiteLarge
        actInd.color = AppColors.darkBlue
        self.backgroundColor = withBgColor
        addSubview(actInd)
        actInd.startAnimating()
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
