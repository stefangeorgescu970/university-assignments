package ro.ubb.exam.web.converter;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import ro.ubb.exam.core.model.Author;
import ro.ubb.exam.core.model.BaseEntity;
import ro.ubb.exam.web.dto.AuthorDTO;

import java.util.stream.Collectors;

@Component
public class AuthorConverter extends AbstractConverterBaseEntity<Author, AuthorDTO>{
    private static final Logger log = LoggerFactory.getLogger(AuthorConverter.class);


    @Override
    public Author convertDTOToModel(AuthorDTO dto) {
        Author author =  Author.builder()
                .contact(dto.getContact())
                .build();
        author.setName(dto.getName());
        author.setSsn(dto.getSsn());
        return author;
    }

    @Override
    public AuthorDTO convertModelToDTO(Author author) {
        AuthorDTO authorDTO =  AuthorDTO
                .builder()
                .name(author.getName())
                .contact(author.getContact())
                .ssn(author.getSsn())
                .build();
        authorDTO.setId(author.getId());
        return authorDTO;
    }
}

