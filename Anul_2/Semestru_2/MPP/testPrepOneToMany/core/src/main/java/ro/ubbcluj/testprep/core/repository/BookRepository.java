package ro.ubbcluj.testprep.core.repository;

import org.springframework.transaction.annotation.Transactional;
import ro.ubbcluj.testprep.core.model.Book;

@Transactional
public interface BookRepository extends MasterJPARepository<Book, Long>{

}
