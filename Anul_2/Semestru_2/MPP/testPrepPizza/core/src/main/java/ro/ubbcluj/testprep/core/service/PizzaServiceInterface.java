package ro.ubbcluj.testprep.core.service;

import ro.ubbcluj.testprep.core.model.Pizza;

import java.util.List;

public interface PizzaServiceInterface {

    List<Pizza> getAllPizzas();

    void addPizza(Pizza pizza);

    Pizza createPizza(String name, String description, Float price);

    Pizza findById(Long id);
}
