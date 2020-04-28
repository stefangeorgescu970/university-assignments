//
//  TaskListTableViewCell.swift
//  DoIT
//
//  Created by Georgescu Stefan on 25/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import UIKit

class TaskListTableViewCell: UITableViewCell {
    
    var taskNameLabel: UILabel = {
        let label = UILabel()
        label.textColor = .white
        label.font = label.font.withSize(18)
        return label
    }()
    
    var dueDateLabel: UILabel = {
        let label = UILabel()
        label.textColor = AppColors.orange
        return label
    }()
    var projectNameLabel: UILabel = {
        let label = UILabel()
        label.textColor = AppColors.orange
        return label
    }()
    
    var separator: UIView = {
        let separator = UIView()
        separator.backgroundColor = .black
        return separator
    }()
    
    
    func syncView(task: Task) {
        self.backgroundColor = AppColors.lightGray
        
        taskNameLabel.text = task.name
        taskNameLabel.sizeToFit()
        taskNameLabel.frame = CGRect(x: 20, y: (frame.height - taskNameLabel.frame.height) / 3, width: taskNameLabel.frame.width, height: taskNameLabel.frame.height)
        addSubview(taskNameLabel)
        
        dueDateLabel.text = DateUtils.getString(fromDate: task.dueDate)
        dueDateLabel.sizeToFit()
        dueDateLabel.frame = CGRect(x: 20, y: frame.height * 2 / 3, width: dueDateLabel.frame.width, height: dueDateLabel.frame.height)
        addSubview(dueDateLabel)
        
    
        projectNameLabel.text = task.project.name
        projectNameLabel.sizeToFit()
        projectNameLabel.frame = CGRect(x: frame.width - 20 - projectNameLabel.frame.width, y: frame.height * 2 / 3, width: projectNameLabel.frame.width, height: projectNameLabel.frame.height)
        addSubview(projectNameLabel)
        
        separator.frame = CGRect(x: 0, y: self.frame.height - 0.7, width: self.frame.width, height: 0.7)
        addSubview(separator)
    }
    
}
