package ro.ubbcluj.testprep.web.dto;

import lombok.*;

import java.util.Set;

@EqualsAndHashCode(callSuper = true)
@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class AuthorDTO extends BaseDTO{

    private String name;
    private Set<Long> books;

}
