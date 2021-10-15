import java.awt.image.BufferedImage;
import java.io.*;
import java.awt.*;
import javax.imageio.ImageIO;

public class Grayscale_Image {
    public static void main(String[] args) {
        int width = 1920;
        int height = 1080;
        BufferedImage image = null;
        File f = null;
        File f1 = null;
        try {
            //Read Image
            f = new File("/run/media/deeprajb/HDD/Important Photos/Wallpapers/wallpaperflare.com_wallpaper3.jpg");
            image = new BufferedImage(width,height,BufferedImage.TYPE_INT_ARGB);
            image = ImageIO.read(f);
            System.out.println("Reading Complete");
        }
        catch(IOException e){
            System.out.println("Error: "+e);
        }
        try {
            //Write Image
            f1 = new File("./java_grayscale_output.jpg");
            for (int i = 0; i < height; i++) {
                for (int j = 0; j < width; j++) {
                    Color c = new Color(image.getRGB(j, i));
                    int red = (int)(c.getRed() * 0.299);
                    int green = (int)(c.getGreen() * 0.587);
                    int blue = (int)(c.getBlue() * 0.114);
                    Color newColor = new Color(red + green + blue, red + green + blue, red + green + blue);
                    image.setRGB(j, i, newColor.getRGB());
                }
            }
            ImageIO.write(image,"jpg",f1);
            System.out.println("Writing Complete");
        }
        catch(IOException e){
            System.out.println("Error: "+e);
        }
    }


}