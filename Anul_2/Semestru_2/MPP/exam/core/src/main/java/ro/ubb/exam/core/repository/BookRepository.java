package ro.ubb.exam.core.repository;

import org.springframework.data.jpa.repository.EntityGraph;
import org.springframework.data.jpa.repository.Query;
import ro.ubb.exam.core.model.Book;

import java.util.List;


public interface BookRepository extends MasterJPARepository<Book, Long>{

    @Query("select distinct b from Book b")
    @EntityGraph(value = "bookWithAuthor", type = EntityGraph.EntityGraphType.LOAD)
    List<Book> findAllWithAuthors();
}
