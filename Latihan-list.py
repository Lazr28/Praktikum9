
Ldata = []
x = 0
while (True):
    nama = input("Nama : ")
    nim = input("Nim : ")
    nt = int(input("Nilai Tugas : "))
    nuts = int(input("Nilai UTS : "))
    nuas = int(input("Nilai UAS : "))
    nakhir = int(((nt / 100) * 30) + (nuts / 100 * 35) + (nuas / 100 * 35))
    Ldata.extend([nama, nim, nt, nuts, nuas, nakhir])
    tambah = input("Tambah data (y/t) : ")
    if (tambah == "t"):
        break
    elif (tambah != "y" and tambah != "t"):
        print("Isi yang benar!")
        tambah = input("Tambah data (y/t) : ")
        continue
print("=======================================================================================")
print("|   NO   |       NAMA       |      NIM       |    Tugas    |   UTS  |   UAS  |  Akhir |")
print("=======================================================================================")
for i in range(int(len(Ldata)/6)):
    print('|{0:^8}|{1:^18}|{2:^16}|{3:^13}|{4:^8}|{5:^8}|{6:^8}|'.format(
        i+1, Ldata[x], Ldata[1+x], Ldata[2+x], Ldata[3+x], Ldata[4+x], Ldata[5+x]))
    x += 6
print("=======================================================================================")
