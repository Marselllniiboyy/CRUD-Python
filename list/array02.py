def buatDeret(step,suku1,suku2,kondisi):
  if step <= 0:
    return None
  else:
    suku_list = [suku1, suku2]
    while len(suku_list) < step + 2:
      if kondisi == 1:
        suku_baru = suku_list[-2] + suku_list[-1]
      elif kondisi == 2:
        suku_baru = suku_list[-2] - suku_list[-1]
      elif kondisi == 3:
        suku_baru = suku_list[-2] * suku_list[-1]
      suku_list.append(suku_baru)
    return suku_list


def kondisiartimatika(sukuList,kondisi):
  hasil = []
  n = len(sukuList)
  for i in range(n // 2):
    if kondisi == 1 :
      hasil.append(sukuList[i] + sukuList[n - i - 1])
    if kondisi == 2 :
      hasil.append(sukuList[i] - sukuList[n - i - 1])
    if kondisi == 3 :
      hasil.append(sukuList[i] * sukuList[n - i - 1])
  if n % 2 != 0:
    hasil.append(sukuList[n // 2])
  return hasil

def main():
  step = int(input())
  suku1 = int(input())
  suku2 = int(input())
  kondisi = int(input())

  deret = buatDeret(step,suku1,suku2,kondisi)
  if deret == None:
    print("Undefined")
    return
  print(*deret)
  aritmatika = kondisiartimatika(deret,kondisi)
  print(*aritmatika)
main()