package project.gui.panels;

import project.exceptions.FileNotDirectory;
import project.gui.GUIConstants;
import project.gui.MyGraphicalUserInterface;
import project.image.repository.ImageRepository;
import project.user_preferences.UserPreferences;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.nio.file.NotDirectoryException;


/**
 * Class extending JPanel, encapsulates ImageView and handles viewing all directories and merge results.
 */
public class ImageViewArea extends JPanel {

    private ImageRepository dir1ImageRepository = new ImageRepository();

    public ImageRepository getDir1ImageRepository() {
        return dir1ImageRepository;
    }

    private ImageRepository dir2ImageRepository = new ImageRepository();
    public ImageRepository getDir2ImageRepository() {
        return dir2ImageRepository;
    }

    private ImageRepository mergeResultRepository = new ImageRepository();
    public ImageRepository getMergeResultRepository() {
        return mergeResultRepository;
    }

    private Boolean isWatchingMergeResults = false;
    public Boolean getWatchingMergeResults() {
        return isWatchingMergeResults;
    }

    private MyGraphicalUserInterface delegate;

    public void setDelegate(MyGraphicalUserInterface delegate) {
        this.delegate = delegate;
    }

    private JLabel viewingLabel;
    private JLabel currentDirectoryLabel;
    private JButton refreshButton;
    private ImageView myImageView;
    private ImageView myImageView2;
    private ImageView mergeResultView;
    private JScrollPane myScrollPane;
    private JScrollPane myScrollPane2;
    private JScrollPane mergeResultScroll;


    public void updateLogger(String text){
        this.delegate.changeLoggerText(text);
    }

    public ImageViewArea(){
        this.dir1ImageRepository.setDelegate(this);
        this.dir2ImageRepository.setDelegate(this);

        this.setLayout(new GridBagLayout());
        GridBagConstraints constraints = new GridBagConstraints();
        constraints.ipadx = 5;
        constraints.ipady = 3;
        constraints.fill = GridBagConstraints.HORIZONTAL;

        this.viewingLabel = new JLabel("Viewing: ");
        this.viewingLabel.setFont(GUIConstants.appFont);
        this.viewingLabel.setMinimumSize(GUIConstants.prePathLabelDimension);
        this.viewingLabel.setPreferredSize(GUIConstants.prePathLabelDimension);
        constraints.gridx = 0;
        constraints.gridy = 0;
        this.add(this.viewingLabel, constraints);

        this.currentDirectoryLabel = new JLabel("no directory selected.");
        this.currentDirectoryLabel.setFont(GUIConstants.appFont);
        this.currentDirectoryLabel.setMinimumSize(GUIConstants.pathLabelDimension);
        this.currentDirectoryLabel.setPreferredSize(GUIConstants.pathLabelDimension);
        constraints.gridx = 1;
        constraints.gridwidth = 6;
        this.add(this.currentDirectoryLabel, constraints);

        this.refreshButton = new JButton("Refresh");
        this.refreshButton.setFont(GUIConstants.appFont);
        this.refreshButton.setPreferredSize(GUIConstants.buttonDimension);
        this.refreshButton.setMinimumSize(GUIConstants.buttonDimension);
        this.refreshButton.addActionListener(new ActionListener(){
            @Override
            public void actionPerformed(ActionEvent arg0) {
                refreshButtonPressed();
            }
        });
        constraints.gridx = 7;
        constraints.gridwidth = 1;
        this.add(this.refreshButton, constraints);

        this.myImageView = new ImageView();
        this.myImageView2 = new ImageView();
        this.mergeResultView = new ImageView();
        constraints.gridy = 1;
        constraints.gridx = 0;
        constraints.gridwidth = 8;

        this.myScrollPane = new JScrollPane(this.myImageView);
        this.myScrollPane2 = new JScrollPane(this.myImageView2);
        this.mergeResultScroll = new JScrollPane(this.mergeResultView);

        this.myScrollPane.setPreferredSize(GUIConstants.ScrollAreaDimension);
        this.myScrollPane.setMinimumSize(GUIConstants.ScrollAreaDimension);
        this.myScrollPane.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);

