with open("text_3.txt", 'r', encoding='utf-8') as f_object:
    n_value = 0
    s_value = 0
    for line in f_object:
        n_value = n_value + 1
        w_list = line.split()
        s_value = s_value + float(w_list[1])
        if float(w_list[1]) < 20000:
            print(w_list[0])
    if n_value > 0:
        s_value = s_value / n_value
    print(f'Средняя зарплата по сотрудника {s_value}')
print( f"-----------------------------------------------------")
with open("text_3.txt", 'r', encoding='utf-8') as f_object:
    worker_diction = { line.split()[0]:float(line.split()[1]) for line in f_object}
    print(f'Средняя зарплата равна - {sum(worker_diction.values())/len(worker_diction)} \n'
          f'Сотрудники получающие менее 20 тысяч {[el[0] for el in worker_diction.items() if  el[1] <20000]}')
