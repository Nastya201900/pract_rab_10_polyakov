fin_up=open('input.txt','r')
s=0 # сумма чисел
n=0 # количество чисел
for line in fin_up: # считываем построчно из файла
    s+=int(line)
    n+=1
fin_up.close()
fout=open('output.txt','w')
if n != 0: # если числа есть
    fout.write(str(s/n))
fout.close()