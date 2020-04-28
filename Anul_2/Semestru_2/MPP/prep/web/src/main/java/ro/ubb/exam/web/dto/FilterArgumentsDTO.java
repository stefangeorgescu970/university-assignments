package ro.ubb.exam.web.dto;


import lombok.*;

@EqualsAndHashCode(callSuper = true)
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class FilterArgumentsDTO extends BaseDTO {
    private Boolean byPrice;
    private float price;
    private Boolean byCuisine;
    private String cuisine;
}
