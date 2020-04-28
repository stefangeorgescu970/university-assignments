package ro.ubbcluj.mobiledev.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ro.ubbcluj.mobiledev.service.ProjectService;
import ro.ubbcluj.mobiledev.service.TaskService;

@RestController
@RequestMapping("/misc")
public class MiscController {

    @Autowired
    private ProjectService projectService;

    @Autowired
    private TaskService taskService;

    @PostMapping(path = "/populateDb")
    public ResponseEntity<Boolean> addProject() {

        taskService.initialSetup();

        return new ResponseEntity<Boolean>(HttpStatus.OK);
    }


}
