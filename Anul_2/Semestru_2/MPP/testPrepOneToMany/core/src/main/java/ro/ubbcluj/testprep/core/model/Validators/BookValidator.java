package ro.ubbcluj.testprep.core.model.Validators;

import org.springframework.lang.Nullable;
import org.springframework.stereotype.Component;
import org.springframework.validation.Errors;
import org.springframework.validation.ValidationUtils;
import org.springframework.validation.Validator;
import ro.ubbcluj.testprep.core.model.Book;

@Component
public class BookValidator implements Validator {
    @Override
    public boolean supports(Class<?> clazz) {
        return Book.class.equals(clazz);
    }

    @Override
    public void validate(@Nullable Object target, Errors errors) {
        Book book = (Book) target;
        ValidationUtils.rejectIfEmpty(errors, "isbn", "isbn is empty");
        ValidationUtils.rejectIfEmpty(errors, "title", "title is empty");
        ValidationUtils.rejectIfEmpty(errors, "year", "year is empty");
        if(book.getYear() > 2018 && book.getYear() < 0) {
            errors.rejectValue("year", "year value not good");
        }
    }
}
