package ro.ubbcluj.testprep.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import ro.ubbcluj.testprep.core.model.Author;
import ro.ubbcluj.testprep.core.model.Book;
import ro.ubbcluj.testprep.core.service.AuthorServiceInterface;
import ro.ubbcluj.testprep.core.service.BookServiceInterface;
import ro.ubbcluj.testprep.web.converter.BookConverter;
import ro.ubbcluj.testprep.web.dto.BookDTO;


import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

@RestController
public class BookController {
    private static final Logger log = LoggerFactory.getLogger(BookController.class);

    @Autowired
    private BookServiceInterface bookServiceInterface;

    @Autowired
    private AuthorServiceInterface authorServiceInterface;

    @Autowired
    private BookConverter bookConverter;

    @RequestMapping(value = "/books", method = RequestMethod.GET)
    public Set<BookDTO> getBooks(){
        log.trace("getBooks");

        List<Book> books = bookServiceInterface.getAllBooks();

        log.trace("getBooks: books = {}", books);

        return new HashSet<>(bookConverter.convertModelsToDTOS(books));
    }

    @RequestMapping(value = "/books/{authorId}", method = RequestMethod.GET)
    public Set<BookDTO> getBooksByAuthor(@PathVariable final Long authorId){
        log.trace("getBooksByAuthor with author id {}", authorId);

        List<Book> books = bookServiceInterface.getAllBooks();

        List<Book> filteredBooks = books.stream().filter(book -> book.getAuthor().getId().equals(authorId)).collect(Collectors.toList());

        log.trace("getBooks: books = {}", filteredBooks);

        return new HashSet<>(bookConverter.convertModelsToDTOS(filteredBooks));
    }

    @RequestMapping(value = "/books", method = RequestMethod.POST)
    public BookDTO createBook(@RequestBody final BookDTO bookDTO) {
        log.trace("createBook: bookDto = {}", bookDTO);

        Author author = authorServiceInterface.findById(bookDTO.getAuthor());

        Book book = bookServiceInterface.createBook(bookDTO.getIsbn(), bookDTO.getTitle(), bookDTO.getYear(), author);

        bookServiceInterface.addBook(book);

        BookDTO result = bookConverter.convertModelToDTO(book);

        log.trace("createBook: book = {}", book);

        return result;

    }

}
