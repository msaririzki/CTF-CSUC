#include<string.h>
#include<stdio.h>

void win(void){
    FILE *file;
    int ch;

    puts("Welcome tamu spesial! How tough are you?");
    puts("Dengan datangnya tamu spesial seperti tuan, kami akan menghidangkan menu spesial kami. Mohon tunggu sebentar, tuan!");
    

    file = fopen("flag.txt", "r");
    if (file == NULL) {
        puts("Waduh, ternyata menu spesial kami lagi kosong. Mohon maaf, tuan.");
        exit(1);
    }

    puts("Terima kasih sudah menunggu. Selamat menikmati menu spesial kami, tuan.");

    while ((ch = fgetc(file)) != EOF) {
        putchar(ch);
    }

    fclose(file);
    puts("\nTerima kasih atas kunjungannya. Mampir lagi ya, tuan!");
}

int main()
{
    char c[10];
    int dek = 0xdeadbeef;
        puts("=============");
        puts("||Anyanayny||");
        puts("=============");
    printf("Anyaaaa ~_~ >> ");
    gets(c);
    printf("dek : %lx", dek);
    if(dek == 0xdeadc0de){
        puts("\nwinn!");
        win();
    }
    puts("\n");
    return 0;
}