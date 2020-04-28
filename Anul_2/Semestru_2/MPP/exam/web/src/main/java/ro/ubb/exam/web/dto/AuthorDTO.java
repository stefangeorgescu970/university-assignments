package ro.ubb.exam.web.dto;

import lombok.*;

import java.util.Set;

@EqualsAndHashCode(callSuper = true)
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class AuthorDTO extends BaseDTO{

    private String ssn;
    private String name;
    private String contact;

}
