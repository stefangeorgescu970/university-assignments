package ro.ubb.remoting.client.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.remoting.rmi.RmiProxyFactoryBean;
import ro.ubb.remoting.client.service.StudentServiceClient;
import ro.ubb.remoting.common.StudentService;

@Configuration
public class ClientConfig {
    @Bean
    StudentService studentServiceClient(){
        return new StudentServiceClient();
    }

    @Bean
    RmiProxyFactoryBean rmiProxyFactoryBean(){
        RmiProxyFactoryBean proxy=new RmiProxyFactoryBean();
        proxy.setServiceInterface(StudentService.class);
        proxy.setServiceUrl("rmi://localhost:1099/StudentService");
        return proxy;
    }
}
