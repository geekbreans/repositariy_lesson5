from random import randint

with open("number.txt",'w', encoding = "utf-8") as n_file:
    n_list = [randint(1,100) for n in range(100)]
    n_file.write( " ".join(map(str, n_list)))
print (f'Сумма сгенерированных чисел ровна - {sum(n_list)}')


