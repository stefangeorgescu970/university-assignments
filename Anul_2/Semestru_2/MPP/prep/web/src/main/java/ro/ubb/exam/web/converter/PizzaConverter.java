package ro.ubb.exam.web.converter;

import org.springframework.stereotype.Component;
import ro.ubb.exam.core.model.Cuisine;
import ro.ubb.exam.core.model.Pizza;
import ro.ubb.exam.web.dto.PizzaDTO;

@Component
public class PizzaConverter extends AbstractConverterBaseEntity<Pizza, PizzaDTO> {
    @Override
    public Pizza convertDTOToModel(PizzaDTO dto) {
        Pizza pizza = Pizza
                .builder()
                .name(dto.getName())
                .description(dto.getDescription())
                .price(dto.getPrice())
                .cuisine(Cuisine.valueOf(dto.getCuisine()))
                .build();
        pizza.setId(dto.getId());
        return pizza;
    }

    @Override
    public PizzaDTO convertModelToDTO(Pizza pizza) {
        PizzaDTO pizzaDTO = PizzaDTO
                .builder()
                .name(pizza.getName())
                .description(pizza.getDescription())
                .price(pizza.getPrice())
                .cuisine(pizza.getCuisine().name())
                .build();
        pizzaDTO.setId(pizza.getId());
        return pizzaDTO;
    }
}
