package ro.ubb.remoting.client;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import ro.ubb.remoting.common.StudentService;

public class ClientApp {
    public static void main(String[] args) {

        AnnotationConfigApplicationContext context =
                new AnnotationConfigApplicationContext("ro.ubb.remoting.client.config");

        StudentService studentService = (StudentService) context.getBean("studentServiceClient");
        studentService.findAll().forEach(System.out::println);

        System.out.println("bye - client");
    }
}
