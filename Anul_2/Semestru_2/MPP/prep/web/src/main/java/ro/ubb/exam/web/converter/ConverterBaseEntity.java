package ro.ubb.exam.web.converter;

import ro.ubb.exam.core.model.BaseEntity;
import ro.ubb.exam.web.dto.BaseDTO;

public interface ConverterBaseEntity <Model extends BaseEntity<Long>, DTO extends BaseDTO>
        extends Converter<Model, DTO>{
}
