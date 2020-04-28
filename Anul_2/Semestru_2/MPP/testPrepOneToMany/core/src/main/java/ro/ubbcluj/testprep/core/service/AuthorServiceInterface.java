package ro.ubbcluj.testprep.core.service;

import ro.ubbcluj.testprep.core.model.Author;

import java.util.List;

public interface AuthorServiceInterface {

    List<Author> getAllAuthors();

    void addAuthor(Author author);

    Author createAuthor(String name);

    Author findById(Long id);
}
