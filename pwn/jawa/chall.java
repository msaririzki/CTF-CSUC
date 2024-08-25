import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
public class chall{
    public static Scanner scanner = new Scanner(System.in);
    public static int count = 0;
    public static String[] name = new String[100];

    public static void win(){
                try {
            File file = new File("flag.txt");
            Scanner fileScanner = new Scanner(file);
            System.out.println("Ini tuan Hadiah Untuk anda");
            while (fileScanner.hasNextLine()) {
                System.out.println(fileScanner.nextLine());
            }
            fileScanner.close();
        } catch (FileNotFoundException e) {
            System.err.println("Tuan, Sepertinya tidak ada file flag nya buat dulu ya file flag.txt nya");
        }
    }

    public static void create(){
        System.out.print("Enter Book Name : ");
        String bookName = scanner.nextLine();
        name[count] = bookName;
        count++;
        System.err.println("Sukses Book at " + (count) + " Position");
        if(count == 88){
            win();
        }        
    }   

    public static void read(){
        System.out.println("Book Data");
        for(int i = 0; i < count; i ++){
            System.out.println(i+1 + ". " + name[i]);
        }
    }

    public static void menu(){
        System.out.println("1.Fill Data");
        System.out.println("2.Read Data");
        System.out.println("3.Exit");
    }

    public static void main(String[] args) {
        while(true){
            System.out.println("Book Edition");
            menu();
            int pilihan = scanner.nextInt();
            scanner.nextLine();
            switch (pilihan) {
                case 1:
                    create();
                    break;
                case 2:
                    read();
                case 3:
                    return;
                default:
                    break;
            }
            
        }
    }
}