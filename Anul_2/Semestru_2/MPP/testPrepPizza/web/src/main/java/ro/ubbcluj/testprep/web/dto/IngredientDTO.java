package ro.ubbcluj.testprep.web.dto;

import lombok.*;

@EqualsAndHashCode(callSuper = true)
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class IngredientDTO extends BaseDTO {

    private String name;
    private Long pizza;
}
