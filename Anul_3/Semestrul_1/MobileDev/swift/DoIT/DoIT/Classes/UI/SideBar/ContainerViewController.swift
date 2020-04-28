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
    
    var mainNavigationController: UINavigationController!
    var taskListViewController: TaskListTableViewController!
    var projectListViewController: ProjectListTableViewController!
    var sideBarViewController: SideBarViewController?
    
    var currentState: SlideOutState = .leftPanelCollapsed {
        didSet {
            let shouldShowShadow = currentState != .leftPanelCollapsed
            showShadowForCenterViewController(shouldShowShadow)
        }
    }
    
    let centerPanelExpandedOffset: CGFloat = 150
    
    override var preferredStatusBarStyle: UIStatusBarStyle {
        return .lightContent
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        projectListViewController = ProjectListTableViewController(frame: CGRect(x: 0, y: 0, width: self.view.bounds.width, height: self.view.bounds.height))
        taskListViewController = TaskListTableViewController(frame: CGRect(x: 0, y: 0, width: self.view.bounds.width, height: self.view.bounds.height))
        
        mainNavigationController = UINavigationController(rootViewController: taskListViewController)
        view.addSubview(mainNavigationController.view)
        addChild(mainNavigationController)
        mainNavigationController.didMove(toParent: self)
        
        mainNavigationController.navigationBar.barTintColor = AppColors.darkGray
        mainNavigationController.navigationBar.topItem?.leftBarButtonItem = UIBarButtonItem(title: "Menu", style: .plain, target: nil, action: #selector(self.didPressMenuButton))
        mainNavigationController.navigationBar.topItem?.leftBarButtonItem?.tintColor = AppColors.orange
        mainNavigationController.navigationBar.topItem?.leftBarButtonItem?.setTitleTextAttributes([NSAttributedString.Key.strokeColor : UIColor.orange], for: .normal)
        mainNavigationController.navigationBar.topItem?.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .add, target: nil, action: #selector(self.didRequestAddTask))
        mainNavigationController.navigationBar.topItem?.rightBarButtonItem?.tintColor = AppColors.orange
        
        
//        let panGestureRecognizer = UIPanGestureRecognizer(target: self, action: #selector(handlePanGesture(_:)))
//        mainNavigationController.view.addGestureRecognizer(panGestureRecognizer)
    }
    
    
    @objc func didPressMenuButton() {
        toggleLeftPanel()
    }
    
    
    @objc func didRequestAddTask() {
        let newController = AddNewTaskViewController(frame: self.view.frame)
        newController.delegate = taskListViewController
        mainNavigationController.pushViewController(newController, animated: true)
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
        
        let vc = SideBarViewController(frame: CGRect(x: 0, y: 0, width: view.frame.width - centerPanelExpandedOffset, height: view.frame.height))
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
        
        UIView.animate(withDuration: 0.5, delay: 0, usingSpringWithDamping: withDamping ? 10 : 10, initialSpringVelocity: 0, options: .curveEaseInOut, animations: {
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

//// MARK: Gesture recognizer
//
//extension ContainerViewController: UIGestureRecognizerDelegate {
//
//    @objc func handlePanGesture(_ recognizer: UIPanGestureRecognizer) {
//
//        let gestureIsDraggingFromLeftToRight = (recognizer.velocity(in: view).x > 0)
//
//        if gestureIsDraggingFromLeftToRight {
//
//            switch recognizer.state {
//
//            case .began:
//                if currentState == .leftPanelCollapsed {
//
//                    addLeftPanelViewController()
//
//                    showShadowForCenterViewController(true)
//                }
//
//            case .changed:
//                if let rview = recognizer.view {
//                    rview.center.x = rview.center.x + recognizer.translation(in: view).x
//                    recognizer.setTranslation(CGPoint.zero, in: view)
//                }
//
//            case .ended:
//                if let _ = sideBarViewController,
//                    let rview = recognizer.view {
//                    // animate the side panel open or closed based on whether the view has moved more or less than halfway
//                    let hasMovedGreaterThanHalfway = rview.center.x > view.bounds.size.width
//                    animateLeftPanel(shouldExpand: hasMovedGreaterThanHalfway)
//                }
//            default:
//                break
//            }
//
//        } else if currentState == .leftPanelExpanded {
//
//
//
//            switch recognizer.state {
//
//            case .began:
//                if currentState == .leftPanelExpanded {
//
//                    toggleLeftPanel()
//
//                    showShadowForCenterViewController(true)
//                }
//
//            case .changed:
//                if let rview = recognizer.view {
//
//                    let translation = recognizer.translation(in: view).x
//                    if rview.center.x + translation > rview.frame.width / 2 {
//
//                        rview.center.x = rview.center.x + recognizer.translation(in: view).x
//                        recognizer.setTranslation(CGPoint.zero, in: view)
//                    }
//
//                }
//
//            case .ended:
//                if let _ = sideBarViewController,
//                    let rview = recognizer.view {
//                    // animate the side panel open or closed based on whether the view has moved more or less than halfway
//                    let hasMovedGreaterThanHalfway = rview.center.x > view.bounds.size.width
//                    animateLeftPanel(shouldExpand: hasMovedGreaterThanHalfway)
//                }
//            default:
//                break
//            }
//
//        }
//    }
//}
//

extension ContainerViewController: SideBarViewControllerDelegate {
    func didSelectOption(_ option: String) {
        
        if option == "Tasks Due" {
            mainNavigationController.viewControllers = [taskListViewController]
            mainNavigationController.navigationBar.topItem?.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .add, target: nil, action: #selector(self.didRequestAddTask))
            taskListViewController.shouldDisplayCompletedTasks(false)
        } else if option == "Completed Tasks" {
            mainNavigationController.viewControllers = [taskListViewController]
            mainNavigationController.navigationBar.topItem?.rightBarButtonItem = nil
            taskListViewController.shouldDisplayCompletedTasks(true)
        } else if option == "Projects" {
            mainNavigationController.viewControllers = [projectListViewController]
            mainNavigationController.navigationBar.topItem?.leftBarButtonItem = UIBarButtonItem(title: "Menu", style: .plain, target: nil, action: #selector(self.didPressMenuButton))
            mainNavigationController.navigationBar.topItem?.leftBarButtonItem?.setTitleTextAttributes([NSAttributedString.Key.strokeColor : UIColor.orange], for: .normal)
            mainNavigationController.navigationBar.topItem?.rightBarButtonItem = UIBarButtonItem(barButtonSystemItem: .add, target: nil, action: #selector(self.didRequestAddProject))
        }
        
        self.collapseLeftPanel()
    }
    
    @objc func didRequestAddProject() {
        
        let alertController: UIAlertController = UIAlertController(title: "DoIT", message: "Name for new project", preferredStyle: .alert)
        //cancel button
        
        let cancelAction: UIAlertAction = UIAlertAction(title: "Cancel", style: .cancel, handler: nil)
        alertController.addAction(cancelAction)
        
        //Create an optional action
        
        let nextAction: UIAlertAction = UIAlertAction(title: "Add", style: .default) { (alertAction: UIAlertAction) in
            let text = alertController.textFields?.first!.text
            
            if let text = text {
                print("You entered \(text)")
                
                let project = Project(name: text)
                
                GlobalData.sharedInstance.getProjectService().saveProject(project){ [unowned self] (newId: String?) in
                    if let id = newId {
                        project.id = id
                        self.projectListViewController.updateForProject(project)
                    } else {
                        // display error
                    }
                }
            }
        }
        alertController.addAction(nextAction)
        
        //Add text field
        alertController.addTextField { (textField: UITextField) in
            textField.textColor = UIColor.black
        }
        
        //Present the AlertController
        present(alertController, animated: true, completion: nil)
    }
}
