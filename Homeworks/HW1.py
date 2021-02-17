for Number in range (1, 101):
  
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
           n=random.randint(1,101)
           

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '      ')
        matrix = [[0 for x in range(3)] for y in range(3)]

for i in range(3):
  for j in range(3):
    n=random.randint(1,101)
    matrix[i][j]=isPrime(n)

for i in range(len(matrix)):
  for j in range(len(matrix[i])):
    print(matrix[i][j],end='        ')
  print()
