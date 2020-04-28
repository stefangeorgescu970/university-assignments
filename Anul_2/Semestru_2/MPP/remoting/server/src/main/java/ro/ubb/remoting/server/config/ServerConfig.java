package ro.ubb.remoting.server.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.remoting.rmi.RmiServiceExporter;
import ro.ubb.remoting.common.StudentService;
import ro.ubb.remoting.server.service.StudentServiceImpl;

@Configuration
public class ServerConfig {
    @Bean
    StudentService studentService() {
        return new StudentServiceImpl();
    }

    @Bean
    RmiServiceExporter rmiServiceExporter(){
        RmiServiceExporter exporter=new RmiServiceExporter();
        exporter.setServiceName("StudentService");
        exporter.setServiceInterface(StudentService.class);
        exporter.setService(studentService());
        return exporter;
    }
}
