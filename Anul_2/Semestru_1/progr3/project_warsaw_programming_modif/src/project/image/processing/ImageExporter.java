package project.image.processing;

import project.image.domain.*;
import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

/**
 * Singleton used to export an image to the file system.
 */
public class ImageExporter {

    /**
     * Part of the code that turns this class into a singleton.
     */
    public final static ImageExporter INSTANCE = new ImageExporter();

    private ImageExporter(){ }

    /**
     * Export an image to the file system.
     * @param myImage - the image to be saved, given as an Image object.
     * @param fileName - a String containing how the file should be named.
     * @param imageFormat - an OutputFormat enum option.
     * @throws IOException - from the File instantiation.
     */
    public void exportImage(Image myImage, File dir, String fileName, OutputFormat imageFormat) throws IOException {
        BufferedImage out = myImage.getBufferedImage(imageFormat.getSupportsAlpha());
        File output = new File(dir.getPath()  + "/" + fileName + "." + imageFormat.getExtension());
        ImageIO.write(out, imageFormat.getExtension(), output);
    }
}
