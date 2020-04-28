package ro.ubbcluj.mobiledev.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import ro.ubbcluj.mobiledev.model.Task;

public interface TaskRepository extends JpaRepository<Task, Integer> {

}
