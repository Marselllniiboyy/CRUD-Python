# refrens bukan pakai index(0,1,2,3,) tapi pakai key tertentu
# index bisa di costom
# dataOrang = ["Jokowi", 50, "Jakarta", "Pria", "membangun kekuasaan"]
# dataJokowi = {"nama":dataOrang[0], "umur":dataOrang[1], "asal":dataOrang[2], "gender":dataOrang[3], "hobi": dataOrang[4]}

# dataMahasisswa = {"nama": "Marsel", "age":20, "hobi": "bermain game", "prodi":"SI"}
# dataMahasisswa2 = {"nama": "jono", "age":10, "hobi": "bermain game", "prodi":"Ilkom"}
# list = [dataMahasisswa,dataMahasisswa2]
# print(list)
def menuUtama():
  print("Selamat datang di domain mahasisswaa")
  print("Pilih menu")
  print("1. Tampilkan Mahasisswa")
  print("2. Tambah Mahasisswa")
  print("3. Hapus Mahasisswa")

def tampilkanMahasisswa(listMahasisswa):
  print("Tampil Mahasiswa")
  for i in listMahasisswa:
    print(i)
  
  inputUser = int(input("Apakah ingin kembali ke menu? 1. Ya 2. Tidak: "))

def tambahMahasisswa(lis):
  print("Tambah Mahasisswa")
  nama = input("Nama: ")
  umur = input("Umur: ")
  hobi = input("Hobi: ")
  prodi = input("Prodi: ")
  dataMahasiswa = {"nama":nama, "umur":umur, "hobi":hobi, "prodi":prodi}
def hapusMahasisswa():
  print("Hapus")

def main():
  menuUtama()
  listMahasiswa =[]
  dictMahasiswa = {"nama": "Marsel", "age":20, "prodi": "SI", "Hobi":"Makan"}

  dictMahasiswa2 = {
    "nama": "Budi",
    "umur": 30,
    "Prodi": "Ilkom",
    "Hobi": "Tidur"
  }

  listMahasiswa.append(dictMahasiswa)
  listMahasiswa.append(dictMahasiswa2)

  userInput = int(input("Pilih menu: "))
  if userInput == 1:
    tampilkanMahasisswa(listMahasiswa)
  if userInput == 2:
    tambahMahasisswa()
  if userInput == 3:
    hapusMahasisswa()
main()