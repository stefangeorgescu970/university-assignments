package ro.ubbcluj.testprep.core.model.Validators;

import org.springframework.lang.Nullable;
import org.springframework.stereotype.Component;
import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;
import org.springframework.validation.Validator;
import ro.ubbcluj.testprep.core.model.Pizza;

@Component
public class PizzaValidator implements Validator {
    @Override
    public boolean supports(Class<?> clazz) {
        return Pizza.class.equals(clazz);
    }

    @Override
    public void validate(@Nullable Object target, Errors errors) {
        Pizza pizza = (Pizza) target;
        ValidationUtils.rejectIfEmpty(errors, "name", "name is empty");
        ValidationUtils.rejectIfEmpty(errors, "description", "description is empty");
        if (pizza.getPrice() <= 0) {
            errors.rejectValue("price", "price is negative");
        }
    }
}
