package project.image.domain;
import java.awt.*;
import java.awt.image.BufferedImage;

/**
 * Class used to represent an Image.
 */
public class Image {

    /**
     * All values required to represent an image.
     */
    private Pixel[][] myPixels;
    private Integer height;
    private Integer width;
    private Boolean hasAlpha;

    private String title = "";
    public void setTitle(String title) {
        this.title = title;
    }
    public String getTitle() {
        return title;
    }

    /**
     * Constructor for an empty image with certain height and width.
     * @param height - Integer.
     * @param width - Integer.
     */
    public Image(Integer height, Integer width){
        this.height = height;
        this.width = width;
        this.hasAlpha = true;
        this.myPixels = new Pixel[width][height];
    }

    /**
     * Initialises a new Image from a BufferedImage.
     * @param bufferedImage - data of image as BufferedImage.
     */
    public Image(BufferedImage bufferedImage, String title) {
        this.title = title;
        this.height = bufferedImage.getHeight();
        this.width = bufferedImage.getWidth();
        this.myPixels = new Pixel[width][height];
        this.hasAlpha = bufferedImage.getColorModel().hasAlpha();

        for(int i = 0; i < this.width ; i++){
            for(int j=0; j < this.height; j++) {
                Color c = new Color(bufferedImage.getRGB(i, j), this.hasAlpha);
                Pixel p = new Pixel(c);
                this.myPixels[i][j] = p;
            }
        }
    }

    /**
     * Gets the pixel as a Pixel object at a certain position in the image. Indexing is done as it would be directly on
     * the image, where x is column, and y is row.
     * @param xPosition - Integer.
     * @param yPosition - Integer.
     * @return - The pixel at the mentioned position.
     */
    public Pixel getPixel(Integer xPosition, Integer yPosition){
        return this.myPixels[xPosition][yPosition];
    }

    /**
     * Sets a pixel in a certain position.
     * @param xPosition - Integer.
     * @param yPosition - Integer.
     * @param pixel - the pixel to be set, as a Pixel object.
     */
    public void setPixel(Integer xPosition, Integer yPosition, Pixel pixel) {
        this.myPixels[xPosition][yPosition] = pixel;
    }

    /**
     * Getter for the height property.
     * @return - the height as an Integer.
     */
    public Integer getHeight() {
        return height;
    }

    /**
     * Getter for the width property.
     * @return - the width as an Integer.
     */
    public Integer getWidth() {
        return width;
    }


    /**
     * Convert the Image object to a BufferedImage with or without alpha channel as parameter requests.
     * @param withAlpha - Boolean value, whether the returned BufferedImage should have an alpha channel.
     * @return - BufferedImage.
     */
    public BufferedImage getBufferedImage(Boolean withAlpha){

        int imageType = withAlpha ? BufferedImage.TYPE_INT_ARGB : BufferedImage.TYPE_INT_RGB;

        BufferedImage newImage = new BufferedImage(this.width, this.height, imageType);
        for(int i=0; i< this.width; i++){
            for(int j=0; j < this.height; j++) {
                try {
                    newImage.setRGB(i, j, this.myPixels[i][j].getIntValue(this.hasAlpha, withAlpha));
                } catch (Exception e) {
                    newImage.setRGB(i, j, 0xffffffff);
                }
            }
        }
        return newImage;
    }
}
