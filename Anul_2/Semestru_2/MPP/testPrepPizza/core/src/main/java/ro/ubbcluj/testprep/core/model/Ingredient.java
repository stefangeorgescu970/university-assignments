package ro.ubbcluj.testprep.core.model;

import lombok.*;

import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.ManyToOne;


@EqualsAndHashCode(callSuper = true)
@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
@ToString(exclude = {"pizza"})
public class Ingredient extends BaseEntity<Long> {

    private String name;

    @ManyToOne(optional = false, fetch = FetchType.EAGER)
    private Pizza pizza;

}
