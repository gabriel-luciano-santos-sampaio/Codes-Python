'''n= int(input("Digite a quantidade de alunos: "))
qap=qrep=qef=0
for i in range(1,n+1):
  n1=float(input(f"Digite a nota da primeira avaliação do {i}º aluno:"))
  n2=float(input(f"Digite a nota da segunda avaliação do {i}º aluno:"))
  media= (n1+n2)/2
  if media>= 7:
    qap+=1
  elif media >=4 :
    qef+=1
  else:
    qrep+=1
  print(f" Relatorio da Turma com {n} alunos")
  print(f"Temos {qap} alunos aprovados que correspondem {qap/n*100}%  ")
  print(f"Temos {qef} alunos em exame final que correspondem {qef/n*100}%  ")
  print(f"Temos {qrep} alunos reprovados que correspondem {qrep/n*100}%  ")'''

n=int(input("Quantos produtos serão cadastrados"))
qsuf=qalert=qabaixo=0
for i in range(1,n+1):
  nome = input(f"Entre com o nome do produto {i} produto: ")
  quant=int(input("Entre com a quantidade em estoque do {i} produto: "))
