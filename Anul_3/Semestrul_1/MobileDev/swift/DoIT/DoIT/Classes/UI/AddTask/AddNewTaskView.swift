//
//  AddNewTaskView.swift
//  DoIT
//
//  Created by Georgescu Stefan on 26/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import UIKit

protocol AddNewTaskViewDelegate: class {
    func didRequestSelectProject()
}

class AddNewTaskView: UIView {

    var task: Task?
    var delegate: AddNewTaskViewDelegate?
    var selectedProject: Project? {
        didSet {
            if let selectedProject = selectedProject {
                chooseProjectButton.setTitle(selectedProject.name, for: .normal)
            }
        }
    }
    
    let nameLabel: UILabel = {
        let label = UILabel()
        label.textColor = AppColors.orange
        return label
    }()

    let nameTextField: UITextField = {
        let textField = UITextField()
        textField.attributedPlaceholder = NSAttributedString(string: "Enter name...",
                                                            attributes: [NSAttributedString.Key.foregroundColor: UIColor.white])
        textField.borderStyle = .none
        textField.textColor = .white
        return textField
    }()

    let dueDateLabel: UILabel = {
        let label = UILabel()
        label.textColor = AppColors.orange
        return label
    }()
    
    let selectedDueDateField: UITextField = {
        let textField = UITextField()
        textField.attributedPlaceholder = NSAttributedString(string: "Tap to select date...",
                                                            attributes: [NSAttributedString.Key.foregroundColor: UIColor.white])
        textField.textColor = .white
        return textField
    }()
    
    let dueDatePicker: UIDatePicker = {
        let picker = UIDatePicker()
        picker.datePickerMode = .date
        picker.sizeToFit()
        return picker
    }()

    let projectLabel: UILabel = {
        let label = UILabel()
        label.textColor = AppColors.orange
        return label
    }()

    let chooseProjectButton: UIButton = {
        let button = UIButton()
        button.setTitle("Choose Project", for: UIControl.State.normal)
        return button
    }()
    
    let descriptionLabel: UILabel = {
        let label = UILabel()
        label.textColor = AppColors.orange
        return label
    }()

    let descriptionTextField: UITextView = {
        let textField = UITextView()
        textField.textColor = .white
        textField.backgroundColor = AppColors.lightGray
        return textField
    }()

    
    init(frame: CGRect, task: Task? = nil) {
        super.init(frame: frame)
        let holder = UIView(frame: frame)
        holder.backgroundColor = AppColors.lightGray

        var currentOffsetY: CGFloat = 100
        var nameText = ""
        
        if let task = task {
            self.task = task
            nameText = task.name
            selectedProject = task.project
        }
        
        
        nameLabel.text = "Name"
        nameLabel.sizeToFit()
        nameLabel.frame = CGRect(x: 20, y: currentOffsetY, width: nameLabel.frame.width, height: nameLabel.frame.height)
        holder.addSubview(nameLabel)

        nameTextField.text = nameText
        nameTextField.frame = CGRect(x: 20 + nameLabel.frame.width + 15,
                                     y: currentOffsetY,
                                     width: frame.width - 2 * 20 - 15 - nameLabel.frame.width,
                                     height: nameLabel.frame.height)
        holder.addSubview(nameTextField)
        currentOffsetY += nameLabel.frame.height + 10
        
        
        dueDateLabel.text = "Date due"
        dueDateLabel.sizeToFit()
        dueDateLabel.frame = CGRect(x: 20, y: currentOffsetY, width: dueDateLabel.frame.width, height: dueDateLabel.frame.height)
        holder.addSubview(dueDateLabel)
        
        selectedDueDateField.sizeToFit()
        selectedDueDateField.delegate = self
        selectedDueDateField.text = task?.getDueDateFormatted()
        selectedDueDateField.frame = CGRect(x: 20 + 15 + dueDateLabel.frame.width,
                                            y: currentOffsetY,
                                            width: frame.width - 40 - 15 - selectedDueDateField.frame.width,
                                            height: selectedDueDateField.frame.height)
        holder.addSubview(selectedDueDateField)
        
        dueDatePicker.addTarget(self, action: #selector(AddNewTaskView.dateChanged(datePicker:)), for: .valueChanged)
        dueDatePicker.setDate(task?.dueDate ?? Date(), animated: false)
        selectedDueDateField.inputView = dueDatePicker
        
        currentOffsetY += selectedDueDateField.frame.height + 10
        
        projectLabel.text = "Project"
        projectLabel.sizeToFit()
        projectLabel.frame = CGRect(x: 20, y: currentOffsetY, width: projectLabel.frame.width, height: projectLabel.frame.height)
        holder.addSubview(projectLabel)
        
        if let selectedProject = selectedProject {
            chooseProjectButton.setTitle(selectedProject.name, for: .normal)
        }
        chooseProjectButton.titleLabel?.font = projectLabel.font
        chooseProjectButton.sizeToFit()
        chooseProjectButton.frame = CGRect(x: 20 + projectLabel.frame.width + 15,
                                           y: currentOffsetY,
                                           width: chooseProjectButton.frame.width,
                                           height: chooseProjectButton.frame.height)
        chooseProjectButton.addTarget(nil, action: #selector(didPressChooseProject), for: .touchUpInside)
        projectLabel.center.y = chooseProjectButton.center.y
        holder.addSubview(chooseProjectButton)
        
        currentOffsetY += chooseProjectButton.frame.height + 10
        
        descriptionLabel.text = "Description"
        descriptionLabel.sizeToFit()
        descriptionLabel.frame = CGRect(x: 20, y: currentOffsetY, width: descriptionLabel.frame.width, height: descriptionLabel.frame.height)
        holder.addSubview(descriptionLabel)
        
        currentOffsetY += descriptionLabel.frame.height + 5
        
        descriptionTextField.frame = CGRect(x: 20, y: currentOffsetY, width: holder.frame.width - 40, height: 100)
        descriptionTextField.text = task != nil ? (task?.description != nil ? task!.description : "Enter description for " + task!.name) : "Enter description ..."
        descriptionTextField.delegate = self
        holder.addSubview(descriptionTextField)
        
        addSubview(holder)
    }
    
    @objc func dateChanged(datePicker: UIDatePicker) {
        selectedDueDateField.text = DateUtils.getString(fromDate: datePicker.date, withYear: true)
    }
    
    @objc func didPressChooseProject() {
        self.delegate?.didRequestSelectProject()
    }
    
    func getNewTask() -> Task? {
        let description = descriptionTextField.text
        let name = nameTextField.text
        let dueDate = dueDatePicker.date
        
        guard let nameU = name, let project = selectedProject else {
            return nil
        }
        
        return Task(name: nameU, dueDate: dueDate, description: description == "Enter description ..." ? nil : description, project: project)
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}


extension AddNewTaskView: UITextViewDelegate {
    func textViewDidBeginEditing(_ textView: UITextView) {
        if textView.backgroundColor == AppColors.lightGray {
            if textView.text == "Enter description ..." {
                textView.text = nil
            }
            textView.backgroundColor = AppColors.darkGray
        }
    }
    
    func textViewDidEndEditing(_ textView: UITextView) {
        if textView.text.isEmpty {
            textView.text = "Enter description..."
            textView.backgroundColor = AppColors.lightGray
        }
    }
}

extension AddNewTaskView: UITextFieldDelegate {
    func textField(_ textField: UITextField, shouldChangeCharactersIn range: NSRange, replacementString string: String) -> Bool {
        if textField == selectedDueDateField {
            return false
        }
        return true
    }
}
