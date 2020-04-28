package project.gui;

import project.gui.dtos.MergePreferencesDTO;
import project.gui.dtos.MergePreferencesDTOConstants;
import project.gui.panels.DirectorySelectPanel;
import project.gui.panels.ImageViewArea;
import project.gui.panels.OperationsPanel;
import project.image.domain.Image;
import project.image.processing.*;
import project.image.repository.ImageRepository;
import project.user_preferences.UserPreferences;

import javax.swing.*;
import java.awt.*;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.io.File;
import java.io.IOException;

/**
 * The main gui of the app
 */
public class MyGraphicalUserInterface {

    private JFrame myMainFrame;
    private DirectorySelectPanel directory1Panel;
    private DirectorySelectPanel directory2Panel;
    private ImageViewArea imageViewArea;
    private OperationsPanel operationsPanel;
    private JLabel loggerLabel;

    public MyGraphicalUserInterface() {
        this.myMainFrame = new JFrame();
        this.myMainFrame.setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE);
        this.myMainFrame.setTitle("Image Merger Beta");
        this.myMainFrame.setSize(GUIConstants.AppFinalSize);
        this.myMainFrame.setLayout(new GridBagLayout());


        GridBagConstraints constraints = new GridBagConstraints();

        // Center the frame in the middle of the screen
        this.myMainFrame.setLocationRelativeTo(null);

        this.directory1Panel = new DirectorySelectPanel();
        this.directory1Panel.setDelegate(this);


        this.directory2Panel = new DirectorySelectPanel();
        this.directory2Panel.setDelegate(this);

        constraints.gridx = 0;
        constraints.gridy = 0;
        constraints.gridwidth = 8;
        constraints.insets = new Insets(5,0,0,0);
        this.myMainFrame.add(this.directory1Panel, constraints);

        constraints.insets = new Insets(0,0,0,0);
        constraints.gridy=1;
        this.myMainFrame.add(this.directory2Panel, constraints);

        this.imageViewArea = new ImageViewArea();
        this.imageViewArea.setDelegate(this);
        constraints.gridy = 2;
        this.myMainFrame.add(this.imageViewArea, constraints);

        this.operationsPanel = new OperationsPanel();
        this.operationsPanel.setDelegate(this);
        constraints.gridx = 8;
        constraints.gridy = 0;
        constraints.gridwidth = 2;
        constraints.gridheight = 5;
        this.myMainFrame.add(this.operationsPanel, constraints);

        this.loggerLabel = new JLabel("Currently doing: nothing");
        this.loggerLabel.setFont(GUIConstants.appFont);
        constraints.gridx = 0;
        constraints.gridy = 10;
        constraints.gridheight = 1;
        constraints.gridwidth = 8;
        this.myMainFrame.add(this.loggerLabel, constraints);


        this.myMainFrame.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                super.windowClosing(e);

                int result = JOptionPane.showConfirmDialog(null, "All unsaved progress will be lost. Do you wish to continue?", "Warning",
                        JOptionPane.YES_NO_OPTION);

