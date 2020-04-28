package ro.ubbcluj.mobiledev.controller;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import ro.ubbcluj.mobiledev.model.dto.TaskDTO;
import ro.ubbcluj.mobiledev.service.TaskService;
import ro.ubbcluj.mobiledev.utils.response.Response;
import ro.ubbcluj.mobiledev.utils.response.ResponseBuilder;

@RestController
@RequestMapping("/task")
public class TaskController {

    @Autowired
    private TaskService taskService;

    @PostMapping(path = "/add")
    public ResponseEntity<Response> addTask(@RequestBody @DateTimeFormat(pattern = "yyyy-mm-dd") TaskDTO newTaskDTO) {
        return ResponseBuilder.encode(HttpStatus.OK, taskService.addTask(newTaskDTO.makeTask(), newTaskDTO.getProjectId()));
    }

    @PostMapping(path = "/get")
    public ResponseEntity<Response> getAll() {
        return ResponseBuilder.encode(HttpStatus.OK, taskService.getAll());
    }

    @PostMapping(path = "/delete/{taskId}")
    public ResponseEntity<Response> deleteTask(@PathVariable Integer taskId) {
        return ResponseBuilder.encode(HttpStatus.OK, taskService.deleteTask(taskId));
    }

    @PostMapping(path = "/update")
    public ResponseEntity<Response> updateTask(@RequestBody TaskDTO taskDTO) {
        return ResponseBuilder.encode(HttpStatus.OK, taskService.updateTask(taskDTO));
    }

}
