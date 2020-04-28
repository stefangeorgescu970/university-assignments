package project.image.processing;


/**
 * Collection of fitting possibilities for the algorithm to use.
 */
public enum FittingMethod {

    PRESERVE_RATIO("Preserve ratio"),
    DISCARD_RATIO("Fit width and height");
    /**
     * The properties mentioned in the enum description.
     */
    private final String name;

    /**
     * Private constructor for the MergeVariant enum.
     * @param name - the name of the method.
     */
    FittingMethod(String name){
        this.name = name;

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
    public static FittingMethod getValueForName(String name){
        for (FittingMethod variant : FittingMethod.values()){
            if (variant.getName().equals(name)) {
                return variant;
            }
        }
        return FittingMethod.PRESERVE_RATIO;
    }
}
