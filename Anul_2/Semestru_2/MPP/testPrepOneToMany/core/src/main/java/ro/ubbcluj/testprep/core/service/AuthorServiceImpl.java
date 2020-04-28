package ro.ubbcluj.testprep.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ro.ubbcluj.testprep.core.model.Author;
import ro.ubbcluj.testprep.core.model.Validators.AuthorValidator;
import ro.ubbcluj.testprep.core.repository.AuthorRepository;
import org.springframework.validation.BindException;
import java.util.HashSet;
import java.util.List;
import java.util.Optional;


@Service
public class AuthorServiceImpl implements AuthorServiceInterface {
    private static final Logger log = LoggerFactory.getLogger(AuthorServiceImpl.class);


    @Autowired
    private AuthorRepository authorRepository;

    @Autowired
    private AuthorValidator authorValidator;


    @Override
    public List<Author> getAllAuthors() {
        List<Author> authors = authorRepository.findAll();
        return authors;
    }

    @Override
    public void addAuthor(Author author) {
        authorRepository.save(author);
    }

    @Override
    public Author createAuthor(String name) {
        Author author = Author
                .builder()
                .name(name)
                .build();
        BindException bindException = new BindException(author, "author");
        authorValidator.validate(author, bindException);
        if (bindException.hasErrors()) {
            throw new IllegalArgumentException("errors when validating new author");
        }
        return author;
    }

    @Override
    public Author findById(Long id) {
        Optional<Author> authorOptional = authorRepository.findById(id);
        if(authorOptional.isPresent()){
            return authorOptional.get();
        }
        throw new RuntimeException("Author with saught ID not there");
    }
}
