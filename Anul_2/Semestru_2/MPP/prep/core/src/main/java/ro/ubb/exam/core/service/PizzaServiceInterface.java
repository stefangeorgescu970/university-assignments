package ro.ubb.exam.core.service;

import ro.ubb.exam.core.model.Cuisine;
import ro.ubb.exam.core.model.Pizza;

import java.util.List;

public interface PizzaServiceInterface {

    void addPizza(Pizza pizza);

    List<Pizza> getAllPizzas();

    List<Pizza> filterPizza(float price, String cuisine);

    Pizza createPizza(String name, String description, float price, Cuisine cuisine);
}
