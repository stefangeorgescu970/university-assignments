package ro.ubb.exam.web.config;

import org.springframework.context.annotation.*;
import org.springframework.context.support.PropertySourcesPlaceholderConfigurer;
import ro.ubb.exam.core.config.JPAConfig;

@Configuration
@ComponentScan({"ro.ubb.exam.core"})
@Import({JPAConfig.class})
@PropertySources({@PropertySource(value = "file:/Users/Stefan/Desktop/prep/web/src/main/resources/local/db.properties"),
})
public class AppLocalConfig {
    /**
     * Enables placeholders usage with SpEL expressions.
     *
     * @return
     */
    @Bean
    public static PropertySourcesPlaceholderConfigurer propertySourcesPlaceholderConfigurer() {
        return new PropertySourcesPlaceholderConfigurer();
    }
}