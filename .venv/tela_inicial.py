import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from patrimonio import Patrimonio
from localização import Localizacao
class TelaInicial (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300,200,200,150)
        self.layout_v = QVBoxLayout()
        self.label_titulo = QLabel("Clique para abrir a janela")
        self.label_titulo2 = QLabel("Abrir Localização")
        self.buttom = QPushButton("Abrir Patrimônio")
        self.buttom2 = QPushButton("Abrir Localização dos Patrimônios")


        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.buttom)
        self.layout_v.addWidget(self.label_titulo2)
        self.layout_v.addWidget(self.buttom2)
       
        self.buttom.clicked.connect(self.abrir_cadatro)
        self.buttom2.clicked.connect(self.localizacao)

        self.setLayout(self.layout_v)
    
    def abrir_cadatro(self):
        self.pat = Patrimonio()
        self.pat.show()
    
    def localizacao (self):
        self.pat2 = Localizacao()
        self.pat2.show()

app = QApplication(sys.argv)
tela = TelaInicial()
tela.show()
app.exec()