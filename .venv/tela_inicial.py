import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
from patrimonio import Patrimonio
from localização import Localizacao
from localizar_patrimonio import LocalizarPatrimonio
class TelaInicial (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300,200,200,150)
        self.layout_v = QVBoxLayout()
        self.label_titulo = QLabel("Clique para abrir a janela")
        self.label_titulo2 = QLabel("Abrir Localização")
        self.label_titulo3 = QLabel("abrir localizador de Patrimônio")
        self.buttom = QPushButton("Abrir Patrimônio")
        self.buttom2 = QPushButton("Abrir Localização dos Patrimônios")
        self.buttom3 = QPushButton("Abrir o localizador do Patrimônio")


        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.buttom)
        
        self.layout_v.addWidget(self.label_titulo2)
        self.layout_v.addWidget(self.buttom2)

        self.layout_v.addWidget(self.label_titulo3)
        self.layout_v.addWidget(self.buttom3)
       
        self.buttom.clicked.connect(self.abrir_cadatro)
        self.buttom2.clicked.connect(self.localizacao)
        self.buttom3.clicked.connect(self.LocalizarPatrimonio)

        self.setLayout(self.layout_v)
    
    def abrir_cadatro(self):
        self.pat = Patrimonio()
        self.pat.show()
    
    def localizacao (self):
        self.pat2 = Localizacao()
        self.pat2.show()

    def LocalizarPatrimonio(self):

        self.pat3=LocalizarPatrimonio()
        self.pat3.show()           

app = QApplication(sys.argv)
tela = TelaInicial()
tela.show()
app.exec()