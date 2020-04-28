package ro.ubb.exam.core.repository;

import org.springframework.transaction.annotation.Transactional;
import ro.ubb.exam.core.model.Pizza;

@Transactional
public interface PizzaRepository extends MasterJPARepository<Pizza, Long> {
}
