package ro.ubb.exam.core.service;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ro.ubb.exam.core.model.Book;
import ro.ubb.exam.core.repository.BookRepository;

import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

@Service
public class BookServiceImpl implements BookServiceInterface{
    private static final Logger log = LoggerFactory.getLogger(AuthorServiceImpl.class);

    @Autowired
    private BookRepository bookRepository;

    @Override
    public List<Book> findBooksByAuthorAndYear(Long authorId, Integer year) {
        List<Book> intermediaryResult, finalResult;
        List<Book> books = bookRepository.findAllWithAuthors();

        if(authorId != -1) {
            intermediaryResult = books.stream()
                    .filter(book -> book.getAuthor().getId().equals(authorId))
                    .collect(Collectors.toList());
        } else {
            intermediaryResult = books;
        }

        if(year != -1) {
            finalResult = intermediaryResult.stream()
                    .filter(book -> book.getYear().equals(year))
                    .collect(Collectors.toList());
        } else {
            finalResult = intermediaryResult;
        }

        return finalResult;
    }


    @Override
    public List<Book> getAllBooks() {
        return bookRepository.findAllWithAuthors();
    }

}
