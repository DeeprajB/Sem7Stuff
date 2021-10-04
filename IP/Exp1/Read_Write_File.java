package Exp1;

import java.awt.image.BufferedImage;
import java.io.*;
import javax.imageio.ImageIO;

public class Read_Write_File {
    public static void main(String[] args) {
        int width = 963;
        int height = 640;
        BufferedImage image = null;
        File f = null;
        try {
            //Read Image
            f = new File("./Exp1/wallpaper.jpg");
            image = new BufferedImage(width,height,BufferedImage.TYPE_INT_ARGB);
            image = ImageIO.read(f);
            System.out.println("Reading Complete");
        }
        catch(IOException e){
            System.out.println("Error: "+e);
        }
        try {
            //Write Image
            f = new File("./Exp1/wallpaper_output.jpg");
            ImageIO.write(image,"jpg",f);
            System.out.println("Writing Complete");
        }
        catch(IOException e){
            System.out.println("Error: "+e);
        }
    }
}