package ro.ubbcluj.mobiledev.model.dto;

import com.fasterxml.jackson.annotation.JsonFormat;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import ro.ubbcluj.mobiledev.model.Task;

import java.io.Serializable;
import java.util.Date;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class TaskDTO implements Serializable {

    private String name;
    private String description;
    private Integer id;
    @JsonFormat(pattern = "yyyy-mm-dd")
    private Date dueDate;
    private ProjectDTO project;
    private Boolean isCompleted;
    @JsonFormat(pattern = "yyyy-mm-dd")
    private Date completionDate;
    private Integer projectId;

    public TaskDTO(Task task) {
        this.id = task.getId();
        this.name = task.getName();
        this.description = task.getDescription();
        this.dueDate = task.getDueDate();
        this.completionDate = task.getCompletionDate();
        this.isCompleted = task.getIsCompleted();
        this.project = new ProjectDTO(task.getProject());
    }

    public Task makeTask() {
        return Task.builder()
                .name(name)
                .description(description)
                .dueDate(dueDate)
                .isCompleted(false)
                .build();
    }
}
