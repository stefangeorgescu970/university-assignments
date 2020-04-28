package ro.ubbcluj.testprep.core.repository;

import org.springframework.transaction.annotation.Transactional;
import ro.ubbcluj.testprep.core.model.Ingredient;

@Transactional
public interface IngredientRepository extends MasterJPARepository<Ingredient, Long>{

}
