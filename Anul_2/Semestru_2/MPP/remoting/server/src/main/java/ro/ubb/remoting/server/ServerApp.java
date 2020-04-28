package ro.ubb.remoting.server;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import ro.ubb.remoting.common.StudentService;

public class ServerApp {
    public static void main(String[] args) {
        AnnotationConfigApplicationContext context =
                new AnnotationConfigApplicationContext("ro.ubb.remoting.server.config");

//        StudentService studentService=context.getBean(StudentService.class);
//        studentService.findAll().forEach(System.out::println);



        System.out.println("bye - server");
    }
}
