package ro.ubbcluj.testprep.core.model;


import lombok.*;

import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.OneToMany;
import java.util.HashSet;
import java.util.Set;


@EqualsAndHashCode(exclude = {"ingredients"}, callSuper = true)
@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
@ToString(exclude = {"ingredients"})
public class Pizza extends BaseEntity<Long> {

    private String name;
    private String description;
    private Float price;

    @OneToMany(mappedBy = "pizza", cascade = CascadeType.ALL, orphanRemoval = true, fetch = FetchType.EAGER)
    private Set<Ingredient> ingredients = new HashSet<>();
}