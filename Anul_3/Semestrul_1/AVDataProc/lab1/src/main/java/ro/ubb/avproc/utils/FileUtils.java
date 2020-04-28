package ro.ubb.avproc.utils;

import ro.ubb.avproc.model.ImageRGB;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;

public class FileUtils {

//    private static String resPath = "/Users/Stefan/Documents/Facultate/codeOnly/Anul_3/Semestrul_1/AVDataProc/lab1/src/main/resources/";
    private static String resPath = "/Users/stefangeorgescu/University/codeOnly/Anul_3/Semestrul_1/AVDataProc/lab1/src/main/resources/";

    public static ImageRGB readImageFromFile(String fileName) throws IOException {
        return new ImageRGB(new File(resPath + fileName));
    }

    public static void dumpImageToFile(ImageRGB imageRGB, String fileName) throws  IOException {
        PrintWriter writer = new PrintWriter(resPath + fileName);
        writer.println("P3");
        writer.println("# CREATOR: GIMP PNM Filter Version 1.1. Altered by Stefan Georgescu");
        writer.println(imageRGB.getWidth() + " " + imageRGB.getHeight());
        writer.println(imageRGB.getMaximumChannelValue());

        for (int currentLine = 0; currentLine < imageRGB.getHeight(); currentLine++) {
            for (int currentColumn = 0; currentColumn < imageRGB.getWidth(); currentColumn++) {
                writer.println(imageRGB.getPixel(currentLine, currentColumn).getRed());
                writer.println(imageRGB.getPixel(currentLine, currentColumn).getGreen());
                writer.println(imageRGB.getPixel(currentLine, currentColumn).getBlue());
            }
        }

        writer.close();
    }

}
