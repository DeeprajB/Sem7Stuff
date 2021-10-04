package Exp2;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import javax.swing.ImageIcon;

public class DisplayImage_GUI extends javax.swing.JFrame {

    public DisplayImage_GUI(){
        initComponents();
    }

    @SuppressWarnings("unchecked")

    private void jButtonActionPerformed(java.awt.event.ActionEvent evt) {
        BufferedImage image = null;
        File f = null;

        try{
            f= new File("./Exp2/image.jpg");
            image= ImageIO.read(f);
            ImageIcon icon = new ImageIcon(image);
            jLabel2.setIcon(icon);
        }
        catch(IOException e){
            System.out.println("Error: "+e);
        }
    }

    public static void main(String[] args) {
        
    }
}          