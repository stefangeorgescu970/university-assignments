package ro.ubb.exam.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import ro.ubb.exam.core.model.Book;
import ro.ubb.exam.core.service.AuthorServiceInterface;
import ro.ubb.exam.core.service.BookServiceInterface;
import ro.ubb.exam.web.converter.BookConverter;
import ro.ubb.exam.web.converter.BookWithDataConverter;
import ro.ubb.exam.web.dto.BookDTO;
import ro.ubb.exam.web.dto.BookWithDataDTO;
import ro.ubb.exam.web.dto.FilterDTO;

import javax.jws.WebParam;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

@RestController
public class BookController {

    private static final Logger log = LoggerFactory.getLogger(AuthorController.class);

    @Autowired
    private BookServiceInterface bookServiceInterface;

    @Autowired
    private BookConverter bookConverter;

    @Autowired
    private BookWithDataConverter bookWithDataConverter;

//    @RequestMapping(value = "/books", method = RequestMethod.GET)
//    public Set<BookWithDataDTO> getBooks(){
//        log.trace("getBooks");
//
//        List<Book> books = bookServiceInterface.getAllBooks();
//
//        Set<BookWithDataDTO> result = new HashSet<>();
//
//        books.forEach(book -> result.add(bookWithDataConverter.convertModelToDTO(book, book.getAuthor())));
//
//        log.trace("getBooks: books = {}", result);
//
//        return result;
//    }

    @RequestMapping(value = "/books", method = RequestMethod.GET)
    public Set<BookWithDataDTO> getBooksByAuthorAndYear(@RequestParam(value = "authorId", defaultValue = "-1", required = false) Long authorId,
                                                        @RequestParam(value = "year", defaultValue = "-1", required = false) Integer year){
        log.trace("getBooksFiltered");

        List<Book> books;

        if(authorId != null && year != null){
            books = bookServiceInterface.findBooksByAuthorAndYear(authorId, year);
        } else {
            books = bookServiceInterface.getAllBooks();
        }

        HashSet<BookWithDataDTO> result = new HashSet<>();

        books.forEach(book -> result.add(bookWithDataConverter.convertModelToDTO(book, book.getAuthor())));

        log.trace("getBooksFiltered: books = {}", result);

        return result;
    }
}
