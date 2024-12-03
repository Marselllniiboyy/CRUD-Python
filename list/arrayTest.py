step = int(input())
suku1 = int(input())
suku2 = int(input())

if step <= 0:
    print('Undefined')
else:
    suku_list = [suku1, suku2]
    while len(suku_list) < step + 2:
      suku_baru = suku_list[-2] + suku_list[-1]
      suku_list.append(suku_baru)
    print(*suku_list)
    result = []
    n = len(suku_list)
    for i in range(n // 2):
      result.append(suku_list[i] + suku_list[n - i - 1])
    if n % 2 != 0:
      result.append(suku_list[n // 2])
    print(*result)