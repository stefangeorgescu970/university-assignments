package project.gui.panels;

import project.gui.GUIConstants;
import project.gui.utils.ImageDrawer;
import project.image.domain.Image;

import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.image.BufferedImage;
import javax.swing.*;


/**
 * Image viewing panel, clickable so you can view large image.
 */
public class ImagePanel extends JPanel implements MouseListener{

    private BufferedImage image;
    private String imageTitle;

    public ImagePanel(Image myImage) {
        this.setMinimumSize(GUIConstants.imagePanelDimension);
        this.setPreferredSize(GUIConstants.imagePanelDimension);
        this.image = myImage.getBufferedImage(false);
        this.imageTitle = myImage.getTitle();
        this.addMouseListener(this);
        JLabel label = new JLabel(this.imageTitle);
        label.setFont(GUIConstants.ImageTitleFont);
        this.add(label, LEFT_ALIGNMENT);
    }

    /**
     * Override to paint the image.
     * @param g own graphics
     */
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.clearRect(0,0,1000,1000);
        g.drawImage(image, 10, 24,135,135, this);
    }

    /**
     * When an image is clicked, display it in different frame, and big.
     * @param event
     */
    @Override
    public void mouseClicked(MouseEvent event) {
        final ImagePanel clicked = (ImagePanel) event.getSource();

        JFrame newFrame = new JFrame(clicked.imageTitle);

        JPanel panel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                ImageDrawer.INSTANCE.drawScaledImage(clicked.image, this, g);
            }
        };
        newFrame.setSize(new Dimension(1020,1020));
        panel.setSize(new Dimension(1020,1020));

        newFrame.add(panel);
        newFrame.setVisible(true);
    }

    @Override
    public void mousePressed(MouseEvent e) {

    }

    @Override
    public void mouseReleased(MouseEvent e) {

    }

    @Override
    public void mouseEntered(MouseEvent e) {

    }

    @Override
    public void mouseExited(MouseEvent e) {

    }
}