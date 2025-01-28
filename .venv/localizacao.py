from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys

class Localizacao(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Localização dos patrimonios")
        self.setGeometry(10, 30, 400, 500)
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

        # Empresa
        # Labels para a empresa do patrimonio
        self.label_empresa = QLabel("Empresa:")
        self.label_empresa.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para a empresa do patrimonio
        self.edit_empresa = QLineEdit()
        self.edit_empresa.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label id e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_empresa)
        self.layout_v.addWidget(self.edit_empresa)

        # Logradouro
        # Labels para o logradouro do patrimonio
        self.label_logra = QLabel("Logradouro:")
        self.label_logra.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o logradouro do patrimonio
        self.edit_logra = QLineEdit()
        self.edit_logra.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label id e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_logra)
        self.layout_v.addWidget(self.edit_logra)

        # Número
        # Labels para o número do patrimonio
        self.label_num = QLabel("Número:")
        self.label_num.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o número do patrimonio
        self.edit_num = QLineEdit()
        self.edit_num.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label id e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_num)
        self.layout_v.addWidget(self.edit_num)
        
        # Prédio
        # Labels para o prédio do patrimonio
        self.label_pred = QLabel("Prédio:")
        self.label_pred.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o prédio do patrimonio
        self.edit_pred = QLineEdit()
        self.edit_pred.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label id e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_pred)
        self.layout_v.addWidget(self.edit_pred)

        # Andar
        # Labels para o andar do patrimonio
        self.label_andar = QLabel("Andar:")
        self.label_andar.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o andar do patrimonio
        self.edit_andar = QLineEdit()
        self.edit_andar.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label id e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_andar)
        self.layout_v.addWidget(self.edit_andar)

        # Sala
        # Labels para a sala do patrimonio
        self.label_sala = QLabel("Sala:")
        self.label_sala.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o sala do patrimonio
        self.edit_sala = QLineEdit()
        self.edit_sala.setStyleSheet("QLineEdit{font-size:12pt}")

        # Adicionar o label id e o lineedit ao layout vertical
        self.layout_v.addWidget(self.label_sala)
        self.layout_v.addWidget(self.edit_sala)

        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:black;color:white;font-size:10pt;font-weight:bold}")

        # Chamar a função de cadastro do cliente ao clicar no botão
        self.button.clicked.connect(self.cadastrar)

        self.layout_v.addWidget(self.button)

        # Adicionanado o layout na tela
        self.setLayout(self.layout_v)

    def cadastrar(self):
        # Vamos criar uma variável que fara referência ao arquivo de texto
        arquivo = open("localizacao.txt", "+a", encoding="utf8")
        arquivo.write(f"Id do produto: {self.edit_id.text()}\n")
        arquivo.write(f"Empresa: {self.edit_empresa.text()}\n")
        arquivo.write(f"Logradouro: {self.edit_logra.text()}\n")
        arquivo.write(f"Número do patrimonio: {self.edit_num.text()}\n")
        arquivo.write(f"Prédio do patrimonio: {self.edit_pred.text()}\n")
        arquivo.write(f"Andar: {self.edit_andar.text()}\n")
        arquivo.write(f"Sala: {self.edit_sala.text()}\n")
        arquivo.write("---------------------------------")
        arquivo.close()


# app = QApplication(sys.argv)
# # Instância da classe CadastroCliente para inicializar a janela
# tela = Localizacao()
# # Exibir a tela durante a execução
# tela.show()
# # Ao clicar no botão fechar a janela deve fechar e sair da memoria
# app.exec()

