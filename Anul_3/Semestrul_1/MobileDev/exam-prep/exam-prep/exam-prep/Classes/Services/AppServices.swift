//
//  AppServices.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation

class AppServices {
    static var domainObjectService: DomainObjectService {
        return DomainObjectService()
    }
    
    static var persistantDomainObjectService: PersistantDomainObjectService {
        return PersistantDomainObjectService()
    }
}
