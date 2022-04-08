print('Situação aluno')
print('Informe a primeira nota')

n1=input('Nota 1:')
n2=input('Nota 2:')
n3=2

print('Informe abaixo o nome do aluno')

nome=input('Nome:')
media=int(n1)+int(n2)
media=int(media)/int(n3)

print('A sua nota final é:',media,',',nome,'.')

if media<6:
    print('Aluno reprovado, tente novamente ano que vem.')
elif media>=6:  
    print('Aluno aprovado, media:',media,'Parabens,',nome,'.')
