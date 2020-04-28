package ro.ubb.exam.web.converter;

import ro.ubb.exam.web.dto.BaseDTO;

import java.util.Collection;
import java.util.stream.Collectors;

public abstract class AbstractConverter <Model, DTO extends BaseDTO>
        implements Converter<Model, DTO> {

    public Collection<DTO> convertModelsToDTOS(Collection<Model> models){
        return models
                .stream()
                .map(this::convertModelToDTO)
                .collect(Collectors.toSet());
    }

    public Collection<Model> convertDTOSToModels(Collection<DTO> dtos){
        return dtos
                .stream()
                .map(this::convertDTOToModel)
                .collect(Collectors.toSet());
    }
}
