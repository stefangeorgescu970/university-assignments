package ro.ubbcluj.testprep.core.service;

import ro.ubbcluj.testprep.core.model.Ingredient;
import ro.ubbcluj.testprep.core.model.Pizza;

import java.util.List;

public interface IngredientServiceInterface {

    List<Ingredient> getAllIngredients();

    void addIngredient(Ingredient ingredient);

    Ingredient createIngredient(String name, Pizza pizza);

    Ingredient findById(Long id);
}
