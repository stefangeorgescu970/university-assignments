package ro.ubbcluj.testprep.core.model.Validators;

import org.springframework.lang.Nullable;
import org.springframework.stereotype.Component;
import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;
import org.springframework.validation.Validator;
import ro.ubbcluj.testprep.core.model.Ingredient;

@Component
public class IngredientValidator implements Validator {
    @Override
    public boolean supports(Class<?> clazz) {
        return Ingredient.class.equals(clazz);
    }

    @Override
    public void validate(@Nullable Object target, Errors errors) {
        Ingredient ingredient = (Ingredient) target;
        ValidationUtils.rejectIfEmpty(errors, "name", "name is empty");
    }
}
