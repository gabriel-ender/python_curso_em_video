from random import randint
n = (randint(0,10), randint(0,10), randint(0,10),
     randint(0,10), randint(0,10))
print(n)
print(f"O MENOR valor sorteado foi: {min(n)}")
print(f"O MAIOR valor sorteado foi: {max(n)}")
