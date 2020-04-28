//
//  MockProfileService.swift
//  DoIT
//
//  Created by Stefan Georgescu on 30/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation

class MockProfileService: ProfileService {
    func getCurrentUser() -> ProfileData {
        return ProfileData(name: "Stefan Georgescu", email: "stefan.georgescu.970@gmail.com")
    }
}
