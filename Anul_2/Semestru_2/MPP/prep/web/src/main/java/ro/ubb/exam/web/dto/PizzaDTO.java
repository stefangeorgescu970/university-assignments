package ro.ubb.exam.web.dto;


import lombok.*;

@EqualsAndHashCode(callSuper = true)
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class PizzaDTO extends BaseDTO{
    private String name;
    private String description;
    private float price;
    private String cuisine;
}
