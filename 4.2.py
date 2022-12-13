#4.2 

meses_trabalhados = int(input("\por quantos meses durou o trabalho do Tiago?"))
disp = input('Tem disponibilidade entre dezembro e janeiro? ')

if (meses_trabalhados >= 12) and (disp == "Sim"):
    print('Tiago vai poder sair de férias')
else:
    print('Tiago não vai poder sair de férias')