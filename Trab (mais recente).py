import sqlite3
import time

banco = sqlite3.connect('Notas_alunos.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE alunos (nome text, data_nasc date, email text, cpf integer, nota intger)")

consulta = 0
while consulta !=8:
 print("Escolha uma opção: \n [1] Visualisar banco de dados \n [2] Adicionar ao banco de dados \n [3] Remover do banco de dados \n [4] Consultar usuário \n [5] Atualizar elemento do banco de dados \n [6] Lançar nota \n [7] Idade do aluno \n [8] Encerrar programa")

 consulta = int(input("Sua opção: "))

 if consulta == 1:
  cursor.execute("SELECT * FROM alunos")
  print(cursor.fetchall())
  time.sleep(6)

 elif consulta == 2:
  nome = str(input("Digite um nome: "))
  idade = str(input("Digite data de nascimento (AAAA-MM-DD): "))
  email = str(input("Digite email: "))
  cpf = int(input("Digite CPF: "))
  cursor.execute("INSERT INTO alunos Values ('"+nome+"','"+str(idade)+"','"+email+"', '"+str(cpf)+"', '0')")
  banco.commit()
  cursor.execute("SELECT * FROM alunos WHERE nome= '"+nome+"'")
  print(cursor.fetchall())
  time.sleep(2)

 elif consulta == 3:
  cursor.execute("SELECT * FROM alunos")
  print(cursor.fetchall())
  nome2 = str(input("Digite o usuário a ser deletado: "))
  cursor.execute("DELETE from alunos WHERE nome='"+nome2+"'")
  banco.commit()
  time.sleep(2)

 elif consulta == 4:
  nome3 = str(input("Digite o usuário para consulta: "))
  cursor.execute("SELECT * FROM alunos WHERE nome='"+nome3+"'")
  print(cursor.fetchall())
  time.sleep(6)

 elif consulta == 5:
  v1 = str(input("Digite o nome do aluno que receberá a alteração: "))
  v2 = str(input("Digite oque deseja substituir: "))
  v3 = str(input("Digite o novo valor: "))
  cursor.execute("UPDATE alunos SET '"+v2+"' = '"+v3+"' WHERE nome= '"+v1+"'")
  banco.commit()
  cursor.execute("SELECT * FROM alunos WHERE nome='"+v1+"'")
  print(cursor.fetchall())
  time.sleep(2)

 elif consulta == 6:
  nome4 = str(input("Digite o nome do aluno: "))
  prova1 = int(input("Digite o resultado da prova 1: "))
  prova2 = int(input("Digite o resultado da prova 2: "))
  ava = int(input("Digite o resultado do avaliando o aprendizado: "))
  resultado = (prova1+prova2)/2 + ava
  if resultado > 10: resultado = 10
  cursor.execute("UPDATE alunos SET nota = '"+str(resultado)+"' WHERE nome= '"+nome4+"' ")
  banco.commit()
  cursor.execute("SELECT nome, nota FROM alunos WHERE nome='"+nome4+"'")
  print(cursor.fetchall())
  time.sleep(2)

 elif consulta == 7:
  nome5 = str(input("Digite o nome do aluno: "))
  cursor.execute("SELECT nome, data_nasc, CASE WHEN strftime('%m', date('now')) >  strftime('%m', date(data_nasc)) THEN strftime('%Y', date('now')) - strftime('%Y', date(data_nasc)) WHEN strftime('%m', date('now')) <  strftime('%m', date(data_nasc)) THEN strftime('%Y', date('now')) - strftime('%Y', date(data_nasc)) - 1 END FROM alunos WHERE nome='"+nome5+"'") 
  print(cursor.fetchall())

 elif consulta == 8:
  print('Programa encerrado') 

 else:
  print("\nDigite uma opção válida")  
  time.sleep(2)

 print('=-'*40) 
