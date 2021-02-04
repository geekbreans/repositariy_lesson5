import json

with open("mFirstJson.json", 'w', encoding='utf-8') as f_t:
    with open("text_7.txt", 'r', encoding='utf-8') as f_object:
        pribyl = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in f_object}
        dochod = [pribyl, {"Средняя доход": round(sum([int(n) for n in pribyl.values() if int(n) > 0]) / len(
            [n for n in pribyl.values() if int(n) > 0]), 3)}]
    json.dump(dochod, f_t, ensure_ascii=False, indent=4)
