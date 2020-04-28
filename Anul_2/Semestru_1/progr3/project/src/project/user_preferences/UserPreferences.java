package project.user_preferences;


import java.io.*;

/**
 * Class to handle saving the selected directories.
 */
public class UserPreferences {
    private File directory1;
    private File directory2;
    private final String fileName = "UserPreferences.txt";

    public final static UserPreferences INSTANCE = new UserPreferences();

    private UserPreferences() {}

    public void updateDirectory1(File newDirectory) {
        this.directory1 = newDirectory;
    }

    public void updateDirectory2(File newDirectory) {
        this.directory2 = newDirectory;
    }

    public void discardDirectory1(){
        this.directory1 = null;
    }

    public void discardDirectory2() {
        this.directory2 = null;
    }

    public File getDirectory1() {
        return this.directory1;
    }

    public File getDirectory2() {
        return this.directory2;
    }


    /**
     * Loads user preferences from file, if existent.
     */
    public void loadFromFile(){
        try {

            String lineRead;

            FileReader fileReader = new FileReader(this.fileName);
            BufferedReader reader = new BufferedReader(fileReader);

            while((lineRead = reader.readLine()) != null) {
                if (lineRead.startsWith("Directory1:")){
                    String filePath = lineRead.substring(11, lineRead.length());
                    this.directory1 = new File(filePath);
                } else {
                    String filePath = lineRead.substring(11, lineRead.length());
                    this.directory2 = new File(filePath);
                }
            }

            reader.close();

        } catch (FileNotFoundException ex) {
            // Do nothing
        } catch (IOException ex){
            ex.printStackTrace();
        }
    }

    /**
     * Export preferences to file when user exits the app.
     */
    public void dumpToFile(){
        try{
            FileWriter writer = new FileWriter(fileName);
            BufferedWriter bw = new BufferedWriter(writer);
            PrintWriter out = new PrintWriter(bw);

            if(this.directory1 != null) {
                out.println("Directory1:" + this.directory1.getAbsolutePath());
            }

            if(this.directory2 != null) {
                out.println("Directory2:" + this.directory2.getAbsolutePath());
            }

            out.close();
            bw.close();
            writer.close();
        }
        catch (IOException ex){
            ex.printStackTrace();
        }
    }
}