                if(result == JOptionPane.YES_OPTION) {
                    UserPreferences.INSTANCE.dumpToFile();
                    System.exit(0);
                }
            }
        });



        this.myMainFrame.setMinimumSize(GUIConstants.AppFinalSize);



        this.myMainFrame.setVisible(true);

        this.tryForPreviousDirectories();
    }

    
    public void changeLoggerText(String text){
        this.loggerLabel.setText("Currently doing: " + text);
    }



    /**
     * Called when we press the select or change button and finalise choosing a directory.
     * @param newDir the new dir we selected
     * @param changedDir the directory (1 or 2) that was changed
     */
    public void filePathChanged(File newDir, String changedDir) {
        Boolean hasImages = this.imageViewArea.updateRepository(newDir, changedDir);
        if(changedDir.equals("Directory 1:")) {
            this.directory1Panel.displayAlert(!hasImages);
        } else {
            this.directory2Panel.displayAlert(!hasImages);
        }
    }

    /**
     * Called when the user presses one of the two directory paths to view it.
     * @param dir the pressed directory
     */
    public void displayDirectory(String dir){
        this.imageViewArea.updateDisplayArea(dir);
    }


    /**
     * Called when the user requests a merge
     * @param preferencesDTO data transfer object containing the way the Merge will be done
     */
    public void handleMergeRequest(MergePreferencesDTO preferencesDTO) {
        // If we got here than we know the preferences DTO is ok, so we start parsing it.

        String mergeMethod = preferencesDTO.get(MergePreferencesDTOConstants.Algorithm);
        MergeVariant mergeVariant = MergeVariant.getValueForName(mergeMethod);

        FittingMethod fittingMethod = FittingMethod.getValueForName(preferencesDTO.get(MergePreferencesDTOConstants.FittingMethod));

        ImageRepository repo1 = this.imageViewArea.getDir1ImageRepository();
        ImageRepository repo2 = this.imageViewArea.getDir2ImageRepository();

        if(!repo1.isEmpty() && !repo2.isEmpty()) {
            this.changeLoggerText("preparing merge results.");

            ImageRepository mergedImages = ImageMerger.INSTANCE.mergeImageRepos(repo1, repo2, mergeVariant, fittingMethod);

            this.changeLoggerText("nothing");

            if(preferencesDTO.get(MergePreferencesDTOConstants.Naming).equals("Generate new names")) {
                String baseName = preferencesDTO.get(MergePreferencesDTOConstants.Base);
                String digitsNumber = preferencesDTO.get(MergePreferencesDTOConstants.Digits);
                String counterStep = preferencesDTO.get(MergePreferencesDTOConstants.Step);
                String counterStart = preferencesDTO.get(MergePreferencesDTOConstants.Start);

                Integer counter = Integer.parseInt(counterStart);
                Integer step = Integer.parseInt(counterStep);
                Integer digitNum = Integer.parseInt(digitsNumber);

                String name;
                for(Image image : mergedImages.getImages()){
                    String counterZeros = "";
                    for( int i = 0; i < digitNum - counter.toString().length(); i++){
                        counterZeros += "0";
                    }

                    name = baseName + counterZeros + counter.toString();
                    counter += step;

                    image.setTitle(name);
                }
            } else {
                String dir = preferencesDTO.get(MergePreferencesDTOConstants.Directory);

                if(dir.equals("Directory 1")) {
                    for(int i=0; i < repo1.getImages().size(); i++) {
                        mergedImages.getImages().get(i).setTitle(repo1.getImages().get(i).getTitle());
                    }
                } else {
                    for(int i=0; i < repo2.getImages().size(); i++) {
                        mergedImages.getImages().get(i).setTitle(repo2.getImages().get(i).getTitle());
                    }
                }

            }
            this.imageViewArea.handleMergeResults(mergedImages);
            this.setUserIsViewingMergeResults(true);
        } else {
            final JPanel panel = new JPanel();

            JOptionPane.showMessageDialog(panel, "One of the selected directories is empty.", "Error", JOptionPane.ERROR_MESSAGE);
        }


    }

    /**
     * Return whether the user is watching merge results or not.
     * @return true if in the view are we have merge results, false otherwise.
     */
    public Boolean userIsViewingMergeResults(){
        return this.imageViewArea.getWatchingMergeResults();
    }

    /**
     * Handle whether we are viewing merge results or not
     * @param isViewing bool true or false
     */
    public void setUserIsViewingMergeResults(Boolean isViewing){
        this.imageViewArea.morphForViewMergeResults(isViewing);
        this.operationsPanel.morphForMergeResults(isViewing);
    }

    /**
     * Handle a save request.
     */
    public void handleSave() {
        ImageRepository toExport = this.imageViewArea.getMergeResultRepository();

        String pathName = null;

        if(System.getProperty("os.name").toLowerCase().contains("mac")){

            JFrame frame = new JFrame("Select a Directory");
            FileDialog fd = new FileDialog(frame, "Choose a directory", FileDialog.SAVE);
            fd.setDirectory("");
            fd.setVisible(true);
            String filename2 = fd.getDirectory();
            if (filename2 != null) {
                pathName = fd.getDirectory();
            }


        } else {

            JFileChooser chooser = new JFileChooser();

            chooser.setCurrentDirectory(new java.io.File("."));
            chooser.setDialogTitle("choosertitle");
            chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);
            chooser.setAcceptAllFileFilterUsed(false);

            if (chooser.showOpenDialog(null) == JFileChooser.APPROVE_OPTION) {
                pathName = chooser.getSelectedFile().toString();
            }
        }

        if(pathName != null) {
            File myDir = new File(pathName);
            OutputFormat outputFormat = this.operationsPanel.getOutputFormat();

            for(Image image : toExport.getImages()) {
                try {
                    ImageExporter.INSTANCE.exportImage(image, myDir, image.getTitle(), outputFormat);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }






    }

    /**
     * Called when discard button is pressed
     */
    public void handleDiscardButton() {
        int result = JOptionPane.showConfirmDialog(null, "All merge progress will be lost. Do you wish to continue?", "Warning",
                JOptionPane.YES_NO_OPTION);

        if(result == JOptionPane.YES_OPTION) {
            this.setUserIsViewingMergeResults(false);
            this.imageViewArea.defaultToDir();
        }
    }

    /**
     * Called when clear button was pressed.
     * @param dir
     */
    public void handleClearButtonPressed(String dir) {
        this.imageViewArea.handleClearButtonPressed(dir);
    }

    /**
     * Tries to read from user preferences, and set the directories accordingly.
     */
    private void tryForPreviousDirectories() {

        UserPreferences.INSTANCE.loadFromFile();
        File dir1 = UserPreferences.INSTANCE.getDirectory1();
        File dir2 = UserPreferences.INSTANCE.getDirectory2();

        if(dir1 != null) {
            this.filePathChanged(dir1, "Directory 1:");
            this.directory1Panel.setFilePath(dir1.getAbsolutePath());
            this.directory1Panel.setSelectOrChangeButtonText("Change");

        }

        if(dir2 != null) {
            this.filePathChanged(dir2, "Directory 2:");
            this.directory2Panel.setFilePath(dir2.getAbsolutePath());
            this.directory2Panel.setSelectOrChangeButtonText("Change");
        }

    }
}
