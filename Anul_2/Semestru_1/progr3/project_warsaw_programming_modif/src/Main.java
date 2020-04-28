import project.gui.MyGraphicalUserInterface;

public class Main {


    public static void main(String[] args) {

        if(System.getProperty("os.name").toLowerCase().contains("mac")) {
            System.setProperty("apple.awt.fileDialogForDirectories", "true"); // to be able to choose directory.
        }

        MyGraphicalUserInterface myGUI = new MyGraphicalUserInterface();

    }
}
