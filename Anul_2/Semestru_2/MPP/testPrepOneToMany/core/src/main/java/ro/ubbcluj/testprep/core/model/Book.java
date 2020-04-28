package ro.ubbcluj.testprep.core.model;

import lombok.*;

import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.ManyToOne;


@EqualsAndHashCode(callSuper = true)
@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
@ToString(exclude = {"author"})
public class Book extends BaseEntity<Long> {

    private String isbn;
    private String title;
    private Integer year;

    @ManyToOne(optional = false, fetch = FetchType.EAGER)
    private Author author;

}
