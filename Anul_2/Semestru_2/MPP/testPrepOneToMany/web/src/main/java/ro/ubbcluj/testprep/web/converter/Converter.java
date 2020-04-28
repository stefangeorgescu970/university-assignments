package ro.ubbcluj.testprep.web.converter;

import ro.ubbcluj.testprep.web.dto.BaseDTO;

public interface Converter<Model, DTO extends BaseDTO> {

    Model convertDTOToModel(DTO dto);

    DTO convertModelToDTO(Model model);

}
