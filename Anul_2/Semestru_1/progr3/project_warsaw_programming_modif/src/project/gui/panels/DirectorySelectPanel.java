package project.gui.panels;

import project.gui.GUIConstants;
import project.gui.MyGraphicalUserInterface;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.io.File;

/**
 * Extension of JPanel, creates the directory select area.
 */
public class DirectorySelectPanel extends JPanel {

	static private int instanceId = 1;
	private JLabel directoryLabel;
	private JLabel pathLabel;
	private JButton selectOrChangeButton;
	private JButton clearButton;
	private JLabel warningLabel;
	private MyGraphicalUserInterface delegate;

	/**
	 * Sets reference to the MGUI object that instantiated this object to signal
	 * changes.
	 * 
	 * @param delegate
	 *            the MGUI
	 */
	public void setDelegate(MyGraphicalUserInterface delegate) {
		this.delegate = delegate;
	}

	/**
	 * Initializer, places down all buttons.
	 */
	public DirectorySelectPanel() {
		this.setLayout(new GridBagLayout());

		GridBagConstraints constraints = new GridBagConstraints();
		constraints.ipadx = 5;
		constraints.ipady = 3;
		constraints.fill = GridBagConstraints.HORIZONTAL;

		this.directoryLabel = new JLabel("Directory "
				+ DirectorySelectPanel.instanceId++ + ":");
		this.directoryLabel.setFont(GUIConstants.appFont);
		this.directoryLabel
				.setPreferredSize(GUIConstants.prePathLabelDimension);
		this.directoryLabel.setMinimumSize(GUIConstants.prePathLabelDimension);
		constraints.gridx = 0;
		constraints.gridy = 0;
		this.add(this.directoryLabel, constraints);

		this.pathLabel = new JLabel("Not selected.");
		this.pathLabel.setFont(GUIConstants.appFont);
		this.pathLabel.setMinimumSize(GUIConstants.pathLabelDimension);
		this.pathLabel.setPreferredSize(GUIConstants.pathLabelDimension);
		this.pathLabel.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				requestViewingDirectoryChange();
			}
		});
		constraints.gridx = 1;
		constraints.gridwidth = 5;
		this.add(this.pathLabel, constraints);

		this.selectOrChangeButton = new JButton("Select");
		this.selectOrChangeButton.setFont(GUIConstants.appFont);
		this.selectOrChangeButton
				.setPreferredSize(GUIConstants.buttonDimension);
		this.selectOrChangeButton.setMinimumSize(GUIConstants.buttonDimension);
		constraints.gridx = 6;
		constraints.gridwidth = 1;
		this.add(this.selectOrChangeButton, constraints);

		this.selectOrChangeButton.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {
				selectOrChangeButtonPressed();

			}
		});

		this.clearButton = new JButton("Remove");
		this.clearButton.setFont(GUIConstants.appFont);
		this.clearButton.setPreferredSize(GUIConstants.buttonDimension);
		this.clearButton.setMinimumSize(GUIConstants.buttonDimension);
		this.clearButton.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				clearButtonPressed();
			}
		});
		constraints.gridx = 7;
		this.add(this.clearButton, constraints);

		this.warningLabel = new JLabel(
				"Warning! This directory has no images in it.");
		this.warningLabel.setPreferredSize(GUIConstants.warningLabelDimension);
		this.warningLabel.setMinimumSize(GUIConstants.warningLabelDimension);
		this.warningLabel.setFont(GUIConstants.warningLabelFont);
		constraints.gridx = 0;
		constraints.gridy = 1;
		constraints.gridwidth = 4;
		this.warningLabel.setVisible(false);
		this.add(this.warningLabel, constraints);

		this.setPreferredSize(GUIConstants.DirectorySelectPanelDimension);
		this.setMinimumSize(GUIConstants.DirectorySelectPanelDimension);
	}

	public void setSelectOrChangeButtonText(String text) {
		this.selectOrChangeButton.setText(text);
	}

	/**
	 * Called when clear button is pressed.
	 */
	void clearButtonPressed() {
		// TODO - inspect why it is not repainted.
		this.delegate.handleClearButtonPressed(this.directoryLabel.getText());
		this.setSelectOrChangeButtonText("Select");
		this.pathLabel.setText("Not selected");
	}

	/**
	 * Reaction of pressing directory select button
	 */
	void selectOrChangeButtonPressed() {

		/**
		 * Make sure that the user knows what he is doing, and only after that
		 * discard merge results
		 */
		int result = JOptionPane.NO_OPTION;
		if (this.delegate.userIsViewingMergeResults()) {
			result = JOptionPane
					.showConfirmDialog(
							null,
							"All merge progress will be lost. Do you wish to continue?",
							"Warning", JOptionPane.YES_NO_OPTION);
		}

		if (!this.delegate.userIsViewingMergeResults()
				|| result == JOptionPane.YES_OPTION) {
			// This is what happens on button press.

			this.setSelectOrChangeButtonText("Change");

			String pathName = null;

			if (System.getProperty("os.name").toLowerCase().contains("mac")) {

				JFrame frame = new JFrame("Select a Directory");
				FileDialog fd = new FileDialog(frame, "Choose a directory",
						FileDialog.LOAD);
				fd.setDirectory("");
				fd.setVisible(true);
				String filename2 = fd.getDirectory();
				if (filename2 != null) {
					pathName = fd.getDirectory() + fd.getFile();
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

			if (pathName != null) {
				File myDir = new File(pathName);
				this.setFilePath(pathName);
				this.delegate.filePathChanged(myDir,
						this.directoryLabel.getText());
				this.delegate.setUserIsViewingMergeResults(false);
			}

		}

	}

	/**
	 * Sets the displayed path name
	 * 
	 * @param pathName
	 *            the path of the current directory
	 */
	public void setFilePath(String pathName) {
		this.pathLabel.setText("..."
				+ pathName.substring(pathName.length() / 2, pathName.length()));
	}

	/**
	 * Tells the panel to display a warning saying that the directory is empty.
	 * 
	 * @param shouldDisplay
	 *            boolean.
	 */
	public void displayAlert(Boolean shouldDisplay) {
		this.warningLabel.setVisible(shouldDisplay);
	}

	/**
	 * Handles clicking on a directory to view it.
	 */
	void requestViewingDirectoryChange() {

		int result = JOptionPane.NO_OPTION;

		if (this.delegate.userIsViewingMergeResults()) {
			result = JOptionPane
					.showConfirmDialog(
							null,
							"All merge progress will be lost. Do you wish to continue?",
							"Warning", JOptionPane.YES_NO_OPTION);
		}

		if (!this.delegate.userIsViewingMergeResults()
				|| result == JOptionPane.YES_OPTION) {
			this.delegate.displayDirectory(this.directoryLabel.getText());
			this.delegate.setUserIsViewingMergeResults(false);
		}
	}
}
