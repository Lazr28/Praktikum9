# List dan Tuple
Tugas membuat program menambahkan data kedalam sebuah list.

### Code :
```python
Ldata = []
x = 0
while True:
    nama = input("Nama    : ")
    nim =  input("Nim     : ")
    nt =   int(input("Nilai Tugas : "))
    nuts = int(input("Nilai UTS   : "))
    nuas = int(input("Nilai UAS   : "))
    nakhir = (nt / 100) * 30 + (nuts / 100 * 35) + (nuas / 100 * 35)
    Ldata.extend([nama, nim, nt, nuts, nuas, nakhir])
    tambah = input("Tambah data (y/t) : ")

    if (tambah == "t"):
        break
    elif (tambah == "y" ):

        continue

print("===================================================================================")
print("|  NO  |       NAMA       |      NIM       |   Tugas   |   UTS  |   UAS  |  Akhir |")
print("===================================================================================")
for i in range(int(len(Ldata)/6)):
    print('|{0:^6}| {1:17}| {2:14} | {3:>9} |{4:^8}|{5:^8}|{6:^7.2f}|'.format(
        i+1, Ldata[x], Ldata[1+x], Ldata[2+x], Ldata[3+x], Ldata[4+x], Ldata[5+x]))
    x += 6
print("===================================================================================")
```
>**Penjelasan :**\
pertama tama kita deklarasikan list kosong dengan sintaks berikut :\
`Ldata = []`\
dan variabel `x = 0` untuk kita gunakan pada _for Looping_\
\
Buat while loop untuk menjalakan perintah pada pertama kali dengan kondisi true, 
agar dapat langsung berjalan dan bisa terus menerus sebelum kita berikan perintah break.\
`while True:`\
\
Buat variabel yang akan menampung inputan user ( Nama, Nim, Nilai Tugas, UTS, UAS, Nilai Akhir)\
`nama = input("Nama    : ")`\
    `nim =  input("Nim     : ")`\
    `nt =   int(input("Nilai Tugas : "))`\
    `nuts = int(input("Nilai UTS   : "))`\
    `nuas = int(input("Nilai UAS   : "))`\
\
Setelah itu jumlahkan nilai-nilai untuk nilai akhir dengan ketentuan (tugas : 30%, uts : 35%, uas : 35%)\
\
lalu masukan data data diatas kedalam list dengan sintaks :\
` Ldata.extend([nama, nim, nt, nuts, nuas, nakhir])`\
\
Tanyakan kepada user, apakah akan menambahkan data lagi.\
lalu gunakan if elif untuk jawabannya\
`tambah = input("Tambah data (y/t) : ")`\
\
    `if (tambah == "t"):`\
    `    break`\
    `elif (tambah == "y"):`\
    `    continue`\
jika user menjawab "t", maka while looping akan berhenti dan akan menjalankan perintah diluar while ( setelah while ).\
tetapi jika user menjawab selain "y" while looping akan dijalankan kembali.\
setelah itu kita buat `print` untuk menampilkan data yang sudah di inputkan\
gunakan for looping untuk menampilkan seluruh data.\
\
`for i range ( jumlah data didalam list / 6 ) # 6 ( Nama, NIM, Tugas,UTS,UAS,Akhir).`\
agar kita dapat mengulang semua data sesuai dengan urutannya
\
setelah itu kita buat print datanya dan di formating agar data lebih rapih.\
setelah itu kita tambah variabel x 6 agar dapat mengambil data selanjutnya pada looping setelah ini.


--
### Output : 
![Output](/Screenshot/Output.png)
