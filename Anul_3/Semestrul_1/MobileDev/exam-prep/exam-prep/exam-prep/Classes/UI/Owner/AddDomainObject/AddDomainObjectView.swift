//
//  AddDomainObjectView.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import UIKit

protocol AddDomainObjectViewDelegate: class {
    func addDomainObjectViewDidRequestAdd(_ domainObject: DomainObject)
}

class AddDomainObjectView: UIView {
    
    // MARK: - Properties Declaration
    
    fileprivate struct Constants {
        static let leftMargin: CGFloat = 40
        static let rowSpacing: CGFloat = 14
        static let labelSpacing: CGFloat = 4
    }
    
    private var isShowingError: Bool = false
    weak var delegate: AddDomainObjectViewDelegate?
    
    // MARK: - View Properties Declaration
    
    private let pageTitleLabel: UILabel = {
        let label = UILabel()
        label.text = "Add new parking spot"
        label.textColor = AppColors.darkBlue
        label.font = UIFont.boldSystemFont(ofSize: 24)
        label.sizeToFit()
        return label
    }()
    
    private let nameLabel: UILabel = {
        let label = UILabel()
        label.text = "Name"
        label.textColor = AppColors.darkBlue
        label.font = UIFont.boldSystemFont(ofSize: 18)
        label.sizeToFit()
        return label
    }()
    
