package ro.ubbcluj.testprep.core.repository;

import org.springframework.transaction.annotation.Transactional;
import ro.ubbcluj.testprep.core.model.Author;

@Transactional
public interface AuthorRepository extends MasterJPARepository<Author, Long>{

}
