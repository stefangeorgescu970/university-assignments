package ro.ubbcluj.testprep.web.converter;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import ro.ubbcluj.testprep.core.model.Book;
import ro.ubbcluj.testprep.web.dto.BookDTO;

@Component
public class BookConverter extends AbstractConverterBaseEntity<Book, BookDTO> {
    private static final Logger log = LoggerFactory.getLogger(AuthorConverter.class);

    @Override
    public Book convertDTOToModel(BookDTO dto) {
        Book book =  Book
                .builder()
                .isbn(dto.getIsbn())
                .title(dto.getTitle())
                .year(dto.getYear())
                .build();
        book.setId(dto.getId());
        return book;
    }

    @Override
    public BookDTO convertModelToDTO(Book book) {
        BookDTO bookDTO = BookDTO
                .builder()
                .isbn(book.getIsbn())
                .title(book.getTitle())
                .year(book.getYear())
                .author(book.getAuthor().getId())
                .build();
        bookDTO.setId(book.getId());
        return bookDTO;
    }
}
