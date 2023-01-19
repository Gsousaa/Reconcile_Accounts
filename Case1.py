import csv
from pathlib import Path
from pprint import pprint

def reconcile_accounts(transactions1, transactions2):

    transactions1.pop(0)#Limpeza dos Headers
    transactions2.pop(0)
    transactions1_str = [str(i) for i in transactions1]#Transformando cada linha em string para busca mais rápida
    transactions2_str = [str(i) for i in transactions2]
    index_match1= [i for i, el in enumerate(transactions1_str) if el in set(transactions2_str)]# Buscando indexs que possuem match
    index_match2= [i for i, el in enumerate(transactions2_str) if el in set(transactions1_str)]

    for i in enumerate(transactions1):
        if(i[0] in index_match1):
            transactions1[i[0]].append("FOUND")#Adicionado Found nos campos com Match
        else:
            transactions1[i[0]].append("MISSING")
    for i in enumerate(transactions2):
        if(i[0] in index_match2):
            transactions2[i[0]].append("FOUND")
        else:
            transactions2[i[0]].append("MISSING")
    return transactions1,transactions2#Retorno das listas tratadas

transactions1 = (list(csv.reader(Path('Case1/transactions1.csv').open(encoding='utf-8'))))
transactions2 = (list(csv.reader(Path('Case1/transactions2.csv').open(encoding='utf-8'))))

out1,out2 =reconcile_accounts(transactions1,transactions2)
pprint(out1)
pprint(out2)