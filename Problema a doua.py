#Continutul listei
with open('input.txt','r')as f:
    lista1=list(eval(f.read()))
print(lista1)
#Lista in ordine crescatoare 
lista2=sorted(lista1)
print(lista2)
#Lista in ordine descrescatoare 
lista3=sorted(lista1,reverse=True)
print(lista3)
#Numarul de elemente 
print(len(lista1))
#Elementul maxim si minim
print(max(lista1),min(lista1),sep="\n")
#La coada sa adaugat "- 111"
lista4=lista1+[111]
print(lista4)
#Pe pozitia a doua se adauga elementul "- 222"
lista5=lista1
lista5.insert(1, 222)
print(lista5)