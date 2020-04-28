package project.gui.panels;


import project.exceptions.NamingErrorException;
import project.gui.GUIConstants;
import project.gui.dtos.MergePreferencesDTO;
import project.gui.MyGraphicalUserInterface;
import project.gui.dtos.MergePreferencesDTOConstants;
import project.image.processing.FittingMethod;
import project.image.processing.MergeVariant;
import project.image.processing.OutputFormat;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.lang.ref.WeakReference;


/**
 * Class that extends JPanel and adds all requirements of the app.
 */
public class OperationsPanel extends JPanel implements ActionListener {

    private JLabel mergeTypeLabel;
    private JComboBox<String> mergeAlgorithmSelect;
    private JLabel formatOutputLabel;
    private JComboBox<String> formatOutputSelect;
    private JLabel namingConventionLabel;
    private JComboBox<String> namingConventionSelect;
    private JLabel fittingMethodLabel;
    private JComboBox<String> fittingMethodSelect;
    private JButton mergeButton;
    private NewNamesPanel myNewNamesPanel;
    private KeepNamesPanel myKeepNamesPanel;
    private JButton saveButton;
    private JButton discardButton;

    private MyGraphicalUserInterface delegate;
    public void setDelegate(MyGraphicalUserInterface delegate) {
        this.delegate = delegate;
    }

