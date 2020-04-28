package ro.ubb.exam.web.dto;

import lombok.*;

@EqualsAndHashCode(callSuper = true)
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class BookDTO extends BaseDTO {
    private String title;
    private Integer year;
    private Long author;
}