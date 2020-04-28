package ro.ubbcluj.testprep.web.dto;

import lombok.*;

@EqualsAndHashCode(callSuper = true)
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class BookDTO extends BaseDTO {

    private String isbn;
    private String title;
    private Integer year;
    private Long author;
}
