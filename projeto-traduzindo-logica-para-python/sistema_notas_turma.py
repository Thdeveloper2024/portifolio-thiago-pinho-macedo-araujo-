def sistema_notas_turmas():

  total_alunos = int(input("quantos alunos existem na turma? "))

  for j in range(total_alunos):

    aluno_nome = input("Digite o nome do aluno: ")

    n1 = float(input("Digite a primeira nota do aluno: "))

    n2 = float(input("Digite a segunda nota do aluno: "))

    media_aluno = (n1 + n2) / 2



  if media_aluno >= 7:

    print(f"{aluno_nome} aprovado com a media: {media_aluno}")



  elif media_aluno >= 5.0:

    print(f"{aluno_nome} recuperacao com a media: {media_aluno}")



  else:

    print(f"{aluno_nome} : Repprovado")



sistema_notas_turmas()
