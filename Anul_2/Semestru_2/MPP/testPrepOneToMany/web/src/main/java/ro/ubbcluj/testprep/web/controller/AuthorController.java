package ro.ubbcluj.testprep.web.controller;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import ro.ubbcluj.testprep.core.model.Author;
import ro.ubbcluj.testprep.core.service.AuthorServiceInterface;
import ro.ubbcluj.testprep.web.converter.AuthorConverter;
import ro.ubbcluj.testprep.web.dto.AuthorDTO;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

@RestController
public class AuthorController {

    private static final Logger log = LoggerFactory.getLogger(AuthorController.class);

    @Autowired
    private AuthorServiceInterface authorServiceInterface;

    @Autowired
    private AuthorConverter authorConverter;

    @RequestMapping(value = "/authors", method = RequestMethod.GET)
    public Set<AuthorDTO> getAuthors(){
        log.trace("getAuthors");

        List<Author> authors = authorServiceInterface.getAllAuthors();

        log.trace("getAuthors: authors = {}", authors);

        return new HashSet<>(authorConverter.convertModelsToDTOS(authors));
    }

    @RequestMapping(value = "/authors", method = RequestMethod.POST)
    public AuthorDTO createAuthor(@RequestBody final AuthorDTO authorDTO){
        log.trace("createAuthor: authorDTO = {}", authorDTO);

        Author author = authorServiceInterface.createAuthor(authorDTO.getName());

        authorServiceInterface.addAuthor(author);

        AuthorDTO result = authorConverter.convertModelToDTO(author);

        log.trace("createAuthor: author = {}", author);

        return result;
    }
}
