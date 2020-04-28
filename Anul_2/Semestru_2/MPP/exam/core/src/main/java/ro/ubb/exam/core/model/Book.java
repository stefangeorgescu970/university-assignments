package ro.ubb.exam.core.model;


import lombok.*;

import javax.persistence.*;

@Data
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode(callSuper = true, exclude = {"author"})
@Entity
@Builder
@ToString(exclude = {"author"})

@NamedEntityGraphs({
        @NamedEntityGraph(name = "bookWithAuthor", attributeNodes = @NamedAttributeNode(value = "author"))
})

public class Book extends BaseEntity<Long>{
    private String title;
    private Integer year;

    @ManyToOne(optional = false, fetch = FetchType.LAZY)
    private Author author;

}
