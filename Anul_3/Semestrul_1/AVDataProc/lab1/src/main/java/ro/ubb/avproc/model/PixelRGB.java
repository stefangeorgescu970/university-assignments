package ro.ubb.avproc.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import static jdk.nashorn.internal.objects.NativeMath.min;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PixelRGB {

    private Integer red;
    private Integer green;
    private Integer blue;


    public PixelRGB(PixelYUV pixelYUV) {
        this.red = (int) Math.max(0, Math.min(255, (pixelYUV.getYChannel() + 1.140 * pixelYUV.getVChannel())));
        this.green = (int) Math.max(0, Math.min(255, (pixelYUV.getYChannel() - 0.395 * pixelYUV.getUChannel() - 0.581 * pixelYUV.getVChannel())));
        this.blue = (int) Math.max(0, Math.min(255, (pixelYUV.getYChannel() + 2.032 * pixelYUV.getUChannel())));
    }

}
