package ro.ubb.avproc.model;

import lombok.Data;

@Data
public class SeparatedImageYUV {

    private Double[][] yComponents;
    private Double[][] uComponents;
    private Double[][] vComponents;
    private int height;
    private int width;

    public SeparatedImageYUV(int height, int width) {
        this.height = height;
        this.width = width;
        this.yComponents = new Double[height][width];
        this.uComponents = new Double[height][width];
        this.vComponents = new Double[height][width];
    }

    public SeparatedImageYUV(ImageYUV imageYUV) {
        int width = imageYUV.getWidth();
        int height = imageYUV.getHeight();

        this.height = height;
        this.width = width;

        this.yComponents = new Double[height][width];
        this.uComponents = new Double[height][width];
        this.vComponents = new Double[height][width];

        for (int currentLine = 0; currentLine < height; currentLine++) {
            for (int currentColumn = 0; currentColumn < width; currentColumn++) {
                this.yComponents[currentLine][currentColumn] = imageYUV.getPixel(currentLine, currentColumn).getYChannel();
                this.uComponents[currentLine][currentColumn] = imageYUV.getPixel(currentLine, currentColumn).getUChannel();
                this.vComponents[currentLine][currentColumn] = imageYUV.getPixel(currentLine, currentColumn).getVChannel();
            }
        }
    }
}
