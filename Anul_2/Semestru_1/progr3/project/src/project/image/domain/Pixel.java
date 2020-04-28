package project.image.domain;

import java.awt.*;

/**
 * Class used to represent a pixel.
 */
public class Pixel {

    /**
     * Integer values for all the channels in ARGB representation.
     */
    private Integer redChannel;
    private Integer greenChannel;
    private Integer blueChannel;
    private Integer alphaChannel;

    /**
     * Default constructor for Pixel class.
     */
    public Pixel() {
        this.redChannel = 0;
        this.greenChannel = 0;
        this.blueChannel = 0;
        this.alphaChannel = 0;
    }

    /**
     * Constructor for Pixel class that receives and object of type Color and initialises all channels accordingly.
     * @param pixelColor - an object of type Color, the information about the pixel.
     */
    Pixel(Color pixelColor) {
        this.redChannel = pixelColor.getRed();
        this.greenChannel = pixelColor.getGreen();
        this.blueChannel = pixelColor.getBlue();
        this.alphaChannel = pixelColor.getAlpha();
    }

    /**
     * Getter for the value of the red channel.
     * @return - Integer with the value of the red channel.
     */
    public Integer getRedChannel() {
        return redChannel;
    }

    /**
     * Setter for the value of the red channel.
     * @param redChannel - Integer containing the new value of the red channel.
     */
    public void setRedChannel(Integer redChannel) {
        this.redChannel = redChannel;
    }

    /**
     * Getter for the value of the green channel.
     * @return - Integer with the value of the green channel.
     */
    public Integer getGreenChannel() {
        return greenChannel;
    }

    /**
     * Setter for the value of the green channel.
     * @param greenChannel - Integer containing the new value of the green channel.
     */
    public void setGreenChannel(Integer greenChannel) {
        this.greenChannel = greenChannel;
    }

    /**
     * Getter for the value of the blue channel.
     * @return - Integer with the value of the blue channel.
     */
    public Integer getBlueChannel() {
        return blueChannel;
    }

    /**
     * Setter for the value of the blue channel.
     * @param blueChannel - Integer containing the new value of the blue channel.
     */
    public void setBlueChannel(Integer blueChannel) {
        this.blueChannel = blueChannel;
    }

    /**
     * Getter for the value of the alpha channel.
     * @return - Integer with the value of the alpha channel.
     */
    public Integer getAlphaChannel() {
        return alphaChannel;
    }

    /**
     * Setter for the value of the alpha channel.
     * @param alphaChannel - Integer containing the new value of the alpha channel.
     */
    public void setAlphaChannel(Integer alphaChannel) {
        this.alphaChannel = alphaChannel;
    }

    /**
     * Converts the pixel to its int value.
     * @param hasAlpha - if the format of the image we got this pixel from has alpha channel.
     * @param needAlpha - if the format we want this image to export to requires alpha channel.
     * @return - the corresponding int value
     */
    int getIntValue(Boolean hasAlpha, Boolean needAlpha) {

        int rgb = (this.redChannel<<16 ) | (this.greenChannel<<8) | this.blueChannel;

        if (hasAlpha && needAlpha){
            rgb = (this.alphaChannel << 24) | rgb;
        } else if (needAlpha) {
            rgb =  0xff000000 | rgb ;
        }
        return rgb;
    }
}
