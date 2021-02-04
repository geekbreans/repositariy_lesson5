m_dict = {}
with open("text_6.txt", 'r', encoding='utf-8') as f_object:
    for line in f_object:
        w_value = line.split(":")
        n = ["".join(el for el in w_value[1] if el == " " or el.isnumeric())]

        m_dict[w_value[0]] = sum(map(int, n[0].split()))

print(f'{m_dict}')