    private let nameInput: UITextField = {
        
        let textField = UITextField()
        textField.attributedPlaceholder = NSAttributedString(string: "The name of your parking spot",
                                                             attributes: [NSAttributedString.Key.foregroundColor: UIColor.lightGray])
        textField.font = UIFont.systemFont(ofSize: 16)
        textField.borderStyle = .none
        textField.textColor = AppColors.darkBlue
        
        textField.addTarget(self, action: #selector(AddDomainObjectView.userEditedText), for: .editingChanged)
        
        return textField
    }()
    
    private let typeLabel: UILabel = {
        let label = UILabel()
        label.text = "Type"
        label.textColor = AppColors.darkBlue
        label.font = UIFont.boldSystemFont(ofSize: 18)
        label.sizeToFit()
        return label
    }()
    
    private let typeInput: UITextField = {
        
        let textField = UITextField()
        textField.attributedPlaceholder = NSAttributedString(string: "Parking spot type",
                                                             attributes: [NSAttributedString.Key.foregroundColor: UIColor.lightGray])
        textField.font = UIFont.systemFont(ofSize: 16)
        textField.borderStyle = .none
        textField.textColor = AppColors.darkBlue
        
        textField.addTarget(self, action: #selector(AddDomainObjectView.userEditedText), for: .editingChanged)
        
        return textField
    }()
    
    private let statusLabel: UILabel = {
        let label = UILabel()
        label.text = "Status"
        label.textColor = AppColors.darkBlue
        label.font = UIFont.boldSystemFont(ofSize: 18)
        label.sizeToFit()
        return label
    }()
    
    private let statusInput: UITextField = {
        
        let textField = UITextField()
        textField.attributedPlaceholder = NSAttributedString(string: "Parking spot status",
                                                             attributes: [NSAttributedString.Key.foregroundColor: UIColor.lightGray])
        textField.font = UIFont.systemFont(ofSize: 16)
        textField.borderStyle = .none
        textField.textColor = AppColors.darkBlue
        
        textField.addTarget(self, action: #selector(AddDomainObjectView.userEditedText), for: .editingChanged)
        
        return textField
    }()
    
    private let powerLabel: UILabel = {
        let label = UILabel()
        label.text = "Power"
        label.textColor = AppColors.darkBlue
        label.font = UIFont.boldSystemFont(ofSize: 18)
        label.sizeToFit()
        return label
    }()
    
    private let powerInput: UITextField = {
        
        let textField = UITextField()
        textField.textContentType = .password
        textField.attributedPlaceholder = NSAttributedString(string: "Parking spot power",
                                                             attributes: [NSAttributedString.Key.foregroundColor: UIColor.lightGray])
        textField.font = UIFont.systemFont(ofSize: 16)
        textField.borderStyle = .none
        textField.textColor = AppColors.darkBlue
        textField.keyboardType = .numberPad
        
        textField.addTarget(self, action: #selector(AddDomainObjectView.userEditedText), for: .editingChanged)
        
        return textField
    }()
    
    private let addDomainObjectButton: ButtonWithActivity = {
        let button = ButtonWithActivity()
        button.setTitle("Add Parking Spot", for: .normal)
        button.setTitleColor(.white, for: .normal)
        button.backgroundColor = AppColors.darkBlue
        button.layer.cornerRadius = 8
        
        button.addTarget(self, action: #selector(AddDomainObjectView.didPressAddDomainObject), for: .touchUpInside)
        return button
    }()

    private let errorLabel: UILabel = {
        let label = UILabel(frame: CGRect.zero)
        label.textColor = AppColors.accentRed
        label.font = UIFont.boldSystemFont(ofSize: 16)
        label.contentMode = .center
        label.textAlignment = .center
        
        return label
    }()
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        var currentYOffset: CGFloat = 60
        let holder = UIView(frame: CGRect(x: 0, y: 0, width: frame.width, height: frame.height))
        holder.backgroundColor = .white
        
        
        pageTitleLabel.frame.origin.y = currentYOffset
        pageTitleLabel.center.x = frame.width / 2
        holder.addSubview(pageTitleLabel)
        currentYOffset += pageTitleLabel.frame.height + Constants.rowSpacing * 2
        
        
        nameLabel.frame.origin.x = Constants.leftMargin
        nameLabel.frame.origin.y = currentYOffset
        holder.addSubview(nameLabel)
        currentYOffset += nameLabel.frame.height + Constants.labelSpacing
        
        
        nameInput.frame = CGRect(x: Constants.leftMargin,
                                 y: currentYOffset,
                                 width: frame.width - 2 * Constants.leftMargin,
                                 height: 40)
        nameInput.delegate = self
        addUnderline(toTextField: nameInput)
        holder.addSubview(nameInput)
        currentYOffset += nameInput.frame.height + Constants.rowSpacing
        
        
        typeLabel.frame.origin.x = Constants.leftMargin
        typeLabel.frame.origin.y = currentYOffset
        holder.addSubview(typeLabel)
        currentYOffset += typeLabel.frame.height + Constants.labelSpacing
        
        typeInput.frame = CGRect(x: Constants.leftMargin,
                                  y: currentYOffset,
                                  width: frame.width - 2 * Constants.leftMargin,
                                  height: 40)
        typeInput.delegate = self
        addUnderline(toTextField: typeInput)
        holder.addSubview(typeInput)
        currentYOffset += typeInput.frame.height + Constants.rowSpacing
        
        statusLabel.frame.origin.x = Constants.leftMargin
        statusLabel.frame.origin.y = currentYOffset
        holder.addSubview(statusLabel)
        currentYOffset += statusLabel.frame.height + Constants.labelSpacing
        
        statusInput.frame = CGRect(x: Constants.leftMargin,
                                     y: currentYOffset,
                                     width: frame.width - 2 * Constants.leftMargin,
                                     height: 40)
        statusInput.delegate = self
        addUnderline(toTextField: statusInput)
        holder.addSubview(statusInput)
        currentYOffset += statusInput.frame.height + Constants.rowSpacing
        
        powerLabel.frame.origin.x = Constants.leftMargin
        powerLabel.frame.origin.y = currentYOffset
        holder.addSubview(powerLabel)
        currentYOffset += powerLabel.frame.height + Constants.labelSpacing
        
        powerInput.frame = CGRect(x: Constants.leftMargin,
                                  y: currentYOffset,
                                  width: frame.width - 2 * Constants.leftMargin,
                                  height: 40)
        powerInput.delegate = self
        addUnderline(toTextField: powerInput)
        holder.addSubview(powerInput)
        currentYOffset += powerInput.frame.height + 3 * Constants.rowSpacing
        
        errorLabel.frame = CGRect(x: 0,
                                  y: currentYOffset,
                                  width: frame.width,
                                  height: 40)
        holder.addSubview(errorLabel)
        errorLabel.alpha = 0
        
        addDomainObjectButton.frame = CGRect(x: Constants.leftMargin * 2,
                                    y: currentYOffset,
                                    width: frame.width - 4 * Constants.leftMargin,
                                    height: 40)
        holder.addSubview(addDomainObjectButton)
        currentYOffset += addDomainObjectButton.frame.height + Constants.rowSpacing / 2
        
        addSubview(holder)
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    // MARK: - Methods
    
    func showError(withText: String) {
        if !isShowingError {
            isShowingError = true
            self.errorLabel.text = withText
            UIView.animate(withDuration: 0.3) { [unowned self] in
                self.addDomainObjectButton.frame = self.addDomainObjectButton.frame.offsetBy(dx: 0, dy: 50)
                self.errorLabel.alpha = 1
            }
        }
    }
    
    func stopShowingError() {
        if isShowingError {
            isShowingError = false
            UIView.animate(withDuration: 0.3) { [unowned self] in
                self.addDomainObjectButton.frame = self.addDomainObjectButton.frame.offsetBy(dx: 0, dy: -50)
                self.errorLabel.alpha = 0
            }
        }
    }
    
    func setButtonLoading(isLoading loading: Bool) {
        loading ? addDomainObjectButton.showLoading() : addDomainObjectButton.hideLoading()
    }
    
    // MARK: - Private Methods
    
    @objc private func didPressAddDomainObject() {
        let name = nameInput.text!
        let type = typeInput.text!
        let status = statusInput.text!
        let power = powerInput.text!
        
        nameInput.resignFirstResponder()
        typeInput.resignFirstResponder()
        statusInput.resignFirstResponder()
        powerInput.resignFirstResponder()
        
        guard !name.isEmpty, !type.isEmpty, !status.isEmpty, !power.isEmpty else {
            showError(withText: "All fields needed")
            return
        }
        
        guard Int(power) != nil else {
            showError(withText: "Power is int")
            return
        }
        
        addDomainObjectButton.showLoading()
        
        delegate?.addDomainObjectViewDidRequestAdd(DomainObject(id: -1, name: name, type: type, status: status, power: Int(power)!))
    }
    
    @objc private func userEditedText() {
        self.stopShowingError()
    }
    
    private func addUnderline(toTextField textField: UITextField) {
        let border = CALayer()
        let width = CGFloat(1.0)
        border.borderColor = AppColors.darkBlue.cgColor
        border.frame = CGRect(x: 0, y: textField.frame.size.height - width, width: textField.frame.size.width, height: textField.frame.size.height)
        
        border.borderWidth = width
        textField.layer.addSublayer(border)
        textField.layer.masksToBounds = true
    }
}

extension AddDomainObjectView: UITextFieldDelegate {
    func textFieldShouldReturn(_ textField: UITextField) -> Bool {
        textField.resignFirstResponder()
        return true
    }
}
