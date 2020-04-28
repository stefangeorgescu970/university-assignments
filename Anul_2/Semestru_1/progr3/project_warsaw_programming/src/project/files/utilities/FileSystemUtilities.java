package project.files.utilities;

import project.image.domain.Image;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

public class FileSystemUtilities {

    /**
     * Part of the code that turns this class into a singleton.
     */
    public final static FileSystemUtilities INSTANCE = new FileSystemUtilities();

    private FileSystemUtilities(){ }

    /**
     * Get an Image object form a File
     * @param imageFile a file in the system
     * @return an Image object containing that image
     * @throws IOException From ImageIO.read.
     */
    public Image convertFileToImage(File imageFile) throws IOException {
        BufferedImage bufferedImage = ImageIO.read(imageFile);
        return new Image(bufferedImage, imageFile.getName());
    }
}
