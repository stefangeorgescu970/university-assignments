package ro.ubb.exam.core.model;


import lombok.*;

import javax.persistence.*;
import java.util.HashSet;
import java.util.Set;

@Data
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode(callSuper = true)
@Entity
@Builder

@NamedEntityGraphs({
        @NamedEntityGraph(name = "authorWithBook", attributeNodes = @NamedAttributeNode(value = "books"))
})
public class Author extends Person{
    private String contact;

    @OneToMany(mappedBy = "author", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.LAZY)
    private Set<Book> books = new HashSet<>();
}
