package project.image.processing;

/**
 * Holds all possible types of output formats, with their extension and whether or not they support an alpha channel.
 */
public enum OutputFormat {

    JPG("jpg", false),
    JPEG("jpeg", false),
    BMP("bmp", false),
    PNG("png", true),
    TIF("tif", true),
    TIFF("tiff", true);

    /**
     * The two properties mentioned in the enum description.
     */
    private final String extension;
    private final Boolean supportsAlpha;


    /**
     * Private constructor for the OutputFormat enum.
     * @param extension - The extension of a file with that type.
     * @param supportsAlpha - Existence of an alpha channel to encode transparency.
     */
    OutputFormat(String extension, Boolean supportsAlpha){
        this.extension = extension;
        this.supportsAlpha = supportsAlpha;
    }

    /**
     * Getter for the extension property.
     * @return The extension of a file of given type as a String.
     */
    public String getExtension() {
        return extension;
    }

    /**
     * Getter for the supportsAlpha property.
     * @return Boolean value true if the format supports an alpha channel, false otherwise.
     */
    public Boolean getSupportsAlpha() {
        return supportsAlpha;
    }
}
