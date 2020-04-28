package project.gui.dtos;

import java.util.HashMap;
import java.util.Map;


/**
 * Simple data transfer object for merge preferences.
 */
public class MergePreferencesDTO {

    private Map<String, String> preferences = new HashMap<>();

    /**
     * Add a new preference
     * @param key the key the param is under
     * @param value the value provided by the user
     */
    public void add(String key, String value){
        this.preferences.put(key, value);
    }

    /**
     * Get a parameter. We use constant string values, no risk of trying to get something that we don't have.
     * @param key the key to get the param
     * @return the value of that key in the dictionary.
     */
    public String get(String key){
        return this.preferences.get(key);
    }

}
