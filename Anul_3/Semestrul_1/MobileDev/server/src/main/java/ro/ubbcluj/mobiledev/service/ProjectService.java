package ro.ubbcluj.mobiledev.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ro.ubbcluj.mobiledev.model.Project;
import ro.ubbcluj.mobiledev.model.dto.AllProjectsDTO;
import ro.ubbcluj.mobiledev.model.dto.ProjectDTO;
import ro.ubbcluj.mobiledev.repository.ProjectRepository;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ProjectService {

    @Autowired
    private ProjectRepository repository;

    public Integer addProject(Project newProject) {
        Project saved = repository.save(newProject);
        return saved.getId();
    }

    public AllProjectsDTO getAll() {
        return AllProjectsDTO.builder().projects(repository.findAll().stream().map(ProjectDTO::new).collect(Collectors.toList())).build();
    }
}
