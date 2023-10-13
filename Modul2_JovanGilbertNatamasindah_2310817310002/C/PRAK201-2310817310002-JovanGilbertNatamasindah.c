#include <stdio.h>

void main () {
    char NAMA[30];
    char NIM[30];
    char KELAS_PARALEL[30];
    char TEMPAT_LAHIR[30];
    char TANGGAL_LAHIR[30];
    char ALAMAT[30];
    char HOBBY[30];
    char NO_HP[30];


    printf("Nama : ");
    gets(NAMA);

    printf("NIM : ");
    gets(NIM);

    printf("Kelas Paralel : ");
    gets(KELAS_PARALEL);

    printf("Tempat Lahir : ");
    gets(TEMPAT_LAHIR);

    printf("Tanggal Lahir : ");
    gets(TANGGAL_LAHIR);

    printf("Alamat : ");
    gets(ALAMAT);

    printf("Hobby : ");
    gets(HOBBY);

    printf("No.HP : ");
    gets(NO_HP);
    
printf("\n\n");

    printf("Nama : %s\n", NAMA);
    printf("NIM : %s\n", NIM );
    printf("Kelas Paralel : %s\n", KELAS_PARALEL );
    printf("Tempat/Tanggal Lahir : %s/%s \n", TEMPAT_LAHIR, TANGGAL_LAHIR);
    printf("Alamat : %s\n", ALAMAT );
    printf("Hobby : %s\n", HOBBY );
    printf("No.HP : %s\n", NO_HP );

}