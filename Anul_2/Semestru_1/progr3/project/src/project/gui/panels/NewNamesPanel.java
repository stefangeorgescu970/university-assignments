package project.gui.panels;

import project.exceptions.NamingErrorException;
import project.gui.GUIConstants;
import javax.swing.*;
import java.awt.*;


/**
 * Class that handles input field for new names option.
 */
public class NewNamesPanel extends JPanel {

    private JLabel baseNameLabel;
    private JTextField baseNameTextField;
    private JLabel digitNumberLabel;
    private JTextField digitNumberTextField;
    private JLabel counterStepLabel;
    private JTextField counterStepTextField;
    private JLabel counterStartLabel;
    private JTextField counterStartTextField;

    NewNamesPanel(){
        this.setLayout(new GridBagLayout());
        GridBagConstraints constraints = new GridBagConstraints();
        constraints.ipadx = 5;
        constraints.ipady = 3;
        constraints.insets = new Insets(3,3,3,3);

        this.baseNameLabel = new JLabel("Base name: ");
        this.baseNameLabel.setFont(GUIConstants.appFont);
        this.baseNameLabel.setPreferredSize(GUIConstants.NewNamesFieldDimension);
        this.baseNameLabel.setMinimumSize(GUIConstants.NewNamesFieldDimension);
        constraints.gridx = 0;
        constraints.gridy = 0;
        this.add(this.baseNameLabel, constraints);

        this.baseNameTextField = new JTextField();
        this.baseNameTextField.setPreferredSize(GUIConstants.NewNamesFieldDimension);
        this.baseNameTextField.setMinimumSize(GUIConstants.NewNamesFieldDimension);
        constraints.gridx = 1;
        this.add(this.baseNameTextField, constraints);

        this.digitNumberLabel = new JLabel("Digits count: ");
        this.digitNumberLabel.setFont(GUIConstants.appFont);
        this.digitNumberLabel.setPreferredSize(GUIConstants.NewNamesFieldDimension);
        this.digitNumberLabel.setMinimumSize(GUIConstants.NewNamesFieldDimension);
        constraints.gridx = 0;
        constraints.gridy = 1;
        this.add(this.digitNumberLabel, constraints);

        this.digitNumberTextField = new JTextField();
        this.digitNumberTextField.setPreferredSize(GUIConstants.NewNamesFieldDimension);
        this.digitNumberTextField.setMinimumSize(GUIConstants.NewNamesFieldDimension);
        constraints.gridx = 1;
        this.add(this.digitNumberTextField, constraints);

        this.counterStepLabel = new JLabel("Counter step: ");
        this.counterStepLabel.setFont(GUIConstants.appFont);
        this.counterStepLabel.setPreferredSize(GUIConstants.NewNamesFieldDimension);
        this.counterStepLabel.setMinimumSize(GUIConstants.NewNamesFieldDimension);
        constraints.gridx = 0;
        constraints.gridy = 2;
        this.add(this.counterStepLabel, constraints);

        this.counterStepTextField = new JTextField();
        this.counterStepTextField.setPreferredSize(GUIConstants.NewNamesFieldDimension);
        this.counterStepTextField.setMinimumSize(GUIConstants.NewNamesFieldDimension);
        constraints.gridx = 1;
        this.add(this.counterStepTextField, constraints);

        this.counterStartLabel = new JLabel("Counter start: ");
        this.counterStartLabel.setFont(GUIConstants.appFont);
        this.counterStartLabel.setPreferredSize(GUIConstants.NewNamesFieldDimension);
        this.counterStartLabel.setMinimumSize(GUIConstants.NewNamesFieldDimension);
        constraints.gridx = 0;
        constraints.gridy = 3;
        this.add(this.counterStartLabel, constraints);

        this.counterStartTextField = new JTextField();
        this.counterStartTextField.setPreferredSize(GUIConstants.NewNamesFieldDimension);
        this.counterStartTextField.setMinimumSize(GUIConstants.NewNamesFieldDimension);
        constraints.gridx = 1;
        this.add(this.counterStartTextField, constraints);
    }

    public String getBaseName() {
        return this.baseNameTextField.getText();
    }

    public String getDigitsCount() throws NamingErrorException {
        try{
            int dummy = Integer.parseInt(this.digitNumberTextField.getText());
            if(dummy == 0) {
                throw new NumberFormatException();
            }
            return this.digitNumberTextField.getText();
        } catch( NumberFormatException nfe) {
            throw new NamingErrorException("Digit count must be an integer value");
        }
    }

    public String getCounterStep() throws NamingErrorException {
        try{
            int dummy = Integer.parseInt(this.counterStepTextField.getText());
            if(dummy == 0) {
                throw new NumberFormatException();
            }
            return this.counterStepTextField.getText();
        } catch( NumberFormatException nfe) {
            throw new NamingErrorException("Counter step must be an integer value");
        }
    }

    public String getCounterStart() throws NamingErrorException {
        try{
            int dummy = Integer.parseInt(this.counterStartTextField.getText());
            return this.counterStartTextField.getText();
        } catch( NumberFormatException nfe) {
            throw new NamingErrorException("Counter start must be an integer value");
        }
    }
}
