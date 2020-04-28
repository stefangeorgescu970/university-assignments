package project.image.repository;

import project.exceptions.FileNotDirectory;
import project.files.navigator.FileNavigator;
import project.files.utilities.FileSystemUtilities;
import project.gui.panels.ImageViewArea;
import project.image.domain.Image;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;



/**
 * Class that encapsulates a list of images, and holds the File the images came from.
 */
public class ImageRepository {

    private List<Image> myImages;
    private File directory;
    private ImageViewArea delegate;

    public void setDelegate(ImageViewArea delegate) {
        this.delegate = delegate;
    }

    public ImageRepository(){
        this.myImages = new ArrayList<>();
    }

    /**
     * Populate the repository with the image files from a given directory
     * @param directory the directory.
     */
    public void populateRepository(File directory) throws FileNotDirectory {
        try {
            this.myImages.clear();

            List<File> myImageFiles = FileNavigator.INSTANCE.getImagesInDirectory(directory);
            for(File imageFile : myImageFiles) {

                this.delegate.updateLogger("parsing image with title " + imageFile.getName());

                this.myImages.add(FileSystemUtilities.INSTANCE.convertFileToImage(imageFile));
            }

            this.delegate.updateLogger("nothing");

            this.directory = directory;
        } catch (IOException e) {
            throw new FileNotDirectory("A weird error happened. Please restart the app.");
        }
    }

    public void refreshRepository() throws FileNotDirectory{
        this.populateRepository(this.directory);
    }

    public File getDirectory() {
        return this.directory;
    }

    public List<Image> getImages(){
        return this.myImages;
    }

    public Boolean isEmpty() {
        return this.myImages.isEmpty();
    }

    public void addImage(Image image){
        this.myImages.add(image);
    }

    public void clear() {
        this.myImages.clear();
    }
}
