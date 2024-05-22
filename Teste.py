import sqlite3
import time

banco = sqlite3.connect('Notas_alunos.db')
banco.execute("PRAGMA foreign_kays = ON")
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Alunos (matrícula TEXT NOT NULL, nome TEXT, email TEXT, nascimento DATE, PRIMARY KEY(matrícula))")

cursor.execute("CREATE TABLE IF NOT EXISTS Notas (matrícula TEXT NOT NULL, id_nota TEXT, disciplina TEXT, nota INTEGER, PRIMARY KEY(matrícula, id_nota), FOREIGN KEY (matrícula) REFERENCES Alunos(matrícula))")


consulta = 0
while consulta !=10:
 print("Escolha uma opção: \n [1] Visualisar banco de dados \n [2] Adicionar aluno ao banco de dados \n [3] Lançar nota \n [4] Consultar usuário \n [5] Atualizar elemento de alunos \n [6] Atualizar elemento de notas \n [7] Idade do aluno \n [8] Remover aluno do banco de dados \n [9] Remover nota do banco de dados \n [10] Encerrar programa")

 consulta = int(input("Sua opção: "))

 if consulta == 1:
  cursor.execute("SELECT * FROM alunos")
  print(cursor.fetchall())

  cursor.execute("SELECT * FROM notas")
  print(cursor.fetchall())
  time.sleep(6)

 elif consulta == 2:
  nome = str(input("Digite um nome: "))
  email = str(input("Digite o email: "))
  idade = str(input("Digite data de nascimento (AAAA-MM-DD): "))
  id = int(input("Digite a matrícula: "))
  cursor.execute("INSERT INTO Alunos Values ('"+str(id)+"','"+nome+"', '"+email+"', '"+str(idade)+"')")
  banco.commit()
  cursor.execute("SELECT * FROM alunos WHERE nome= '"+nome+"'")
  print(cursor.fetchall())
  time.sleep(2)

 elif consulta == 3:
  nome4 = int(input("Digite a matrícula do aluno: "))
  idnot = int(input("Digite o id_nota: "))
  mat = str(input("Digite a matéria: "))
  ava1 = float(input("Digite o resultado do ava 1: "))
  ava2 = float(input("Digite o resultado do ava 2: "))
  prova = int(input("Digite o resultado da prova: "))
  resultado = ava1+ava2+prova
  if resultado > 10: resultado = 10
  cursor.execute("INSERT INTO Notas VALUES ('"+str(nome4)+"', '"+str(idnot)+"', '"+mat+"', '"+str(resultado)+"' ) ")
  banco.commit()
  cursor.execute("SELECT * FROM Notas WHERE id_nota= '"+str(idnot)+"' ")
  print(cursor.fetchall())
  time.sleep(2)

 elif consulta == 4:
  nome3 = str(input("Digite a matrícula do usuário para consulta: "))
  cursor.execute("SELECT * FROM Alunos WHERE matrícula='"+nome3+"'")
  print(cursor.fetchall())
  cursor.execute("SELECT * FROM Notas WHERE matrícula='"+nome3+"'")
  print(cursor.fetchall())
  time.sleep(6)

 elif consulta == 5:
   v1 = str(input("Digite a matrícula do aluno: "))
   v2 = str(input("Digite oque deseja substituir: "))
   v3 = str(input("Digite o novo valor: "))
   cursor.execute("UPDATE Alunos SET '"+v2+"' = '"+v3+"' WHERE matrícula= '"+v1+"'")
   banco.commit()
   cursor.execute("SELECT * FROM alunos WHERE matrícula='"+v1+"'")
   print(cursor.fetchall())
   time.sleep(2)

 elif consulta == 6:
  q1 = str(input("Digite o id_nota: "))
  q2 = str(input("Digite oque deseja substituir: "))
  q3 = str(input("Digite o novo valor: "))
  cursor.execute("UPDATE Notas SET '"+q2+"' = '"+q3+"' WHERE id_nota= '"+q1+"'")
  banco.commit()
  cursor.execute("SELECT * FROM Notas WHERE id_nota='"+q1+"'")
  print(cursor.fetchall())
  time.sleep(2)

 elif consulta == 7:
  nome5 = str(input("Digite o nome do aluno: "))
  cursor.execute("SELECT nome, nascimento, CASE WHEN strftime('%m', date('now')) >  strftime('%m', date(nascimento)) THEN strftime('%Y', date('now')) - strftime('%Y', date(nascimento)) WHEN strftime('%m', date('now')) = strftime('%m', date(nascimento)) THEN CASE WHEN strftime('%d', date('now')) >= strftime('%d', date(nascimento)) THEN strftime('%Y', date('now')) - strftime('%Y', date(nascimento)) ELSE strftime('%Y', date('now')) - strftime('%Y', date(nascimento)) - 1 END WHEN strftime('%m', date('now')) < strftime('%m', date(nascimento)) THEN strftime('%Y', date('now')) - strftime('%Y', date(nascimento)) - 1 END FROM alunos WHERE nome='"+nome5+"'") 
  print(cursor.fetchall())
  time.sleep(2)

 elif consulta == 8:
  cursor.execute("SELECT * FROM Alunos")
  print(cursor.fetchall())
  nome2 = int(input("Digite a matrícula do usuário a ser deletado: "))
  cursor.execute("DELETE from alunos WHERE matrícula='"+str(nome2)+"'")
  banco.commit()
  time.sleep(2)

 elif consulta == 9:
  cursor.execute("SELECT * FROM Notas")
  print(cursor.fetchall())
  nota2 = int(input("Digite o id_nota da nota a ser deletada: "))
  cursor.execute("DELETE from notas WHERE id_nota='"+str(nota2)+"'")
  banco.commit()
  time.sleep(2)

 elif consulta == 10:
  print('Programa encerrado') 

 else:
  print("\nDigite uma opção válida")  
  time.sleep(2)

 print('=-'*40) 