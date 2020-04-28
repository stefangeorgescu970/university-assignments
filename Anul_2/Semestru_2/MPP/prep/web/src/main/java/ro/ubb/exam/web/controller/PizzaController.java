package ro.ubb.exam.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;
import ro.ubb.exam.core.model.Cuisine;
import ro.ubb.exam.core.model.Pizza;
import ro.ubb.exam.core.service.PizzaServiceInterface;
import ro.ubb.exam.web.converter.PizzaConverter;
import ro.ubb.exam.web.dto.FilterArgumentsDTO;
import ro.ubb.exam.web.dto.PizzaDTO;

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


    @RequestMapping(value = "/pizzas", method = RequestMethod.POST)
    public PizzaDTO createPizza(@RequestBody final PizzaDTO pizzaDTO){
        log.trace("createPizza: pizzaDTO = {}", pizzaDTO);

        Pizza pizza = pizzaServiceInterface.createPizza(pizzaDTO.getName(), pizzaDTO.getDescription(),
                pizzaDTO.getPrice(), Cuisine.valueOf(pizzaDTO.getCuisine()));

        pizzaServiceInterface.addPizza(pizza);

        PizzaDTO result = pizzaConverter.convertModelToDTO(pizza);

        log.trace("createPizza: pizza = {}", pizza);

        return result;
    }

    @RequestMapping(value = "pizzas/filter", method = RequestMethod.POST)
    public Set<PizzaDTO> getFilteredPizzas(@RequestBody final FilterArgumentsDTO fadto) {
        log.trace("filterPizzas: filterDTO = {}", fadto);


        List<Pizza> pizzas;

        if(fadto.getByPrice() && fadto.getByCuisine()) {
            pizzas = pizzaServiceInterface.filterPizza(fadto.getPrice(), fadto.getCuisine());
        }
        else if(fadto.getByCuisine()){
            pizzas = pizzaServiceInterface.filterPizza(-1, fadto.getCuisine());
        } else if(fadto.getByPrice()) {
            pizzas = pizzaServiceInterface.filterPizza(fadto.getPrice(), "");
        } else {
            pizzas = this.pizzaServiceInterface.getAllPizzas();
        }

        log.trace("filterPizzas: pizza = {}", pizzas);

        return new HashSet<>(pizzaConverter.convertModelsToDTOS(pizzas));
    }

}
