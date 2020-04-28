//
//  GlobalData.swift
//  DoIT
//
//  Created by Georgescu Stefan on 24/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation

class GlobalData {
    
    static let sharedInstance = GlobalData()
    private init() {}
    
    private var taskService: TaskService!
    private var projectService: ProjectService!
    private var profileService: ProfileService!
    private var offlineTaskService: MockTaskService = MockTaskService()
    private var offlineProjectService: MockProjectService = MockProjectService()
    
    func setTaskService(_ taskService: TaskService) {
        self.taskService = taskService
    }
    
    func getTaskService() -> TaskService {
        return taskService
    }
    
    func setProjectService(_ projectService: ProjectService) {
        self.projectService = projectService
    }
    
    func getProjectService() -> ProjectService {
        return projectService
    }
    
    func setProfileService(_ profileService: ProfileService) {
        self.profileService = profileService
    }
    
    func getProfileService() -> ProfileService {
        return profileService
    }
    
    func getLocalTaskStorage() -> MockTaskService {
        return offlineTaskService
    }
    
    func getLocalProjectStorage() -> MockProjectService {
        return offlineProjectService
    }
}
