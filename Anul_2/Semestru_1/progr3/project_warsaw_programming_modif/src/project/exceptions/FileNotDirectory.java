package project.exceptions;

public class FileNotDirectory extends Exception{

    public FileNotDirectory() {}

    public FileNotDirectory(String message) {
        super(message);
    }
}