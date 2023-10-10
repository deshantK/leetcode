import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class test {
    public static void main(String[] args) throws IOException{
        String inputFileName = "input.txt";
        FileReader fr = null
        try{
             fr = new FileReader(inputFileName);
        }
        catch (FileNotFoundException e)
        {
            System.out.println("File not found");
        }
        BufferedReader bufferedReader = new BufferedReader(fr);

        while ((line = bufferedReader.readLine()) != null ) {
            // Zeilen in Array speichern
            System.out.println(line);
        }
    



        // close the file
        fr.close();




    }




}
