//
//  ContainerViewController.swift
//  DoIT
//
//  Created by Georgescu Stefan on 25/10/2018.
//  Copyright © 2018 stefan. All rights reserved.
//

import UIKit


protocol RevealableViewController: class {
    func toggleLeftPanel()
    func collapseLeftPanel()
}

class ContainerViewController: UIViewController {
    enum SlideOutState {
        case leftPanelCollapsed
        case leftPanelExpanded
    }
    
    var currentState: SlideOutState = .leftPanelCollapsed {
        didSet {
            let shouldShowShadow = currentState != .leftPanelCollapsed
            showShadowForCenterViewController(shouldShowShadow)
        }
    }
    
    var mainNavigationController: UINavigationController!
    var sideBarViewController: SideBarViewController?
    var domainObjectListViewController: UIViewController!
    
    let centerPanelExpandedOffset: CGFloat = 150
    private let userRole: UserRole

    init(forUserRole: UserRole) {
        self.userRole = forUserRole
        super.init(nibName: nil, bundle: nil)
        
        self.view = UIView(frame: UIScreen.main.bounds)
        self.view.backgroundColor = AppColors.white
        
        switch userRole {
        case .clientUser:
            domainObjectListViewController = ClientDomainObjectListViewController()
        case .ownerUser:
            domainObjectListViewController = OwnerDomainObjectListViewController()
        }
        
        mainNavigationController = UINavigationController(rootViewController: domainObjectListViewController)
        view.addSubview(mainNavigationController.view)
        addChild(mainNavigationController)
        mainNavigationController.didMove(toParent: self)
        
        mainNavigationController.navigationBar.barTintColor = AppColors.darkBlue
        mainNavigationController.navigationBar.topItem?.leftBarButtonItem = UIBarButtonItem(title: "Menu", style: .plain, target: nil, action: #selector(self.didPressMenuButton))
        mainNavigationController.navigationBar.topItem?.leftBarButtonItem?.tintColor = AppColors.white
    }
    
    required init?(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    override var preferredStatusBarStyle: UIStatusBarStyle {
        return .lightContent
    }
    
    @objc func didPressMenuButton() {
        toggleLeftPanel()
    }
}

// MARK: TaskListTableViewController delegate
extension ContainerViewController: RevealableViewController {
    
    func toggleLeftPanel() {
        let notAlreadyExpanded = (currentState != .leftPanelExpanded)
        
        if notAlreadyExpanded {
            addLeftPanelViewController()
        }
        
        animateLeftPanel(shouldExpand: notAlreadyExpanded)
    }
    
    func collapseLeftPanel() {
        switch currentState {
        case .leftPanelExpanded:
            toggleLeftPanel()
        default:
            break
        }
    }

    func addLeftPanelViewController() {
        guard sideBarViewController == nil else { return }
        
        let vc = SideBarViewController(frame: CGRect(x: 0,
                                                     y: 0,
                                                     width: view.frame.width - centerPanelExpandedOffset,
                                                     height: view.frame.height),
                                       forUserRole: userRole)
        addChildSidePanelController(vc)
        sideBarViewController = vc
    }
    
    func addChildSidePanelController(_ sidePanelController: SideBarViewController) {
        sidePanelController.delegate = self
        view.insertSubview(sidePanelController.view, at: 0)
        
        addChild(sidePanelController)
        sidePanelController.didMove(toParent: self)
    }
    
    
    func animateLeftPanel(shouldExpand: Bool) {
        if shouldExpand {
            currentState = .leftPanelExpanded
            animateCenterPanelXPosition(targetPosition: mainNavigationController.view.frame.width - centerPanelExpandedOffset, withDamping: true)
            
        } else {
            animateCenterPanelXPosition(targetPosition: 0, withDamping: false) { _ in
                self.currentState = .leftPanelCollapsed
                self.sideBarViewController?.view.removeFromSuperview()
                self.sideBarViewController = nil
            }
        }
    }
    
    func animateCenterPanelXPosition(targetPosition: CGFloat, withDamping: Bool, completion: ((Bool) -> Void)? = nil) {
        UIView.animate(withDuration: 0.5,
                       delay: 0,
                       usingSpringWithDamping: 10,
                       initialSpringVelocity: 0,
                       options: .curveEaseInOut,
                       animations: {
            self.mainNavigationController.view.frame.origin.x = targetPosition
        }, completion: completion)
    }
    
    func showShadowForCenterViewController(_ shouldShowShadow: Bool) {
        if shouldShowShadow {
            mainNavigationController.view.layer.shadowOpacity = 0.8
        } else {
            mainNavigationController.view.layer.shadowOpacity = 0.0
        }
    }
}

extension ContainerViewController: SideBarViewControllerDelegate {
    func didSelectOption(_ option: String) {
        switch userRole {
        case .clientUser:
            if let option = ClientRoleOptions(rawValue: option) {
                switch option {
                case .viewSavedDomainObject:
                    mainNavigationController.viewControllers = [PersistedDomainObjectsListView()]
                    mainNavigationController.navigationBar.barTintColor = AppColors.darkBlue
                    mainNavigationController.navigationBar.topItem?.leftBarButtonItem = UIBarButtonItem(title: "Menu", style: .plain, target: nil, action: #selector(self.didPressMenuButton))
                    mainNavigationController.navigationBar.topItem?.leftBarButtonItem?.tintColor = AppColors.white
                case .viewPartOfDomainObject:
                    mainNavigationController.viewControllers = [domainObjectListViewController]
                    mainNavigationController.navigationBar.barTintColor = AppColors.darkBlue
                    mainNavigationController.navigationBar.topItem?.leftBarButtonItem = UIBarButtonItem(title: "Menu", style: .plain, target: nil, action: #selector(self.didPressMenuButton))
                    mainNavigationController.navigationBar.topItem?.leftBarButtonItem?.tintColor = AppColors.white
                case .goBack:
                    MainFlowManager.goBackToMain()
                }
            }
        case .ownerUser:
            if let option = OwnerRoleOptions(rawValue: option) {
                switch option {
                case .viewDomainObject:
                    mainNavigationController.viewControllers = [domainObjectListViewController]
                case .goBack:
                    MainFlowManager.goBackToMain()
                }
            }
        }
    
        self.collapseLeftPanel()
    }
}
