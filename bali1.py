with open('11.txt', encoding='utf-8') as f:
    s = f.read()
datas = sorted([line.split() for line in s.split("\n")],
               key=lambda item: int(item[2]), reverse=True)
for i, (last_name, first_name, score) in enumerate(datas, start=1):
    if int(score) > 80:
        print(f"{i:3}) {first_name[0]}. {last_name} {score}")