        this.myScrollPane2.setPreferredSize(GUIConstants.ScrollAreaDimension);
        this.myScrollPane2.setMinimumSize(GUIConstants.ScrollAreaDimension);
        this.myScrollPane2.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);

        this.mergeResultScroll.setPreferredSize(GUIConstants.ScrollAreaDimension);
        this.mergeResultScroll.setMinimumSize(GUIConstants.ScrollAreaDimension);
        this.mergeResultScroll.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);

        this.add(this.myScrollPane, constraints);
        this.add(this.myScrollPane2, constraints);
        this.add(this.mergeResultScroll, constraints);
        this.mergeResultScroll.setVisible(false);
        this.myScrollPane2.setVisible(false);
    }


    /**
     * Called after a directory changes by user action.
     * @param newDir the directory that was selected by the user
     * @param changedDir either Directory1: or Directory2:
     * @return true if there were new images to be added, false otherwise
     */
    public Boolean updateRepository(File newDir, String changedDir){

        this.currentDirectoryLabel.setText(changedDir.substring(0, changedDir.length()-1));

        try{
            if (changedDir.equals("Directory 1:")) {
                this.dir1ImageRepository.populateRepository(newDir);
                UserPreferences.INSTANCE.updateDirectory1(newDir);
                this.myScrollPane2.setVisible(false);
                this.mergeResultScroll.setVisible(false);

                if(this.dir1ImageRepository.isEmpty()) {
                    this.myImageView.clear();
                    this.myScrollPane.setVisible(true);
                    return false;
                }

                this.myScrollPane.setVisible(true);
                this.myImageView.setRepository(this.dir1ImageRepository);
                this.myImageView.displayImages();

                return true;

            } else {
                this.dir2ImageRepository.populateRepository(newDir);
                UserPreferences.INSTANCE.updateDirectory2(newDir);
                this.myScrollPane.setVisible(false);
                this.mergeResultScroll.setVisible(false);

                if(this.dir2ImageRepository.isEmpty()) {
                    this.myImageView2.clear();
                    this.myScrollPane2.setVisible(true);
                    return false;
                }

                this.myScrollPane2.setVisible(true);
                this.myImageView2.setRepository(this.dir2ImageRepository);
                this.myImageView2.displayImages();

                return true;
            }
        } catch (FileNotDirectory fnd) {
            final JPanel panel = new JPanel();
            JOptionPane.showMessageDialog(panel, fnd.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
            return false;
        }

    }


    /**
     * Called when the user clicks a different file paths
     * @param dir the directory the user wants to view
     */
    public void updateDisplayArea(String dir){
        this.currentDirectoryLabel.setText(dir.substring(0, dir.length()-1));

        if (dir.equals("Directory 1:")) {
            this.mergeResultScroll.setVisible(false);
            this.myScrollPane2.setVisible(false);

            this.myScrollPane.setVisible(true);

        } else {
            this.myScrollPane.setVisible(false);
            this.mergeResultScroll.setVisible(false);

            this.myScrollPane2.setVisible(true);
        }
    }

    /**
     * Called after a merge is done, or when a merge is discarded, or when changing directories,
     * to handle the way ui looks whether we are viewing merge or not.
     * @param isViewingResults true if we need to view results, false otherwise
     */
    public void morphForViewMergeResults(Boolean isViewingResults) {
        if(isViewingResults) {
            this.isWatchingMergeResults = true;
            this.refreshButton.setVisible(false);
        } else {
            this.isWatchingMergeResults = false;
            this.mergeResultScroll.setVisible(false);

            this.refreshButton.setVisible(true);
        }
    }

    /**
     * Sets the viewing area on directory 1 when we discard merge results.
     */
    public void defaultToDir(){
        this.myScrollPane2.setVisible(false);
        this.myScrollPane.setVisible(true);
        this.currentDirectoryLabel.setText("Directory 1");
    }

    /**
     * Called when a merge is done, and displays it.
     * @param mergeResultRepository An ImageRepository containing results of merge.
     */
    public void handleMergeResults(ImageRepository mergeResultRepository) {

        this.mergeResultRepository = mergeResultRepository;
        this.mergeResultView.clear();

        this.myScrollPane.setVisible(false);
        this.myScrollPane2.setVisible(false);

        this.mergeResultView.setRepository(this.mergeResultRepository);
        this.mergeResultView.displayImages();
        this.mergeResultScroll.setVisible(true);
        this.currentDirectoryLabel.setText("Merge results.");
    }


    /**
     * Called when the user requests a remove of directory settings.
     * @param dir the requesting directory
     */
    public void handleClearButtonPressed(String dir){
        this.currentDirectoryLabel.setText("");
        if(dir.equals("Directory 1:")) {
            this.dir1ImageRepository.clear();
            UserPreferences.INSTANCE.discardDirectory1();
            this.myImageView.clear();
        } else {
            this.myImageView2.clear();
            UserPreferences.INSTANCE.discardDirectory2();
            this.dir2ImageRepository.clear();
        }
    }

    /**
     * Gets called when the refresh button is pressed.
     */
    private void refreshButtonPressed(){
        String dir = this.currentDirectoryLabel.getText();

        this.handleClearButtonPressed(dir + ":");

        try{
            if(dir.equals("Directory 1")) {
                this.currentDirectoryLabel.setText("Directory 1");
                this.dir1ImageRepository.refreshRepository();
                this.myImageView.setRepository(this.dir1ImageRepository);
                this.myImageView.setVisible(false);
                this.myImageView.setVisible(true);
            } else {
                this.currentDirectoryLabel.setText("Directory 2");
                this.dir2ImageRepository.refreshRepository();
                this.myImageView2.setRepository(this.dir2ImageRepository);
                this.myImageView2.setVisible(false);
                this.myImageView2.setVisible(true);
            }
        } catch (FileNotDirectory fnd) {
            final JPanel panel = new JPanel();
            JOptionPane.showMessageDialog(panel, fnd.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        }
    }
}
