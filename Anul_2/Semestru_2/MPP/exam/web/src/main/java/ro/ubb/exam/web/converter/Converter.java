package ro.ubb.exam.web.converter;


import ro.ubb.exam.web.dto.BaseDTO;

public interface Converter<Model, DTO extends BaseDTO> {

    Model convertDTOToModel(DTO dto);

    DTO convertModelToDTO(Model model);

}
