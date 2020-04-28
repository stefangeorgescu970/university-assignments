package ro.ubb.exam.core.model;


import lombok.*;

import javax.persistence.Entity;
import javax.persistence.EnumType;
import javax.persistence.Enumerated;

@EqualsAndHashCode(callSuper = true)
@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
@Builder
public class Pizza extends BaseEntity<Long>{
    private String name;
    private String description;
    private float price;

    @Enumerated(EnumType.STRING)
    private Cuisine cuisine;
}
