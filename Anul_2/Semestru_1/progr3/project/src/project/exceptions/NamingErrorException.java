package project.exceptions;

/**
 * Extends class exception for better exception handling in-app
 */
public class NamingErrorException extends Exception{

    /**
     * Extend the constructor from Exception class
     * @param message Error message
     */
    public NamingErrorException(String message) {
        super(message);
    }
}
