from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton
import sys

class Localizacao(QWidget):
    def __init__(self):
        super().__init__()
        # geometria da tela
        self.setGeometry(500,30,400,600)
        # Titulo da tela
        self.setWindowTitle("Cadastrar Localização")
        # Layout vertical
        self.layout_v = QVBoxLayout()

        # id  Qlabel
        self.label_id = QLabel("Id:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        # Id QLineEdit
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12pt}")

        # Empresa QLabels
        self.label_empresa = QLabel("Empresa:")
        self.label_empresa.setStyleSheet("QLabel{font-size:12pt}")

        # Empresa QLineEdit
        self.edit_emprsa = QLineEdit()
        self.edit_emprsa.setStyleSheet("QLineEdit{font-size:12pt}")

        # logradouro QLabels
        self.label_logradouro = QLabel("Logradouro:")
        self.label_logradouro.setStyleSheet("QLabel{font-size:12pt}")

        # logradouro QLineEdit
        self.edit_logradouro = QLineEdit()
        self.edit_logradouro.setStyleSheet("QLineEdit{font-size:12pt}")

        # numero Qlabel
        self.label_numero = QLabel("Número:")
        self.label_numero.setStyleSheet("QLabel{font-size:12pt}")

        # numero QLineEdit
        self.edit_numero = QLineEdit()
        self.edit_numero.setStyleSheet("QLIneEdit{font-size:12pt}")

        # Prédio QLabel
        self.label_predio = QLabel("Prédio:")
        self.label_predio.setStyleSheet("QLabel{font-size:12pt}")

        # Prédio QLineEdit
        self.edit_predio = QLineEdit()
        self.edit_predio.setStyleSheet("QLineEdit{font-size:12pt}")

        # andar QLabel
        self.label_andar = QLabel("Andar:")
        self.label_andar.setStyleSheet("QLabel{font-size:12pt}")

        # Andar QLineEdit
        self.edit_andar = QLineEdit()
        self.edit_andar.setStyleSheet("QLineEdit{font-size:12pt}")

        # sala QLabel
        self.label_sala =QLabel("Sala:")
        self.label_sala.setStyleSheet("QLabel{font-size:12pt}")

        # sala QLineEdit
        self.edit_sala = QLineEdit()
        self.edit_sala.setStyleSheet("QLineEdit{font-size:12pt}")


        
        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:red;color:white;font-size:12pt;font-weight:bold}")
        # Chamar a função de castro do  
        # cliente ao clicar no botão
        self.button.clicked.connect(self.cadastrar)


        #  adicionar no layout 
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        # empresa
        self.layout_v.addWidget(self.label_empresa)
        self.layout_v.addWidget(self.edit_emprsa)

        # logradouro
        self.layout_v.addWidget(self.label_logradouro)
        self.layout_v.addWidget(self.edit_logradouro)

        # numero
        self.layout_v.addWidget(self.label_numero)
        self.layout_v.addWidget(self.edit_numero)

        # predio
        self.layout_v.addWidget(self.label_predio)
        self.layout_v.addWidget(self.edit_predio)

        # andar
        self.layout_v.addWidget(self.label_andar)
        self.layout_v.addWidget(self.edit_andar)

        # sala
        self.layout_v.addWidget(self.label_sala)
        self.layout_v.addWidget(self.edit_sala)

        # botao
        self.layout_v.addWidget(self.button)

        self.setLayout(self.layout_v)
    def cadastrar(self):
        #  Vamos criar uma variavel que fará
        # referência ao um arquivo de texto
        arquivo = open("Localização.txt","+a",encoding="utf8")
        arquivo.write(f"Id :{self.edit_id.text()}\n")
        arquivo.write(f"Empresa: {self.edit_emprsa.text()}\n")
        arquivo.write(f"logradouro: {self.edit_logradouro.text()}\n")
        arquivo.write(f"Número: {self.edit_numero.text()}\n")
        arquivo.write(f"Prédio: {self.edit_predio.text()}\n")
        arquivo.write(f"Andar: {self.edit_andar.text()}\n")
        arquivo.write(f"Sala: {self.edit_sala.text()}\n")
        arquivo.write("-----------------------------------------------")
        arquivo.close()



















