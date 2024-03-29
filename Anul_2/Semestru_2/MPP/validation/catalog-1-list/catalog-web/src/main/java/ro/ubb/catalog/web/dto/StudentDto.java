package ro.ubb.catalog.web.dto;

import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import javax.validation.constraints.Min;

/**
 * Created by radu.
 */

@NoArgsConstructor
@AllArgsConstructor
@Getter
@Setter
public class StudentDto extends BaseDto {
    private String serialNumber;
    private String name;
    @Min(5)
    private Integer groupNumber;


    @Override
    public String toString() {
        return "StudentDto{" +
                "serialNumber='" + serialNumber + '\'' +
                ", name='" + name + '\'' +
                ", groupNumber=" + groupNumber +
                "} " + super.toString();
    }
}
