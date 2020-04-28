//
//  TaskDetailsView.swift
//  DoIT
//
//  Created by Georgescu Stefan on 26/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import UIKit

protocol TaskDetailsViewDelegate: class {
    func deleteTask(_ task: Task)
    func completeTask(_ task: Task)
}

class TaskDetailsView: UIView {
    
    var task: Task
    var delegate: TaskDetailsViewDelegate?
    
    let nameLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.boldSystemFont(ofSize: 16)
        label.textColor = AppColors.orange
        return label
    }()
    
    let nameText: UILabel = {
        let label = UILabel()
        label.textColor = .white
        return label
    }()
    
    let dueDateLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.boldSystemFont(ofSize: 16)
        label.textColor = AppColors.orange
        return label
    }()
    
    let actualDueDateLabel: UILabel = {
        let label = UILabel()
        label.textColor = .white
        return label
    }()
    
    let projectLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.boldSystemFont(ofSize: 16)
        label.textColor = AppColors.orange
        return label
    }()
    
    let actualProjectLabel: UILabel = {
        let label = UILabel()
        label.textColor = .white
        return label
    }()
    
    let descriptionLabel: UILabel = {
        let label = UILabel()
        label.font = UIFont.boldSystemFont(ofSize: 16)
        label.textColor = AppColors.orange
        return label
    }()
    
    let descriptionTextField: UITextView = {
        let textField = UITextView()
        textField.isEditable = false
        textField.backgroundColor = .clear
        textField.textColor = .white
        return textField
    }()
    
    let completeButton: UIButton = {
        let button = UIButton()
        button.setTitle("Complete", for: .normal)
        button.backgroundColor = AppColors.orange
        button.layer.cornerRadius = 5
        return button
    }()
    
    let deleteButton: UIButton = {
        let button = UIButton()
        button.setTitle("Delete", for: .normal)
        button.backgroundColor = AppColors.darkGray
        button.layer.cornerRadius = 5
        return button
    }()

    private func addSeparator(view: UIView, yOffset: CGFloat) {
        let sep = UIView(frame: CGRect(x: 20, y: yOffset, width: view.frame.width - 40, height: 0.5))
        sep.backgroundColor = AppColors.darkGray
        view.addSubview(sep)
    }
    
    init(frame: CGRect, task: Task){
        self.task = task
        super.init(frame: frame)
        
        let holder = UIView(frame: frame)
        holder.backgroundColor = AppColors.lightGray
        
        var currentOffsetY: CGFloat = 100
        
        nameLabel.text = "Name"
        nameLabel.sizeToFit()
        nameLabel.frame = CGRect(x: 20, y: currentOffsetY, width: nameLabel.frame.width, height: nameLabel.frame.height)
        holder.addSubview(nameLabel)
        
        nameText.text = task.name
        nameText.sizeToFit()
        nameText.frame = CGRect(x: holder.frame.width - 20 - nameText.frame.width,
                                y: currentOffsetY,
                                width: frame.width - 2 * 20 - 15 - nameLabel.frame.width,
                                height: nameLabel.frame.height)
        holder.addSubview(nameText)
        
        currentOffsetY += nameLabel.frame.height + 20
        addSeparator(view: holder, yOffset: currentOffsetY - 15)
        
        dueDateLabel.text = "Date due"
        dueDateLabel.sizeToFit()
        dueDateLabel.frame = CGRect(x: 20, y: currentOffsetY, width: dueDateLabel.frame.width, height: dueDateLabel.frame.height)
        holder.addSubview(dueDateLabel)
    
        actualDueDateLabel.text = DateUtils.getString(fromDate: task.dueDate)
        actualDueDateLabel.sizeToFit()
        actualDueDateLabel.frame = CGRect(x: holder.frame.width - 20 - actualDueDateLabel.frame.width,
                                          y: currentOffsetY,
                                          width: frame.width - 2 * 20 - 15 - dueDateLabel.frame.width ,
                                          height: actualDueDateLabel.frame.height)
        holder.addSubview(actualDueDateLabel)
        
        currentOffsetY += actualDueDateLabel.frame.height + 20
        addSeparator(view: holder, yOffset: currentOffsetY - 15)
        
        projectLabel.text = "Project"
        projectLabel.sizeToFit()
        projectLabel.frame = CGRect(x: 20, y: currentOffsetY, width: projectLabel.frame.width, height: projectLabel.frame.height)
        holder.addSubview(projectLabel)
 
        actualProjectLabel.text = task.project.name
        actualProjectLabel.sizeToFit()
        actualProjectLabel.frame = CGRect(x: holder.frame.width - 20 - actualProjectLabel.frame.width,
                                          y: currentOffsetY,
                                          width: actualProjectLabel.frame.width,
                                          height: actualProjectLabel.frame.height)
        holder.addSubview(actualProjectLabel)
        
        currentOffsetY += actualProjectLabel.frame.height + 20
        addSeparator(view: holder, yOffset: currentOffsetY - 15)
        
        descriptionLabel.text = "Description"
        descriptionLabel.sizeToFit()
        descriptionLabel.frame = CGRect(x: 20, y: currentOffsetY, width: descriptionLabel.frame.width, height: descriptionLabel.frame.height)
        holder.addSubview(descriptionLabel)
        currentOffsetY += descriptionLabel.frame.height + 5
        
        descriptionTextField.text = task.description ?? "No description."
        descriptionTextField.frame = CGRect(x: 20, y: currentOffsetY, width: holder.frame.width - 40, height: 100)
        holder.addSubview(descriptionTextField)
        currentOffsetY += descriptionTextField.frame.height + 10
        
        if !task.isCompleted {
            completeButton.frame = CGRect(x: (holder.frame.width - 200) / 2,
                                          y: currentOffsetY,
                                          width: 200,
                                          height: 40)
            completeButton.addTarget(self, action: #selector(didComplete), for: .touchUpInside)
            holder.addSubview(completeButton)
            currentOffsetY += completeButton.frame.height + 10
            
            deleteButton.frame = CGRect(x: (holder.frame.width - 200) / 2,
                                        y: currentOffsetY,
                                        width: 200,
                                        height: 40)
            deleteButton.addTarget(self, action: #selector(didDelete), for: .touchUpInside)
            holder.addSubview(deleteButton)
        }

        addSubview(holder)
    }
    
    func syncView() {
        nameText.text = task.name
        actualDueDateLabel.text = task.getDueDateFormatted()
        actualProjectLabel.text = task.project.name
        descriptionTextField.text = task.description
    }
    
    @objc func didComplete() {
        delegate?.completeTask(task)
    }
    
    @objc func didDelete() {
        delegate?.deleteTask(task)
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
