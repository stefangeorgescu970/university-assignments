package ro.ubb.exam.core.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.validation.BindException;
import org.springframework.validation.annotation.Validated;
import ro.ubb.exam.core.model.Cuisine;
import ro.ubb.exam.core.model.Pizza;
import ro.ubb.exam.core.model.Validators.PizzaValidator;
import ro.ubb.exam.core.repository.PizzaRepository;

import java.util.List;

@Service
@Validated
public class PizzaServiceImpl implements PizzaServiceInterface {

    @Autowired
    private PizzaRepository pizzaRepository;

    @Autowired
    private PizzaValidator pizzaValidator;

    @Override
    public void addPizza(Pizza pizza) {
        pizzaRepository.save(pizza);
    }

    @Override
    public List<Pizza> getAllPizzas() {
        return pizzaRepository.findAll();
    }

    @Override
    public List<Pizza> filterPizza(float price, String cuisine) {
        return this.getAllPizzas(); // TODO - implement
    }

    @Override
    public Pizza createPizza(String name, String description, float price, Cuisine cuisine) {
        Pizza pizza = Pizza
                .builder()
                .name(name)
                .description(description)
                .price(price)
                .cuisine(cuisine)
                .build();

        BindException bindException = new BindException(pizza, "pizza");
        pizzaValidator.validate(pizza, bindException);
        if (bindException.hasErrors()) {
            throw new IllegalArgumentException("errors when validating pizza");
        }
        return pizza;
    }
}
