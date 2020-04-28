package ro.ubb.exam.web.dto;

import lombok.*;

@EqualsAndHashCode(callSuper = true)
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class BookWithDataDTO extends BaseDTO{
    private String title;
    private Integer year;
    private String ssn;
    private String name;
    private String contact;
    private Long author;
}
