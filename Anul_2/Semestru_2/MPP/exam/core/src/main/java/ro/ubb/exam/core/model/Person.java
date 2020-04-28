package ro.ubb.exam.core.model;


import lombok.*;

import javax.persistence.Entity;
import javax.persistence.MappedSuperclass;

@Entity
@Data
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode(callSuper = true)
public class Person extends BaseEntity<Long>{

    protected String ssn;
    protected String name;

}
