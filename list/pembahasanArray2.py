# input user
# kondisi 1(+),2(-),3(*)


arr = []
step = int(input())
bilanganPertama = int(input())
BilanganKedua = int(input())
kondisi = int(input())

# bilangan 1 dan 2
arr.append(bilanganPertama)
arr.append(BilanganKedua)
print(f"{arr[0]} {arr[1]} ", end="")

# Fibonaci
for i in range(step):
  if kondisi == 1:
    print(f"{arr[-2] + arr[-1]} ", end="")
    arr.append(arr[-2] + arr[-1])
  elif kondisi == 2:
    print(f"{arr[-2] - arr[-1]} ", end="")
    arr.append(arr[-2] - arr[-1])
  elif kondisi == 3:
    print(f"{arr[-2] * arr[-1]} ", end="")
    arr.append(arr[-2] * arr[-1])

print("")
# aritmatika

for i in range((len(arr)+1) //2):
    if (i == (len(arr) - (i+1))):
      print(arr[i])
    else:
      if (kondisi == 1):
        print(f"{arr[i] + arr[-(i+1)]} ", end="")
      if (kondisi == 2):
        print(f"{arr[i] * arr[-(i+1)]} ", end="")
      if (kondisi == 3):
        print(f"{arr[i] * arr[-(i+1)]} ", end="")