    public OperationsPanel(){
        String[] mergeVariants = new String[MergeVariant.values().length];
        int i=0;
        for(MergeVariant variant : MergeVariant.values()){
            mergeVariants[i++] = variant.getName();
        }

        String[] fitMethod = new String[FittingMethod.values().length];
        i=0;
        for(FittingMethod variant : FittingMethod.values()){
            fitMethod[i++] = variant.getName();
        }

        String[] namingConventions = {"Select...", "Keep names from directory", "Generate new names"};
        String[] formatOptions = {"JPG", "PNG", "JPEG", "BMP", "TIF", "TIFF"};

        this.setLayout(new GridBagLayout());
        GridBagConstraints constraints = new GridBagConstraints();
        constraints.ipadx = 5;
        constraints.ipady = 3;

        this.mergeTypeLabel = new JLabel("Choose merge type");
        this.mergeTypeLabel.setHorizontalAlignment(JLabel.LEFT);
        this.mergeTypeLabel.setFont(GUIConstants.appFont);
        this.mergeTypeLabel.setPreferredSize(GUIConstants.OperationPanelWideLabel);
        this.mergeTypeLabel.setMinimumSize(GUIConstants.OperationPanelWideLabel);
        constraints.gridy = 0;
        constraints.gridx = 0;
        constraints.ipadx = 10;
        constraints.gridwidth = 2;
        this.add(this.mergeTypeLabel, constraints);

        this.mergeAlgorithmSelect = new JComboBox<>(mergeVariants);
        this.mergeAlgorithmSelect.setMinimumSize(GUIConstants.ComboBoxDimension);
        this.mergeAlgorithmSelect.setPreferredSize(GUIConstants.ComboBoxDimension);
        constraints.gridy = 1;
        constraints.ipadx = 5;
        this.add(this.mergeAlgorithmSelect,constraints);

        this.formatOutputLabel = new JLabel("Choose output format");
        this.formatOutputLabel.setHorizontalAlignment(JLabel.LEFT);
        this.formatOutputLabel.setFont(GUIConstants.appFont);
        this.formatOutputLabel.setPreferredSize(GUIConstants.OperationPanelWideLabel);
        this.formatOutputLabel.setMinimumSize(GUIConstants.OperationPanelWideLabel);
        constraints.gridy = 2;
        this.add(this.formatOutputLabel, constraints);

        this.formatOutputSelect = new JComboBox<>(formatOptions);
        this.formatOutputSelect.setMinimumSize(GUIConstants.ComboBoxDimension);
        this.formatOutputSelect.setPreferredSize(GUIConstants.ComboBoxDimension);
        constraints.gridy = 3;
        constraints.ipadx = 5;
        this.add(this.formatOutputSelect,constraints);

        this.fittingMethodLabel = new JLabel("Choose fitting method");
        this.fittingMethodLabel.setHorizontalAlignment(JLabel.LEFT);
        this.fittingMethodLabel.setFont(GUIConstants.appFont);
        this.fittingMethodLabel.setPreferredSize(GUIConstants.OperationPanelWideLabel);
        this.fittingMethodLabel.setMinimumSize(GUIConstants.OperationPanelWideLabel);
        constraints.gridy = 4;
        this.add(this.fittingMethodLabel, constraints);

        this.fittingMethodSelect = new JComboBox<>(fitMethod);
        this.fittingMethodSelect.setMinimumSize(GUIConstants.ComboBoxDimension);
        this.fittingMethodSelect.setPreferredSize(GUIConstants.ComboBoxDimension);
        constraints.gridy = 5;
        constraints.ipadx = 5;
        this.add(this.fittingMethodSelect,constraints);

        this.namingConventionLabel = new JLabel("Naming convention");
        this.namingConventionLabel.setFont(GUIConstants.appFont);
        this.namingConventionLabel.setPreferredSize(GUIConstants.OperationPanelWideLabel);
        this.namingConventionLabel.setMinimumSize(GUIConstants.OperationPanelWideLabel);
        constraints.gridy = 6;
        constraints.ipadx = 10;
        this.add(this.namingConventionLabel, constraints);

        this.namingConventionSelect = new JComboBox<>(namingConventions);
        this.namingConventionSelect.setMinimumSize(GUIConstants.ComboBoxDimension);
        this.namingConventionSelect.setPreferredSize(GUIConstants.ComboBoxDimension);
        this.namingConventionSelect.addActionListener(this);
        constraints.gridy = 7;
        constraints.ipadx = 5;
        this.add(this.namingConventionSelect, constraints);

        this.myNewNamesPanel = new NewNamesPanel();
        constraints.gridx = 0;
        constraints.gridy = 8;
        constraints.gridwidth = 2;
        constraints.gridheight = 4;
        this.add(this.myNewNamesPanel, constraints);
        this.myNewNamesPanel.setVisible(false);

        this.myKeepNamesPanel = new KeepNamesPanel();
        this.add(this.myKeepNamesPanel, constraints);
        this.myKeepNamesPanel.setVisible(false);

        this.mergeButton = new JButton("Merge");
        this.mergeButton.setFont(GUIConstants.appFont);
        this.mergeButton.setMinimumSize(GUIConstants.buttonDimension);
        this.mergeButton.setPreferredSize(GUIConstants.buttonDimension);
        this.mergeButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent arg0) {
				mergeButtonPressed();
				
			}
        });
        constraints.gridx = 1;
        constraints.gridy = 12;
        constraints.gridwidth = 1;
        this.add(this.mergeButton, constraints);

        this.saveButton = new JButton("Save");
        this.saveButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent arg0) {
				saveButtonPressed();
				
			}
        });
        this.saveButton.setFont(GUIConstants.appFont);
        this.saveButton.setMinimumSize(GUIConstants.buttonDimension);
        this.saveButton.setPreferredSize(GUIConstants.buttonDimension);
        constraints.gridx = 0;
        this.add(this.saveButton, constraints);
        this.saveButton.setVisible(false);

        this.discardButton = new JButton("Discard");
        this.discardButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent arg0) {
				discardButtonPressed();
				
			}
        });
        this.discardButton.setFont(GUIConstants.appFont);
        this.discardButton.setMinimumSize(GUIConstants.buttonDimension);
        this.discardButton.setPreferredSize(GUIConstants.buttonDimension);
        constraints.gridx = 1;
        this.add(this.discardButton, constraints);
        this.discardButton.setVisible(false);

        this.setMinimumSize(GUIConstants.OperationsPanelDimension);
        this.setPreferredSize(GUIConstants.OperationsPanelDimension);
    }

    /**
     * Called when the discard button is pressed.
     */
    private void discardButtonPressed() {
        this.delegate.handleDiscardButton();

    }

    /**
     * Called when the save button is pressed.
     */
    void saveButtonPressed(){
        this.delegate.handleSave();
    }

    /**
     * Called when the merge button is pressed. Assembles the merge preferences dto and then signals the MGUI a merge
     * has been requested.
     */
    public void mergeButtonPressed(){
        MergePreferencesDTO preferencesDTO = new MergePreferencesDTO();

        preferencesDTO.add(MergePreferencesDTOConstants.Algorithm, (String)this.mergeAlgorithmSelect.getSelectedItem());
        preferencesDTO.add(MergePreferencesDTOConstants.Naming, (String)this.namingConventionSelect.getSelectedItem());
        preferencesDTO.add(MergePreferencesDTOConstants.Format, (String)this.formatOutputSelect.getSelectedItem());
        preferencesDTO.add(MergePreferencesDTOConstants.FittingMethod, (String)this.fittingMethodSelect.getSelectedItem());

        try {
            if(preferencesDTO.get(MergePreferencesDTOConstants.Naming).equals(MergePreferencesDTOConstants.NAMING_CONVENTION_UNSELECTED)) {
                throw new NamingErrorException("Please choose a naming convention.");
            } else if(preferencesDTO.get(MergePreferencesDTOConstants.Naming).equals(MergePreferencesDTOConstants.NAMING_CONVENTION_GENERATE)){
                preferencesDTO.add(MergePreferencesDTOConstants.Base, this.myNewNamesPanel.getBaseName());
                preferencesDTO.add(MergePreferencesDTOConstants.Digits, this.myNewNamesPanel.getDigitsCount());
                preferencesDTO.add(MergePreferencesDTOConstants.Step, this.myNewNamesPanel.getCounterStep());
                preferencesDTO.add(MergePreferencesDTOConstants.Start, this.myNewNamesPanel.getCounterStart());
            } else {
                preferencesDTO.add(MergePreferencesDTOConstants.Directory, this.myKeepNamesPanel.getSelectedDirectory());
            }
            this.delegate.handleMergeRequest(preferencesDTO);
        } catch (NamingErrorException nee) {
            final JPanel panel = new JPanel();
            JOptionPane.showMessageDialog(panel, nee.getMessage(), "Error", JOptionPane.ERROR_MESSAGE);
        }


    }

    /**
     * Change the appearance of the panel wrt the naming convention.
     * @param namingConvention the naming convention we have
     */
    private void updateOperationsPanel(String namingConvention){
        switch (namingConvention) {
            case MergePreferencesDTOConstants.NAMING_CONVENTION_UNSELECTED:
                this.myKeepNamesPanel.setVisible(false);
                this.myNewNamesPanel.setVisible(false);
                break;
            case MergePreferencesDTOConstants.NAMING_CONVENTION_KEEP_NAMES:
                this.myNewNamesPanel.setVisible(false);
                this.myKeepNamesPanel.setVisible(true);
                break;
            default:
                this.myKeepNamesPanel.setVisible(false);
                this.myNewNamesPanel.setVisible(true);
                break;
        }
    }

    /**
     * Called when the naming convention comboBox is changed, since we listen to it.
     * @param event the event that triggered the call.
     */
    public void actionPerformed(ActionEvent event) {
        JComboBox comboBox = (JComboBox)event.getSource();
        String selectedValue = (String)comboBox.getSelectedItem();
        this.updateOperationsPanel(selectedValue);
    }

    /**
     * Return the output format of the selected type
     * @return OutputFormat enum value
     */
    public OutputFormat getOutputFormat() {
        return OutputFormat.valueOf((String)this.formatOutputSelect.getSelectedItem());
    }

    /**
     * Change the way the panel looks depending on whether we are viewing merge results or not.
     * @param isViewingMergeResults true if we are viewing merge, false otherwise.
     */
    public void morphForMergeResults(Boolean isViewingMergeResults) {
        if(isViewingMergeResults) {
            this.mergeButton.setVisible(false);

            this.saveButton.setVisible(true);
            this.discardButton.setVisible(true);
        } else {
            this.mergeButton.setVisible(true);

            this.saveButton.setVisible(false);
            this.discardButton.setVisible(false);
        }
    }
}
