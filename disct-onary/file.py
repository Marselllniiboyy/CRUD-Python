import os

def menuUtama(listMahasiswa):
    os.system('cls')
    sambutan = """
Selamat datang di Sistem Akademik Mahasiswa
    
Pilihan Menu:
1. Tampilkan List Mahasiswa
2. Tambah Mahasiswa
3. Hapus Mahasiswa
4. Keluar
    """
    print(sambutan)
    
    pilihanUser = int(input('Pilih Menu: '))
    
    if(pilihanUser == 1):
        showListMahasiswa(listMahasiswa)
    if(pilihanUser == 2):
        tambahMahasiswa(listMahasiswa)
    if(pilihanUser == 3):
        hapusMahasiswa(listMahasiswa)

def showListMahasiswa(listMahasiswa):
    print('ini menu list show mahasiswa')
    for index, i in enumerate(listMahasiswa):
        print(f"""
              ------------------------
              Index: {index}
              Nama Mahasiswa: {i['name']}
              Umur : {i['umur']}
              Prodi: {i['prodi']}
              ------------------------
              """)
        
    inputUser = int(input('Apakah ingin kembali ke Menu Utama? 1.Ya / 2.Tidak : '))
    if (inputUser == 1):
        menuUtama(listMahasiswa)
    
def tambahMahasiswa(listMahasiswa):
    dMB = {}
    dMB['name'] = str(input('Input Nama Mahasiswa: '))
    dMB['umur'] = int(input('Input Umur Mahasiswa: '))
    dMB['prodi'] = str(input('Input Prodi Mahasiswa: '))
    
    listMahasiswa.append(dMB)
    print('Data Mahasiswa Berhasil di Tambah!!')
    
    inputUser = int(input('Apakah ingin kembali ke Menu Utama? 1.Ya / 2.Tidak : '))
    if (inputUser == 1):
        menuUtama(listMahasiswa)
      
def hapusMahasiswa(listMahasiswa):
    print('ini menu hapus mahasiswa')
    for index, i in enumerate(listMahasiswa):
        print(f"""
              ------------------------
              Index: {index}
              Nama Mahasiswa: {i['name']}
              Umur : {i['umur']}
              Prodi: {i['prodi']}
              ------------------------
              """)
    pilihIndexMahasiswa = int(input('Input Index Mahasiswa: '))
    del(listMahasiswa[pilihIndexMahasiswa])
    print('Data Mahasiswa Berhasil di Hapus!!')
    
    inputUser = int(input('Apakah ingin kembali ke Menu Utama? 1.Ya / 2.Tidak : '))
    if (inputUser == 1):
        menuUtama(listMahasiswa)


def main():
    listMahasiswa = []

    DictMahasiswa = {
        'name': 'Budi',
        'umur': 20,
        'prodi': 'Sistem Informasi'
        }

    listMahasiswa.append(DictMahasiswa)

    DictMahasiswa = {
        'name': 'Asep',
        'umur': 21,
        'prodi': 'Ilmu Komputer'
        }

    listMahasiswa.append(DictMahasiswa)
    menuUtama(listMahasiswa)

main()



