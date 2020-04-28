package project.image.processing;


/**
 * Collection of merge possibilities for the algorithm to use, with a short description.
 */
public enum MergeVariant {

    NORMAL("Normal", "Replace each pixel with the color in between the two."),
    HARD_MIX("Hard Mix", "All pixels will get either red, green, blue, white or black depending on some rules."),
    AND("AND", "Applies an AND binary operation."),
    OR("OR", "Applies an OR binary operation."),
    XOR("XOR", "Applies an XOR binary operation.");
    /**
     * The properties mentioned in the enum description.
     */
    private final String description;
    private final String name;

    /**
     * Private constructor for the MergeVariant enum.
     * @param description - the description of the merge algorithm.
     * @param name - the name of the method.
     */
    MergeVariant(String name, String description){
        this.name = name;
        this.description = description;
    }

    /**
     * Getter for the description property.
     * @return - a String containing the description of the property.
     */
    public String getDescription() {
        return description;
    }

    /**
     * Getter for the name property.
     * @return - a String containing the name of the property.
     */
    public String getName() {
        return name;
    }

    /**
     * Return the MergeVariant enum value of a given string.
     * @param name the name.
     * @return the MergeValue, normal if not identified.
     */
    public static MergeVariant getValueForName(String name){
        for (MergeVariant variant : MergeVariant.values()){
            if (variant.getName().equals(name)) {
                return variant;
            }
        }
        return MergeVariant.NORMAL;
    }
}
