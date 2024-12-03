# Masuk Input
step = int(input())
angka1 = int(input())
angka2 = int(input())
next_angka = 0
penampung = [angka1,angka2]

if (step < 1 ):
  print("Undefined")
else:
  print(angka1,angka2,end=" ")
  for x in range(0, step):
    next_angka = angka1 + angka2
    angka1 = angka2
    angka2 = next_angka
    penampung.append(next_angka)
    print(angka2,end=" ")

  print()
  while len(penampung) > 1:
    summation = penampung[0] + penampung[-1]
    penampung.pop(0)
    penampung.pop(-1)
    print(summation,end=" ")

  if len(penampung) == 1:
    print(penampung[0])