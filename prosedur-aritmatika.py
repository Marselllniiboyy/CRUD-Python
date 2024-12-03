# angka1 = int(input("masukkan angka pertama.... "))
# angka2 = int(input("masukkan angka kedua... "))

# def aritmatika(kondisi):#prosedur#mini program menggunakan prosedur, setelah itu tinggal di panggil
#   if (kondisi == "plus") :
#     print(angka1+angka2)
#   if (kondisi == "minus"):
#     print(angka1-angka2)
#   if (kondisi == "kali"):
#     print(angka1*angka2)
#   if (kondisi == "bagi"):
#     print(angka1/angka2)

# penampungArit= str(input('bagi,tambah,kurang,kali... ')).lower()

def aritmatika(angka1,angka2,kondisi):#prosedur#mini program menggunakan prosedur, setelah itu tinggal di panggil
  if (kondisi == "+") :
    print(angka1+angka2)
  if (kondisi == "-"):
    print(angka1-angka2)
  if (kondisi == "*"):
    print(angka1*angka2)
  if (kondisi == "/"):
    print(angka1/angka2)


# def aritmatika(angka1,angka2):#prosedur#mini program menggunakan prosedur, setelah itu tinggal di panggil
#   hasilTambah= print(angka1+angka2)
#   hasilKurang = print(angka1-angka2)
#   hasilKali = print(angka1*angka2)
#   hasilBagi= print(angka1/angka2)
#   return hasilTambah,hasilKurang,hasilKali,hasilBagi

def sukaMusik():
  print("Kamu suka musik apa?")
  genres = [
        "Pop", 
        "Rock/Metal", 
        "Hip-Hop/Rap", 
        "Jazz/Blues/Soul", 
        "Klasik", 
        "EDM (Electronic Dance Music)", 
        "Country", 
        "Reggae", 
        "Indie", 
        "Dangdut/Koplo/Musik Tradisional"
    ]
  for i,genres in enumerate(genres, start=1):
    print(f"{i}. {genres}")

  pilihan = int(input("Masukkan nomor genre pilihanmu (1-10): "))
  print(f"keren pilihan kamu {genres[0]}")
  deskripsi = {
        "1": "Kamu optimis, ramah, dan suka mengekspresikan diri. Lagu-lagu ceria dan populer adalah favoritmu.",
        "2": "Kamu kreatif, emosional, dan mungkin sedikit pemberontak. Musik intens seperti rock atau metal cocok untukmu.",
        "3": "Kamu percaya diri, energik, dan suka bersosialisasi. Genre hip-hop atau rap menunjukkan semangat tinggi.",
        "4": "Kamu reflektif, tenang, dan sensitif. Kamu suka mendengarkan musik yang penuh emosi seperti jazz atau blues.",
        "5": "Kamu cerdas, introspektif, dan terorganisasi. Musik klasik menarik bagi orang yang menghargai keindahan.",
        "6": "Kamu berani, suka pesta, dan terbuka terhadap pengalaman baru. Musik EDM memicu semangatmu.",
        "7": "Kamu sederhana, tulus, dan berpikiran praktis. Lagu-lagu country yang emosional menjadi favoritmu.",
        "8": "Kamu santai, optimis, dan toleran. Musik reggae mencerminkan gaya hidup bebas dan damai.",
        "9": "Kamu mandiri, kreatif, dan unik. Musik indie menunjukkan jiwa orisinalitasmu.",
        "10": "Kamu ramah, humoris, dan bangga dengan budaya lokal. Musik dangdut atau tradisional mendekatkanmu dengan identitasmu."
    }
  
  # Menampilkan deskripsi berdasarkan input
  if pilihan in deskripsi:
    print(deskripsi[pilihan])
  else:
    print("Pilihanmu tidak tersedia. Silakan pilih kembali.")
  return 

def Menu():
  print("Pilih apa yang kamu mau tmapilin")
  print("input 1 untuk suka musik apa")
  print("input 2 Kalkulator")
  pilihan = int(input("masukkan pilihan... "))
  if (pilihan == 1):
    sukaMusik()
  elif (pilihan == 2):
    angka1 = int(input("masukkan angka pertama.... "))
    angka2 = int(input("masukkan angka kedua... "))
    kondisiArit= str(input('bagi,tambah,kurang,kali... ')).lower()
    aritmatika(angka1,angka2,kondisiArit)
  else:
    print("pilihan tidak tersedia")
    Menu()#panggil menu#mini program menggunakan prosedur, setelah itu tinggal
Menu()