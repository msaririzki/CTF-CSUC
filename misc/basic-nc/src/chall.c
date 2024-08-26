#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void encode(){
    puts("YmFzZWJhc2ViYXNlYmFzZWJhc2U2NG5paWNpa2Jvc3M=");
    fflush(stdout); // Tambahkan fflush setelah puts
}

int main(int argc, char const *argv[])
{
    char input[100];
    puts("This is key to input : ");
    fflush(stdout); // Tambahkan fflush setelah puts
    encode();
    puts("\n");
    fflush(stdout); // Tambahkan fflush setelah puts
    puts("!program just accept plain text answer (not encoded)");
    fflush(stdout); // Tambahkan fflush setelah puts
    puts("input key : ");
    fflush(stdout); // Tambahkan fflush setelah puts

    gets(input); // Pastikan untuk memberikan input saat nc
    if(strcmp(input, "basebasebasebasebase64niicikboss") == 0){
        puts("bener!!! this flag for you\n");
        fflush(stdout); // Tambahkan fflush setelah puts
        puts("CSUC{h1h111_r1bet_d1kit_g4_ngaruh}");
        fflush(stdout); // Tambahkan fflush setelah puts
    }else {
        puts("salah wkwkw");
        fflush(stdout); // Tambahkan fflush setelah puts
    }
    return 0;
}
