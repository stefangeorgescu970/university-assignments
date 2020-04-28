//
//  DomainObjectUtils.swift
//  exam-prep
//
//  Created by Stefan Georgescu on 26/01/2019.
//  Copyright © 2019 Stefan Georgescu. All rights reserved.
//

import Foundation

class DomainObjectUtils {
    static func orderDomainObjects(_ domainObjects: [DomainObject]) -> [DomainObject] {
        return domainObjects.sorted(by: {
            if $0.status == $1.status {
                return $0.power > $1.power
            }
            return $0.status > $1.status
        })
    }
}
