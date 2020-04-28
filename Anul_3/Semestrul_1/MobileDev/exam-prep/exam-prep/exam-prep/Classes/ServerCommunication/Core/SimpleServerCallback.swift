//
//  SimpleServerCallback.swift
//  EasyHelp
//
//  Created by Georgescu Stefan on 16/09/2018.
//  Copyright © 2018 EasyHelp. All rights reserved.
//

import Foundation

typealias SimpleServerCallbackBlock = (AnyObject?) -> ()

class SimpleServerCallback {
    var successBlocks = [SimpleServerCallbackBlock]()
    var errorBlocks = [SimpleServerCallbackBlock]()
    
    var state: AnyObject?
    
    init(successBlock: @escaping SimpleServerCallbackBlock, errorBlock: @escaping SimpleServerCallbackBlock) {
        self.errorBlocks.append(errorBlock)
        self.successBlocks.append(successBlock)
    }
    
    func addBlocks(successBlock: @escaping SimpleServerCallbackBlock, errorBlock: @escaping SimpleServerCallbackBlock) {
        self.errorBlocks.append(errorBlock)
        self.successBlocks.append(successBlock)
    }
    
    func onSuccess(_ data: Any!) {
        for block in successBlocks {
            if data != nil {
                block(data as AnyObject)
            } else {
                block(nil)
            }
        }
    }
    
    func onError(_ data: Any!) {
        for block in errorBlocks {
            if data != nil {
                block(data as AnyObject)
            } else {
                block(nil)
            }
        }
    }
}
