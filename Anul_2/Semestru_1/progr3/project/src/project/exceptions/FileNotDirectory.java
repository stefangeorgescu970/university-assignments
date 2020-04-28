package project.exceptions;

/**
 * Extends class exception for better exception handling in-app
 */
public class FileNotDirectory extends Exception{

    /**
     * Extend the constructor from Exception class
     * @param message Error message
     */
    public FileNotDirectory(String message) {
        super(message);
    }
}