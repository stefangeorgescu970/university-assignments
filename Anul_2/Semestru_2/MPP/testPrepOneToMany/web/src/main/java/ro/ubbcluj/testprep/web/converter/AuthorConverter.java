package ro.ubbcluj.testprep.web.converter;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import ro.ubbcluj.testprep.core.model.Author;
import ro.ubbcluj.testprep.core.model.BaseEntity;
import ro.ubbcluj.testprep.web.dto.AuthorDTO;

import java.util.stream.Collectors;

@Component
public class AuthorConverter extends AbstractConverterBaseEntity<Author, AuthorDTO>{
    private static final Logger log = LoggerFactory.getLogger(AuthorConverter.class);


    @Override
    public Author convertDTOToModel(AuthorDTO dto) {
        return Author.builder()
                .name(dto.getName())
                .build();
    }

    @Override
    public AuthorDTO convertModelToDTO(Author author) {
        AuthorDTO authorDTO =  AuthorDTO
                .builder()
                .name(author.getName())
                .books(author.getBooks().stream().map(BaseEntity::getId).collect(Collectors.toSet()))
                .build();
        authorDTO.setId(author.getId());
        return authorDTO;
    }
}
