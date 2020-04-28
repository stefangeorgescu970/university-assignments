package ro.ubb.remoting.server.service;

import ro.ubb.remoting.common.Student;
import ro.ubb.remoting.common.StudentService;

import java.util.Arrays;
import java.util.List;

public class StudentServiceImpl implements StudentService {
    @Override
    public List<Student> findAll() {
        return Arrays.asList(
                new Student("john", 10),
                new Student("mary", 10)
        );
    }
}
