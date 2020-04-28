package ro.ubb.exam.core.service;

import ro.ubb.exam.core.model.Book;

import java.util.List;

public interface BookServiceInterface {

    List<Book> findBooksByAuthorAndYear(Long authorId, Integer year);

    List<Book> getAllBooks();
}
