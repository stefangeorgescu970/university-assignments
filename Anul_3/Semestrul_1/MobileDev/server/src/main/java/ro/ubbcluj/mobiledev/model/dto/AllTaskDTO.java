package ro.ubbcluj.mobiledev.model.dto;


import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;
import java.util.List;

@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class AllTaskDTO implements Serializable {
    private List<TaskDTO> tasks;
}
