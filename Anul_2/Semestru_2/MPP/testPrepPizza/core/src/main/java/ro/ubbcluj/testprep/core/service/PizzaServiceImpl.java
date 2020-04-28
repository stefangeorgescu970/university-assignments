package ro.ubbcluj.testprep.core.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ro.ubbcluj.testprep.core.model.Pizza;
import ro.ubbcluj.testprep.core.model.Validators.PizzaValidator;
import ro.ubbcluj.testprep.core.repository.PizzaRepository;
import org.springframework.validation.BindException;

import java.util.List;
import java.util.Optional;


@Service
public class PizzaServiceImpl implements PizzaServiceInterface {
    private static final Logger log = LoggerFactory.getLogger(PizzaServiceImpl.class);


    @Autowired
    private PizzaRepository pizzaRepository;

    @Autowired
    private PizzaValidator pizzaValidator;


    @Override
    public List<Pizza> getAllPizzas() {
        List<Pizza> pizzas = pizzaRepository.findAll();
        return pizzas;
    }

    @Override
    public void addPizza(Pizza pizza) {
        pizzaRepository.save(pizza);
    }

    @Override
    public Pizza createPizza(String name, String description, Float price) {
        Pizza pizza = Pizza
                .builder()
                .name(name)
                .description(description)
                .price(price)
                .build();
        BindException bindException = new BindException(pizza, "pizza");
        pizzaValidator.validate(pizza, bindException);
        if (bindException.hasErrors()) {
            throw new IllegalArgumentException("errors when validating new pizza");
        }
        return pizza;
    }

    @Override
    public Pizza findById(Long id) {
        Optional<Pizza> authorOptional = pizzaRepository.findById(id);
        if(authorOptional.isPresent()){
            return authorOptional.get();
        }
        throw new RuntimeException("Pizza with saught ID not there");
    }
}
