import csv

# Abrir o arquivo csv e atribuir 
# a uma variavel
arquivo = open("iventario.csv", "r",encoding="utf8")
linhas = csv.reader(arquivo)


for i in linhas :
    lin = str(i).replace("['","").replace("']","").split(";")
    if(lin[0]=="14"):
     print(lin[0])
