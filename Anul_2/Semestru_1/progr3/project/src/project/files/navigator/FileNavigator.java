package project.files.navigator;

import project.exceptions.FileNotDirectory;
import project.image.processing.OutputFormat;
import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class FileNavigator {

    /**
     * Part of the code that turns this class into a singleton.
     */
    public final static FileNavigator INSTANCE = new FileNavigator();

    private FileNavigator(){ }


    /**
     * Checks if a given file matches the picture formats accepted by the app.
     * @param myFile a file in the selected directory.
     * @return true if the file matches the format and false otherwise.
     */
    private Boolean matchesFormat(File myFile) {
        return myFile.getName().toLowerCase().endsWith(OutputFormat.BMP.getExtension()) ||
                myFile.getName().toLowerCase().endsWith(OutputFormat.JPEG.getExtension()) ||
                myFile.getName().toLowerCase().endsWith(OutputFormat.JPG.getExtension()) ||
                myFile.getName().toLowerCase().endsWith(OutputFormat.PNG.getExtension()) ||
                myFile.getName().toLowerCase().endsWith(OutputFormat.TIF.getExtension()) ||
                myFile.getName().toLowerCase().endsWith(OutputFormat.TIFF.getExtension());
    }


    /**
     * Returns a list of files containing images from a given directory
     * @param directory a File, preferably a directory, otherwise bam, exception
     * @return a list of images from the directory
     * @throws FileNotDirectory if the file is not a directory
     */
    public List<File> getImagesInDirectory(File directory) throws FileNotDirectory {
        if(!directory.isDirectory())
            throw new FileNotDirectory("The provided File is not a directory: " + directory.getAbsolutePath());

        List<File> myPictures = new ArrayList<>();
        File[] myFiles = directory.listFiles();

        if (myFiles != null) {
            for(File newFile : myFiles) {
                if(this.matchesFormat(newFile)) {
                    myPictures.add(newFile);
                }
            }
        }
        return myPictures;
    }
}
