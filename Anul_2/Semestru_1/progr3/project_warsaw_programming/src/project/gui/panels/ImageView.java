package project.gui.panels;

import project.image.domain.Image;
import project.image.repository.ImageRepository;
import javax.swing.*;
import java.awt.*;
import java.util.ArrayList;
import java.util.List;


/**
 * Class extending JPanel, used to display images that are currently selected.
 */
public class ImageView extends JPanel{

    public ImageView(){

    }

    private List<ImagePanel> myImagePanels = new ArrayList<>();

    /**
     * Display all images on the canvas
     */
    public void displayImages(){

        this.removeAll();

        this.setLayout(new GridBagLayout());
        GridBagConstraints constraints = new GridBagConstraints();
        constraints.ipadx = 5;
        constraints.ipady = 5;
        constraints.gridwidth = 2;
        constraints.gridheight = 2;
        constraints.gridx = 0;
        constraints.gridy = 1;
        constraints.fill = GridBagConstraints.HORIZONTAL;

        for(ImagePanel imagePanel : this.myImagePanels){
            this.add(imagePanel,constraints);
            constraints.gridx += 3;
            if(constraints.gridx > 7){ constraints.gridx = 0; constraints.gridy += 3;}
        }

    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.clearRect(0,0,1000,1000);
    }

    /**
     * Populates the image panels list from an ImageRepository object
     * @param myImageRepository an object that encapsulates images
     */
    public void setRepository(ImageRepository myImageRepository){
        this.myImagePanels.clear();
        for(Image myImage : myImageRepository.getImages()) {
            this.myImagePanels.add(new ImagePanel(myImage));
        }
        this.displayImages();
    }

    /**
     * Clear imagePanels from memory and from canvas
     */
    public void clear(){
        this.myImagePanels.clear();
        this.removeAll();
    }
}
