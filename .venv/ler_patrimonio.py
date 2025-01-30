import csv 

# Abrir o arquivo csv e atribuir a uma variável
arquivo = open("patrimonio.csv","r",encoding="utf-8")
linhas = csv.reader(arquivo) # essa linha serve para ler o que está dentro do arquivo

for i in linhas:
    lin = str(i).replace("['","").replace("']","").split(";")
    if(lin[0] == "12"):
        print(lin)
