#4.1

nota =  int(input('Qual a nota do aluno? '))
participacao = (input('Você é participativo? '))

if nota >= 7: 
    print('Você foi aprovado, parabéns!!')

elif (nota == 6) and (participacao == "Sim"):  
    print('Você está de recuperação!')
    
else:
    print('Você foi reprovado!')