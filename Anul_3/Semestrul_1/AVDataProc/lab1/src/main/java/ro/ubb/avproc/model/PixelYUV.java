package ro.ubb.avproc.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PixelYUV {
    private Double yChannel;
    private Double uChannel;
    private Double vChannel;


    public PixelYUV(PixelRGB pixelRGB) {
        this.yChannel = 0.299 * pixelRGB.getRed() + 0.587 * pixelRGB.getGreen() + 0.114 * pixelRGB.getBlue();
        this.uChannel = 0.492 * (pixelRGB.getBlue() - this.yChannel);
        this.vChannel = 0.877 * (pixelRGB.getRed() - this.yChannel);
    }
}
