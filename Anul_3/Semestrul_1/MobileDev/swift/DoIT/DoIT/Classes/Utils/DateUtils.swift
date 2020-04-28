//
//  DateUtils.swift
//  DoIT
//
//  Created by Stefan Georgescu on 31/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import Foundation

class DateUtils {
    
    private static var dateFormatterPrint: DateFormatter = {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "MMM dd"
        return dateFormatter
    }()
    
    private static var dateFormatterPrintYear: DateFormatter = {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "MMM dd, yyyy"
        return dateFormatter
    }()
    
    private static var serverDateFormatter: DateFormatter = {
        let dateFormatter = DateFormatter()
        dateFormatter.dateFormat = "yyyy-mm-dd"
        return dateFormatter
    }()
    
    static func getString(fromDate date: Date, withYear: Bool = false) -> String {
        return withYear ? dateFormatterPrintYear.string(from: date) : dateFormatterPrint.string(from:date)
    }
    
    static func getDateFromServer(fromString: String) -> Date? {
        return serverDateFormatter.date(from: fromString)
    }
    
    static func getDateStringForServer(fromDate: Date) -> String {
        return serverDateFormatter.string(from:fromDate)
    }
}
