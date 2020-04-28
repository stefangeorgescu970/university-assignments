//
//  ProfileService.swift
//  DoIT
//
//  Created by Stefan Georgescu on 30/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation

protocol ProfileService {
    func getCurrentUser() -> ProfileData
}
