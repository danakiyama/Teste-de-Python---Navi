#questão 1
count = 0
for i in range(1, 5000001):
    if i%2 == 0 and i%37 == 0 and i%49 == 0:
        count+=1
print('#Questão 1')
print("Número total de multiplos:", count)

#questão 2
import math
x = []
for i in range(10):
    if i%2 == 0:
        fat = math.factorial(i)
        x.append(3**i + 7*fat)
    else:
        ln = math.log(i)
        x.append(2**i + 4*ln)
x_max_index = x.index(max(x))
media = sum(x)/len(x)
media = round(media,2)
print('#Questão 2')
print('Posição  do maior valor de x: ', x_max_index)
print('Média do vetor: ', media)

#questao 3
print('#Questão 3')
string = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto']
dic = {}
for i  in range(5):
    nome = input('digite o nome do ' + string[i] + ' aluno: ')
    nota = int(input('Digite a nota de ' + nome + ': '))
    dic[nome] = nota
max_value = max(dic.values())
maiores_notas = [k for k, v in dic.items() if v == max_value]
print('A maior nota é/são do(s) aluno(s): ', maiores_notas)
print('e a nota é igual a: ', max_value)
