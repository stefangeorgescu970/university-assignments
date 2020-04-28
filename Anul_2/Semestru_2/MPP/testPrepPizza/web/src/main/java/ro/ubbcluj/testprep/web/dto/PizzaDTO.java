package ro.ubbcluj.testprep.web.dto;

import lombok.*;

import java.util.Set;

@EqualsAndHashCode(callSuper = true)
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class PizzaDTO extends BaseDTO{

    private String name;
    private String description;
    private Float price;
    private Set<Long> ingredients;

}
