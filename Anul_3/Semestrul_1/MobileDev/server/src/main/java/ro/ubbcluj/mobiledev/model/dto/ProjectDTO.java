package ro.ubbcluj.mobiledev.model.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import ro.ubbcluj.mobiledev.model.Project;

import java.io.Serializable;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class ProjectDTO implements Serializable {
    private Integer id;
    private String name;

    public Project makeProject() {
        return Project.builder()
                .name(name)
                .build();
    }

    public ProjectDTO(Project project) {
        this.id = project.getId();
        this.name = project.getName();
    }
}
