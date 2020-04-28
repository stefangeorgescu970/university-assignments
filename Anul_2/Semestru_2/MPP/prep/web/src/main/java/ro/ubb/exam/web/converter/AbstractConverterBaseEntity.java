package ro.ubb.exam.web.converter;

import ro.ubb.exam.core.model.BaseEntity;
import ro.ubb.exam.web.dto.BaseDTO;

import java.util.Set;
import java.util.stream.Collectors;

public abstract class AbstractConverterBaseEntity<Model extends BaseEntity<Long>, Dto extends BaseDTO>
        extends AbstractConverter<Model, Dto> implements ConverterBaseEntity<Model, Dto> {

    public Set<Long> convertModelsToIDs(Set<Model> models) {
        return models.stream()
                .map(BaseEntity::getId)
                .collect(Collectors.toSet());
    }

    public Set<Long> convertDTOsToIDs(Set<Dto> dtos) {
        return dtos.stream()
                .map(BaseDTO::getId)
                .collect(Collectors.toSet());
    }

}
