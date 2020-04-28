package ro.ubbcluj.testprep.web.converter;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import ro.ubbcluj.testprep.core.model.Ingredient;
import ro.ubbcluj.testprep.web.dto.IngredientDTO;

@Component
public class IngredientConverter extends AbstractConverterBaseEntity<Ingredient, IngredientDTO> {
    private static final Logger log = LoggerFactory.getLogger(PizzaConverter.class);

    @Override
    public Ingredient convertDTOToModel(IngredientDTO dto) {
        Ingredient ingredient =  Ingredient
                .builder()
                .name(dto.getName())
                .build();
        ingredient.setId(dto.getId());
        return ingredient;
    }

    @Override
    public IngredientDTO convertModelToDTO(Ingredient ingredient) {
        IngredientDTO ingredientDTO = IngredientDTO
                .builder()
                .name(ingredient.getName())
                .pizza(ingredient.getPizza().getId())
                .build();
        ingredientDTO.setId(ingredient.getId());
        return ingredientDTO;
    }
}
