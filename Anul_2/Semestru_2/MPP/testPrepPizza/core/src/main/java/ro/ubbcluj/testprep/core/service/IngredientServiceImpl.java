package ro.ubbcluj.testprep.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ro.ubbcluj.testprep.core.model.Ingredient;
import ro.ubbcluj.testprep.core.model.Pizza;
import ro.ubbcluj.testprep.core.model.Validators.IngredientValidator;
import ro.ubbcluj.testprep.core.repository.IngredientRepository;
import org.springframework.validation.BindException;

import java.util.List;
import java.util.Optional;

@Service
public class IngredientServiceImpl implements IngredientServiceInterface {

    private static final Logger log = LoggerFactory.getLogger(IngredientServiceImpl.class);

    @Autowired
    private IngredientRepository ingredientRepository;

    @Autowired
    private IngredientValidator ingredientValidator;

    @Override
    public List<Ingredient> getAllIngredients() {
        return ingredientRepository.findAll();
    }

    @Override
    public void addIngredient(Ingredient ingredient) {
        ingredientRepository.save(ingredient);
    }

    @Override
    public Ingredient createIngredient(String name, Pizza pizza) {
        Ingredient ingredient = Ingredient
                .builder()
                .name(name)
                .pizza(pizza)
                .build();
        BindException bindException = new BindException(ingredient, "ingredient");
        ingredientValidator.validate(ingredient, bindException);
        if (bindException.hasErrors()) {
            throw new IllegalArgumentException("errors when validating new ingredient");
        }
        return ingredient;
    }

    @Override
    public Ingredient findById(Long id) {
        Optional<Ingredient> bookOptional = ingredientRepository.findById(id);
        if(bookOptional.isPresent()){
            return bookOptional.get();
        }
        throw new RuntimeException("Ingredient with sought ID not there");
    }
}
