package ro.ubbcluj.mobiledev.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import ro.ubbcluj.mobiledev.model.dto.ProjectDTO;
import ro.ubbcluj.mobiledev.service.ProjectService;
import ro.ubbcluj.mobiledev.utils.response.Response;
import ro.ubbcluj.mobiledev.utils.response.ResponseBuilder;

@RestController
@RequestMapping("/project")
public class ProjectController {
    @Autowired
    private ProjectService projectService;


    @PostMapping(path = "/add")
    public ResponseEntity<Response> addProject(@RequestBody ProjectDTO projectDTO) {
        return ResponseBuilder.encode(HttpStatus.OK, projectService.addProject(projectDTO.makeProject()));
    }

    @PostMapping(path = "/get")
    public ResponseEntity<Response> getAll() {
        return ResponseBuilder.encode(HttpStatus.OK, projectService.getAll());
    }

}
