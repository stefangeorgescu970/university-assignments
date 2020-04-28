package ro.ubbcluj.mobiledev.model;


import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import ro.ubbcluj.mobiledev.model.dto.TaskDTO;

import javax.persistence.*;
import java.util.Date;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Task {

    @Id
    @GeneratedValue
    private Integer id;

    private String name;
    private Date dueDate;
    private String description;
    private Boolean isCompleted;
    private Date completionDate;

    @ManyToOne
    @JoinColumn(name = "projectId")
    private Project project;
}
