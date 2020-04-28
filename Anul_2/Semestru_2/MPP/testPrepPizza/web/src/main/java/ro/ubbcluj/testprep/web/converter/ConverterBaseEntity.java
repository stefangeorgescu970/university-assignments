package ro.ubbcluj.testprep.web.converter;

import ro.ubbcluj.testprep.core.model.BaseEntity;
import ro.ubbcluj.testprep.web.dto.BaseDTO;

public interface ConverterBaseEntity <Model extends BaseEntity<Long>, DTO extends BaseDTO>
        extends Converter<Model, DTO>{
}
