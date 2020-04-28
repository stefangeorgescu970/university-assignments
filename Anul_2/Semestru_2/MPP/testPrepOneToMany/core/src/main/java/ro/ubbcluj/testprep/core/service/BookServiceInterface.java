package ro.ubbcluj.testprep.core.service;

import ro.ubbcluj.testprep.core.model.Author;
import ro.ubbcluj.testprep.core.model.Book;

import java.util.List;

public interface BookServiceInterface {

    List<Book> getAllBooks();

    void addBook(Book book);

    Book createBook(String isbn, String title, Integer year, Author author);

    Book findById(Long id);
}
