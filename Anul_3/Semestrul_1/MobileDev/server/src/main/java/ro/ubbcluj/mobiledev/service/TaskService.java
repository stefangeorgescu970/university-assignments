package ro.ubbcluj.mobiledev.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ro.ubbcluj.mobiledev.model.Project;
import ro.ubbcluj.mobiledev.model.Task;
import ro.ubbcluj.mobiledev.model.dto.AllTaskDTO;
import ro.ubbcluj.mobiledev.model.dto.TaskDTO;
import ro.ubbcluj.mobiledev.repository.ProjectRepository;
import ro.ubbcluj.mobiledev.repository.TaskRepository;

import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

@Service
public class TaskService {

    @Autowired
    private TaskRepository taskRepository;

    @Autowired
    private ProjectRepository projectRepository;

    public Integer addTask(Task newTask, int projectId) {
        System.out.println("Adding task");
        Project p = projectRepository.findById(projectId).get();
        p.getTasks().add(newTask);
        newTask.setProject(p);
        projectRepository.save(p);
        Task saved = taskRepository.save(newTask);
        return saved.getId();
    }

    public Boolean updateTask(TaskDTO newTask) {
        Task task = taskRepository.getOne(newTask.getId());

        if (task != null) {
            task.setName(newTask.getName());
            task.setDescription(newTask.getDescription());

            if (!task.getProject().getId().equals(newTask.getProject().getId())) {
                task.setProject(projectRepository.getOne(newTask.getProject().getId()));
                Project oldProject = projectRepository.getOne(task.getProject().getId());
                Project newProject = projectRepository.getOne(newTask.getProject().getId());
                oldProject.getTasks().remove(task);
                newProject.getTasks().add(task);
                projectRepository.save(oldProject);
                projectRepository.save(newProject);
            }

            task.setIsCompleted(newTask.getIsCompleted());
            if (newTask.getCompletionDate() != null) {
                task.setCompletionDate(newTask.getCompletionDate());
            }
            taskRepository.save(task);
            return true;
        } else {
            return false;
        }
    }

    public Boolean deleteTask(Integer taskId) {
        Optional<Task> taskOptional = taskRepository.findById(taskId);

        if (taskOptional.isPresent()) {
            taskRepository.delete(taskOptional.get());
            return true;
        } else {
            return false;
        }
    }

    public AllTaskDTO getAll() {
        List<Task> tasks = taskRepository.findAll();

        return AllTaskDTO.builder().tasks(tasks.stream().map(TaskDTO::new).collect(Collectors.toList())).build();
    }

    public void initialSetup() {

        taskRepository.deleteAll();

        projectRepository.deleteAll();


        Project p1 = Project.builder().name("University").tasks(new ArrayList<>()).build();
        Project p2 = Project.builder().name("Work").tasks(new ArrayList<>()).build();
        Project p3 = Project.builder().name("Personal").tasks(new ArrayList<>()).build();

        projectRepository.save(p1);
        projectRepository.save(p2);
        projectRepository.save(p3);

        List<Project> projects = projectRepository.findAll();

        Date dueDate = new Date(2018, 12, 1);
        Date completedDate = new Date();
        Date oldDueDate = new Date(2018, 10, 12);

        Task t1 = Task.builder().name("Task 1").dueDate(dueDate).description("One task").isCompleted(false).project(projects.get(0)).build();
        projects.get(0).getTasks().add(t1);
        Task t2 = Task.builder().name("Task 2").dueDate(dueDate).description("Two task").isCompleted(false).project(projects.get(0)).build();
        projects.get(0).getTasks().add(t2);
        Task t3 = Task.builder().name("Task 3").dueDate(dueDate).description("Three task").isCompleted(false).project(projects.get(1)).build();
        projects.get(1).getTasks().add(t3);
        Task t4 = Task.builder().name("Task 4").dueDate(dueDate).description("Four task").isCompleted(false).project(projects.get(1)).build();
        projects.get(1).getTasks().add(t4);
        Task t5 = Task.builder().name("Task 5").dueDate(dueDate).description("Five task").isCompleted(false).project(projects.get(2)).build();
        projects.get(2).getTasks().add(t5);

        Task t6 = Task.builder().name("Completed Task 1").dueDate(oldDueDate).description("Six task").isCompleted(true).completionDate(completedDate).project(projects.get(0)).build();
        projects.get(0).getTasks().add(t6);

        Task t7 = Task.builder().name("Completed Task 2").dueDate(oldDueDate).description("Seven task").isCompleted(true).completionDate(completedDate).project(projects.get(1)).build();
        projects.get(1).getTasks().add(t7);

        taskRepository.save(t1);
        taskRepository.save(t2);
        taskRepository.save(t3);
        taskRepository.save(t4);
        taskRepository.save(t5);
        taskRepository.save(t6);
        taskRepository.save(t7);
    }

}
