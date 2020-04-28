package ro.ubb.exam.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ro.ubb.exam.core.model.Author;
import ro.ubb.exam.core.model.Book;
import ro.ubb.exam.core.repository.AuthorRepository;
import ro.ubb.exam.core.repository.BookRepository;

import java.util.List;

@Service
public class AuthorServiceImpl implements AuthorServiceInterface {
    private static final Logger log = LoggerFactory.getLogger(AuthorServiceImpl.class);

    @Autowired
    private AuthorRepository authorRepository;

    @Autowired
    private BookRepository bookRepository;


    @Override
    public List<Author> getAllAuthors() {
        List<Author> authors = authorRepository.findAllWithBooks();
        return authors;
        
    }
}
