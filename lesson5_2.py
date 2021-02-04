with open("text_2.txt",'r', encoding='utf-8') as f_object:
    n_value = 0
    w_value = 0
    for line in f_object:
        n_value = n_value + 1
        w_value = w_value + len(line.split())
        print(f'{n_value + 1} колисество слов {len(line.split())}, строка - {line}', end="")

    print("\n",f'Всего слов {w_value}')
    print(f'Всего строк {n_value}')

print( f"-----------------------------------------------------")
with open("text_2.txt",'r', encoding='utf-8') as f_object:
    my_list = [f'{n_value} строка, {" ".join(w_value.split())} -имеет слов {len(w_value.split())}' for n_value, w_value in enumerate(f_object, 1)]
    print(*my_list, f'Всего строк - {len(my_list)}', sep="\n")

