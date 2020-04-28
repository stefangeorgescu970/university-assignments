package ro.ubbcluj.testprep.web.converter;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.stereotype.Component;
import ro.ubbcluj.testprep.core.model.Pizza;
import ro.ubbcluj.testprep.core.model.BaseEntity;
import ro.ubbcluj.testprep.web.dto.PizzaDTO;

import java.util.stream.Collectors;

@Component
public class PizzaConverter extends AbstractConverterBaseEntity<Pizza, PizzaDTO>{
    private static final Logger log = LoggerFactory.getLogger(PizzaConverter.class);


    @Override
    public Pizza convertDTOToModel(PizzaDTO dto) {
        return Pizza.builder()
                .name(dto.getName())
                .description(dto.getDescription())
                .price(dto.getPrice())
                .build();
    }

    @Override
    public PizzaDTO convertModelToDTO(Pizza pizza) {
        PizzaDTO pizzaDTO =  PizzaDTO
                .builder()
                .name(pizza.getName())
                .description(pizza.getDescription())
                .price(pizza.getPrice())
                .ingredients(pizza.getIngredients().stream().map(BaseEntity::getId).collect(Collectors.toSet()))
                .build();
        pizzaDTO.setId(pizza.getId());
        return pizzaDTO;
    }
}
