package ro.ubb.avproc.model;

import lombok.Data;

@Data
public class ImageYUV {

    private PixelYUV[][] pixels;
    private Integer height;
    private Integer width;

    public ImageYUV(ImageRGB imageRGB) {
        this.height = imageRGB.getHeight();
        this.width = imageRGB.getWidth();
        this.pixels = new PixelYUV[this.height][this.width];
        for (int currentLine = 0; currentLine < this.height; currentLine++) {
            for (int currentColumn = 0; currentColumn < this.width; currentColumn++) {
                this.pixels[currentLine][currentColumn] = new PixelYUV(imageRGB.getPixel(currentLine, currentColumn));
            }
        }
    }

    public ImageYUV(SeparatedImageYUV separatedImageYUV) {
        this.height = separatedImageYUV.getHeight();
        this.width = separatedImageYUV.getWidth();
        this.pixels = new PixelYUV[this.height][this.width];
        for (int currentLine = 0; currentLine < this.height; currentLine++) {
            for (int currentColumn = 0; currentColumn < this.width; currentColumn++) {
                this.pixels[currentLine][currentColumn] =
                        new PixelYUV(separatedImageYUV.getYComponents()[currentLine][currentColumn],
                                separatedImageYUV.getUComponents()[currentLine][currentColumn],
                                separatedImageYUV.getVComponents()[currentLine][currentColumn]);
            }
        }
    }

    public PixelYUV getPixel(int line, int column) {
        return this.pixels[line][column];
    }
}
