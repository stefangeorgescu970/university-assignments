package ro.ubb.exam.core.repository;

import org.springframework.data.jpa.repository.EntityGraph;
import org.springframework.data.jpa.repository.Query;
import org.springframework.transaction.annotation.Transactional;
import ro.ubb.exam.core.model.Author;
import ro.ubb.exam.core.model.Book;

import java.util.List;

@Transactional
public interface AuthorRepository extends MasterJPARepository<Author, Long> {

    @Query("select distinct a from Author a")
    @EntityGraph(value = "authorWithBook", type = EntityGraph.EntityGraphType.LOAD)
    List<Author> findAllWithBooks();
}
