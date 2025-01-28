from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox 
import sys

class Patrimonio(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos configurar a geometria da tela. 
        # Setando os valores de posição x e y,
        # Além de largura
        self.setGeometry(10, 30, 400, 300) # Fazendo o tamanho da Janela

        # Texto para a barra de título
        self.setWindowTitle("Cadastro de equipamentos")

        # Gerenciador de layout vertical
        self.layout_v = QVBoxLayout()

        # ID
        # Labels para os id dos produtos
        self.label_id = QLabel("Id do equipamento")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o id do cliente
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label id e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        # Número de serie
        # Labels para o número de serie do produto
        self.label_serie = QLabel("Número de série: ")
        self.label_serie.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o número de serie do produto
        self.edit_serie = QLineEdit()
        self.edit_serie.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label número de serie e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_serie)
        self.layout_v.addWidget(self.edit_serie)

        # Nome
        # Labels para o nome do equipamento
        self.label_nome = QLabel("Nome do equipamento: ")
        self.label_nome.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o nome do equipamento
        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label nome do equipamento e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_nome)
        self.layout_v.addWidget(self.edit_nome)

        # Tipo de produto
        # Labels para o Idade do cliente
        self.label_tipo = QLabel("Tipo de produto: ")
        self.label_tipo.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o tipo de produto
        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label tipo e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)

        # Descrição do produto
        # Labels para o Idade do cliente
        self.label_desc = QLabel("Descrição do produto: ")
        self.label_desc.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o descrição de produto
        self.edit_desc = QLineEdit()
        self.edit_desc.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label descrição e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_desc)
        self.layout_v.addWidget(self.edit_desc)

        # Localização do produto
        # Labels para o Idade do cliente
        self.label_local = QLabel("Localização do produto: ")
        self.label_local.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o localização de produto
        self.edit_local = QLineEdit()
        self.edit_local.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label local e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_local)
        self.layout_v.addWidget(self.edit_local)

        # Data de fabricação
        # Labels para o data de fabricação
        self.label_dataf = QLabel("Data de fabricação: ")
        self.label_dataf.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o data de fabricação
        self.edit_dataf = QLineEdit()
        self.edit_dataf.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label data e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_dataf)
        self.layout_v.addWidget(self.edit_dataf)

        # Data de aquisição
        # Labels para o data de aquisição
        self.label_dataq = QLabel("Data de aquisição: ")
        self.label_dataq.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para data de aquisição
        self.edit_dataq = QLineEdit()
        self.edit_dataq.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label data e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_dataq)
        self.layout_v.addWidget(self.edit_dataq)
        

        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:black;color:white;font-size:10pt;font-weight:bold}")

        # Chamar a função de cadastro do cliente ao clicar no botão
        self.button.clicked.connect(self.cadastrar)

        self.layout_v.addWidget(self.button)

        # Adicionanado o layout na tela
        self.setLayout(self.layout_v)

    def cadastrar(self):
        if(self.edit_id.text() == "" or self.edit_serie.text() == "" or self.edit_nome.text() == "" or self.edit_tipo.text() == "" or self.edit_desc.text() == "" or self.edit_local.text() == "" or self.edit_dataf.text() == "" or self.edit_dataq.text() == ""):
            QMessageBox.critical(self,"Erro","Você deve preencher todos os campos!")
        else:
            # Vamos criar uma variável que fara referência ao arquivo de texto
            arquivo = open("patrimonio.txt", "+a", encoding="utf8")
            arquivo.write(f"Id do produto: {self.edit_id.text()}\n")
            arquivo.write(f"Número de série: {self.edit_serie.text()}\n")
            arquivo.write(f"Número do equipamento: {self.edit_nome.text()}\n")
            arquivo.write(f"Tipo do produto: {self.edit_tipo.text()}\n")
            arquivo.write(f"Descrição do produto: {self.edit_desc.text()}\n")
            arquivo.write(f"Localização do produto: {self.edit_local.text()}\n")
            arquivo.write(f"Data de fabricação do produto: {self.edit_dataf.text()}\n")
            arquivo.write(f"Data de aquisação do produto: {self.edit_dataq.text()}\n")
            arquivo.write("---------------------------------")
            arquivo.close()

            # Serve para exibir essa mensagem quando clicar em "cadastrar"
            QMessageBox.information(self,"Salvo","Os dados do patrimonio foram salvos")





# app = QApplication(sys.argv)
# # Instância da classe CadastroCliente para inicializar a janela
# tela = Patrimonio()
# # Exibir a tela durante a execução
# tela.show()
# # Ao clicar no botão fechar a janela deve fechar e sair da memoria
# app.exec()