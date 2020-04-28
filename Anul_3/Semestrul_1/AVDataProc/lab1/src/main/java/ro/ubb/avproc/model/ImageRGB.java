package ro.ubb.avproc.model;

import lombok.Data;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;

@Data
public class ImageRGB {

    private PixelRGB[][] pixels;
    private Integer height;
    private Integer width;
    private Integer maximumChannelValue;

    public ImageRGB(ImageYUV imageYUV) {
        this.width = imageYUV.getWidth();
        this.height = imageYUV.getHeight();
        this.pixels = new PixelRGB[this.height][this.width];
        for (int currentLine = 0; currentLine < this.height; currentLine++) {
            for (int currentColumn = 0; currentColumn < this.width; currentColumn++) {
                this.pixels[currentLine][currentColumn] = new PixelRGB(imageYUV.getPixel(currentLine, currentColumn));
            }
        }
    }

    public ImageRGB(File imageFile) throws IOException {
        Integer numberOfHeaderLinesRead = 0;
        String line;

        BufferedReader br = new BufferedReader(new FileReader(imageFile));

        while ((line = br.readLine()) != null) {
            if (!line.startsWith("#")) {
                numberOfHeaderLinesRead++;
            }

            switch (numberOfHeaderLinesRead) {
                case 0:
                    continue;
                case 1:
                    continue;
                case 2:
                    this.setHeightAndWidthFromFileLine(line);
                    continue;
                case 3:
                    this.maximumChannelValue = Integer.parseInt(line);
                    this.parsePixelRows(br);
                    break;
                default:
                    break;
            }
        }
    }

    public PixelRGB getPixel(int line, int column){
        return this.pixels[line][column];
    }

    private void parsePixelRows(BufferedReader br) throws IOException {
        for (int currentLine = 0; currentLine < this.height; currentLine++) {
            for (int currentColumn = 0; currentColumn < this.width; currentColumn++) {
                int redChannel = Integer.parseInt(br.readLine());
                int greenChannel = Integer.parseInt(br.readLine());
                int blueChannel = Integer.parseInt(br.readLine());
                this.pixels[currentLine][currentColumn] = new PixelRGB(redChannel, greenChannel, blueChannel);
            }
        }
    }

    private void setHeightAndWidthFromFileLine(String fileLine) {
        String[] components = fileLine.split(" ");
        this.width = Integer.parseInt(components[0]);
        this.height = Integer.parseInt(components[1]);
        this.pixels = new PixelRGB[this.height][this.width];
    }

}
