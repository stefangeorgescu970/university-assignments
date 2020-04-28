package ro.ubb.exam.web.converter;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import ro.ubb.exam.core.model.Book;
import ro.ubb.exam.web.dto.BookDTO;

@Component
public class BookConverter extends AbstractConverterBaseEntity<Book, BookDTO> {
    private static final Logger log = LoggerFactory.getLogger(AuthorConverter.class);

    @Override
    public Book convertDTOToModel(BookDTO dto) {
        Book book =  Book
                .builder()
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
                .title(book.getTitle())
                .year(book.getYear())
                .author(book.getAuthor().getId())
                .build();
        bookDTO.setId(book.getId());
        return bookDTO;
    }
}
