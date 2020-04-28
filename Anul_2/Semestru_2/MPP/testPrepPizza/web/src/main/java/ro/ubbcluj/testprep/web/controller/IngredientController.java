package ro.ubbcluj.testprep.web.controller;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import ro.ubbcluj.testprep.core.model.Ingredient;
import ro.ubbcluj.testprep.core.model.Pizza;
import ro.ubbcluj.testprep.core.service.PizzaServiceInterface;
import ro.ubbcluj.testprep.core.service.IngredientServiceInterface;
import ro.ubbcluj.testprep.web.converter.IngredientConverter;
import ro.ubbcluj.testprep.web.dto.IngredientDTO;


import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;

@RestController
public class IngredientController {
    private static final Logger log = LoggerFactory.getLogger(IngredientController.class);

    @Autowired
    private IngredientServiceInterface ingredientServiceInterface;

    @Autowired
    private PizzaServiceInterface pizzaServiceInterface;

    @Autowired
    private IngredientConverter ingredientConverter;

    @RequestMapping(value = "/ingredients", method = RequestMethod.GET)
    public Set<IngredientDTO> getBooks(){
        log.trace("getIngredients");

        List<Ingredient> ingredients = ingredientServiceInterface.getAllIngredients();

        log.trace("getIngredients: ingredients = {}", ingredients);

        return new HashSet<>(ingredientConverter.convertModelsToDTOS(ingredients));
    }


    @RequestMapping(value = "/ingredients", method = RequestMethod.POST)
    public IngredientDTO createBook(@RequestBody final IngredientDTO ingredientDTO) {
        log.trace("createBook: bookDto = {}", ingredientDTO);

        Pizza pizza = pizzaServiceInterface.findById(ingredientDTO.getPizza());

        Ingredient ingredient = ingredientServiceInterface.createIngredient(ingredientDTO.getName(), pizza);

        ingredientServiceInterface.addIngredient(ingredient);

        IngredientDTO result = ingredientConverter.convertModelToDTO(ingredient);

        log.trace("createBook: ingredient = {}", ingredient);

        return result;

    }

}
