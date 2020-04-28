package ro.ubb.exam.web.converter;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import ro.ubb.exam.core.model.Author;
import ro.ubb.exam.core.model.Book;
import ro.ubb.exam.web.dto.BookDTO;
import ro.ubb.exam.web.dto.BookWithDataDTO;

import java.util.Set;

@Component
public class BookWithDataConverter {
    private static final Logger log = LoggerFactory.getLogger(AuthorConverter.class);


    public BookWithDataDTO convertModelToDTO(Book book, Author author) {
        BookWithDataDTO bookWithDataDTO = BookWithDataDTO
                .builder()
                .title(book.getTitle())
                .year(book.getYear())
                .author(book.getAuthor().getId())
                .ssn(author.getSsn())
                .contact(author.getContact())
                .name(author.getName())
                .build();
        return bookWithDataDTO;
    }
}


