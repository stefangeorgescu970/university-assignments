package ro.ubb.remoting.client.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.remoting.rmi.RmiProxyFactoryBean;
import ro.ubb.remoting.common.Student;
import ro.ubb.remoting.common.StudentService;

import java.util.List;

public class StudentServiceClient implements StudentService {
    @Autowired
    private StudentService service;

    @Override
    public List<Student> findAll() {
        return service.findAll();
    }
}
