package project.gui.panels;

import project.exceptions.NamingErrorException;

import javax.swing.*;
import java.awt.*;

/**
 * Class used for keeping names option.
 */
public class KeepNamesPanel extends JPanel {
    private JRadioButton button1;
    private JRadioButton button2;
    private ButtonGroup buttonGroup;

    public KeepNamesPanel(){
        this.setLayout(new GridBagLayout());
        GridBagConstraints constraints = new GridBagConstraints();
        constraints.ipadx = 5;
        constraints.ipady = 3;

        this.button1 = new JRadioButton("Directory 1");
        constraints.gridx = 0;
        constraints.gridy = 0;
        this.add(this.button1, constraints);

        this.button2 = new JRadioButton("Directory 2");
        constraints.gridx = 0;
        constraints.gridy = 1;
        this.add(this.button2, constraints);

        this.buttonGroup = new ButtonGroup();
        this.buttonGroup.add(this.button1);
        this.buttonGroup.add(this.button2);
    }

    public String getSelectedDirectory() throws NamingErrorException {

        if(!this.button1.isSelected() && !this.button2.isSelected()){
            throw new NamingErrorException("Please select one of the two directories.");
        }

        if(this.button1.isSelected())
            return this.button1.getText();

        return this.button2.getText();
    }
}
