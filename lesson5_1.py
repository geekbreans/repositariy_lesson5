
n_value = "__"
while len(n_value) != 0:
    n_value = input('Введите слово для записи в файл out_file.txt, или ничего для окончания записи ')
    out_f = open("out_file.txt", "a")
    out_f.writelines(n_value + '\n')
    out_f.close()

