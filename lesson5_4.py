er_words = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_4r.txt", 'w', encoding='utf-8') as f_t:
    with open("text_4.txt", 'r', encoding='utf-8') as f_object:
        f_t.writelines([line.replace(line.split()[0], er_words.get(line.split()[0])) for line in f_object])
print('Перевод текста записан в файл text_4r.txt')