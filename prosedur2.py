def aritmatika(inputMenu,nama):#prosedur#mini program menggunakan prosedur, setelah itu tinggal di panggil
  if (inputMenu == 1) :
    print(f'ini beranda broo {nama}')
  if (inputMenu == 2) :
    print(f'ini Abot broo {nama}')
  if (inputMenu == 3) :
    print(f'ini help broo {nama}')

penampungArit= str(input('bagi,tambah,kurang,kali... ')).lower()

aritmatika(penampungArit)