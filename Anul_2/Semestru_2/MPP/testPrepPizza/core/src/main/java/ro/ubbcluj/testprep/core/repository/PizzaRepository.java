package ro.ubbcluj.testprep.core.repository;

import org.springframework.transaction.annotation.Transactional;
import ro.ubbcluj.testprep.core.model.Pizza;

@Transactional
public interface PizzaRepository extends MasterJPARepository<Pizza, Long>{

}
