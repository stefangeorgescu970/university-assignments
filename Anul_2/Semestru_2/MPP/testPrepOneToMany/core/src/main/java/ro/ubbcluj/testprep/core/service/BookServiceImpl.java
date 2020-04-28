package ro.ubbcluj.testprep.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ro.ubbcluj.testprep.core.model.Author;
import ro.ubbcluj.testprep.core.model.Book;
import ro.ubbcluj.testprep.core.model.Validators.BookValidator;
import ro.ubbcluj.testprep.core.repository.BookRepository;
import org.springframework.validation.BindException;

import java.util.List;
import java.util.Optional;

@Service
public class BookServiceImpl implements BookServiceInterface {

    private static final Logger log = LoggerFactory.getLogger(BookServiceImpl.class);

    @Autowired
    private BookRepository bookRepository;

    @Autowired
    private BookValidator bookValidator;

    @Override
    public List<Book> getAllBooks() {
        return bookRepository.findAll();
    }

    @Override
    public void addBook(Book book) {
        bookRepository.save(book);
    }

    @Override
    public Book createBook(String isbn, String title, Integer year, Author author) {
        Book book = Book
                .builder()
                .isbn(isbn)
                .title(title)
                .year(year)
                .author(author)
                .build();
        BindException bindException = new BindException(book, "book");
        bookValidator.validate(book, bindException);
        if (bindException.hasErrors()) {
            throw new IllegalArgumentException("errors when validating new book");
        }
        return book;
    }

    @Override
    public Book findById(Long id) {
        Optional<Book> bookOptional = bookRepository.findById(id);
        if(bookOptional.isPresent()){
            return bookOptional.get();
        }
        throw new RuntimeException("Book with saught ID not there");
    }
}
