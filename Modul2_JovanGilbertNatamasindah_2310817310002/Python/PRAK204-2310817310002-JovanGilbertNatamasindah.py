print("\nketik \"h\" untuk horizontal dan ketik \"v\" untuk vertikal ")

JENIS = input("Masukkan jenis perhitungan : ")

if JENIS == "h" :

    Jari_jari, TINGGI = input("").split(" ")

    VOLUME = round (3.14 * int(Jari_jari) * int(Jari_jari) * int(TINGGI),2)
    LUAS = round ((2 * 3.14 * int(Jari_jari) * int(Jari_jari)) + (2 * 3.14 * int(Jari_jari) * int(TINGGI)),2)
    KELILING = round (2 * 3.14 * int(Jari_jari),2)

    print("Volume : ", VOLUME)
    print("Luas : ", LUAS)
    print("Keliling : ", KELILING)

elif JENIS == "v" :
    
    Jari_jari = input("")
    TINGGI = input("")

    VOLUME = round (3.14 * int(Jari_jari) * int(Jari_jari) * int(TINGGI),2)
    LUAS = round ((2 * 3.14 * int(Jari_jari) * int(Jari_jari)) + (2 * 3.14 * int(Jari_jari) * int(TINGGI)),2)
    KELILING = round (2 * 3.14 * int(Jari_jari),2)

    print("Volume :", VOLUME)
    print("Luas :", LUAS)
    print("Keliling :", KELILING)


    #terjadi error dimana pembulatan tidak sesuai dengan soal, yang diminta 2 angka belakang koma malah ada
    #yang cuma satu angka 