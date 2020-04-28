package ro.ubbcluj.testprep.web.controller;


import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import ro.ubbcluj.testprep.core.model.Pizza;
import ro.ubbcluj.testprep.core.service.PizzaServiceInterface;
import ro.ubbcluj.testprep.web.converter.PizzaConverter;
import ro.ubbcluj.testprep.web.dto.PizzaDTO;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

@RestController
public class PizzaController {

    private static final Logger log = LoggerFactory.getLogger(PizzaController.class);

    @Autowired
    private PizzaServiceInterface pizzaServiceInterface;

    @Autowired
    private PizzaConverter pizzaConverter;

    @RequestMapping(value = "/pizzas", method = RequestMethod.GET)
    public Set<PizzaDTO> getAuthors(){
        log.trace("getAuthors");

        List<Pizza> pizzas = pizzaServiceInterface.getAllPizzas();

        log.trace("getAuthors: pizzas = {}", pizzas);

        return new HashSet<>(pizzaConverter.convertModelsToDTOS(pizzas));
    }

    @RequestMapping(value = "/pizzas", method = RequestMethod.POST)
    public PizzaDTO createAuthor(@RequestBody final PizzaDTO pizzaDTO){
        log.trace("createAuthor: pizzaDTO = {}", pizzaDTO);

        Pizza pizza = pizzaServiceInterface.createPizza(pizzaDTO.getName(), pizzaDTO.getDescription(), pizzaDTO.getPrice());

        pizzaServiceInterface.addPizza(pizza);

        PizzaDTO result = pizzaConverter.convertModelToDTO(pizza);

        log.trace("createAuthor: pizza = {}", pizza);

        return result;
    }
}
