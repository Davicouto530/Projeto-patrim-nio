import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from patrimonio import Patrimonio
from localizacao import Localizacao

class TelaInicial(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300, 200, 200, 150)
        self.layout_v = QVBoxLayout()

        self.label_titulo = QLabel("Clique para abrir a janela")
        self.button = QPushButton("Abrir patrimonio")

        self.label_titulo2 = QLabel("Clique para abrir a janela localização")
        self.button2 = QPushButton("Abrir localização")

        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.button)

        self.layout_v.addWidget(self.label_titulo2)
        self.layout_v.addWidget(self.button2)

        self.button.clicked.connect(self.abrir_cadastro)

        self.button2.clicked.connect(self.abrir_localizacao)

        self.setLayout(self.layout_v)
    
    def abrir_cadastro(self):
        self.pat = Patrimonio()
        self.pat.show()

    def abrir_localizacao(self):
        self.loc = Localizacao()
        self.loc.show()

app = QApplication(sys.argv)
tela = TelaInicial()
tela.show()
app.exec()