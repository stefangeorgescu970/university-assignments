package ro.ubbcluj.mobiledev.repository;

import org.springframework.data.jpa.repository.JpaRepository;
import ro.ubbcluj.mobiledev.model.Project;

public interface ProjectRepository extends JpaRepository<Project, Integer> {
}
