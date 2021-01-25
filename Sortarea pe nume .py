#importam biblioteca de functii extrem de mari si biblioteca de preprocesare  
import functools 
import sklearn.processing

inp=open('Lista de copii: date de intrare.txt','r')
nume=inp.readlines()

nume[-1]=nume[-1]+'\n'
result=[]

for x in nume:
    result.append(x.split())

item=[]
t=[]
for i in result:
    i1=list(i[0])
    i2=list(i[1])
    item.append(i1[0])
    item.append(i2[0])
    item=[functools.reduce(lambda a, b: a+b, item)]
    t.append(item[0])
    item.clear()
    

print(t)
final=[]
gh=0
for i in t:
    final.append(i+nume[gh])
    gh+=1

final.sort()
print(final)

n=0
while n<len(final):
    final[n]=(final[n])[2:]
    n+=1

with open('Lista de copii: date de iesire.txt', 'w') as f:
    for i in final:
        f.write(i)