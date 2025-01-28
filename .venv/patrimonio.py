from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton
import sys

class Patrimonio(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos cofigurar a geometria da
        #tela. Setando os valores de posição X e Y,
        #além de largura e altura
        self.setGeometry(500,30,400,600)

        # Texto para barra de titulo
        self.setWindowTitle("Cadastrar Patrimônio")

        # Gerenciador de layout vertical 
        self.layout_v =QVBoxLayout()

        #  id do patrimonio Labels  
        self.label_id = QLabel("id do patrimonio:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        #  id do patrimonio LineEdit  
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12pt}")

        # Número de sére Labels
        self.label_numerodeserie = QLabel("Numero de serie:")
        self.label_numerodeserie.setStyleSheet("QLabel{font-size:12pt}")

        # numero de serie LineEdit
        self.edit_numerodeserie = QLineEdit()
        self.edit_numerodeserie.setStyleSheet("QLineEdit{font-size:12pt}")

        # nome do patrimonio Labels
        self.label_nomedopatrimonio = QLabel("Nome do patrimonio:")
        self.label_nomedopatrimonio.setStyleSheet("QLabel{font-size:12pt}")

        # Nome do patrimonio LineEdit

        self.edit_nomedopatrimonio = QLineEdit()
        self.edit_nomedopatrimonio.setStyleSheet("QLineEdit{font-size:12pt}")

        # tipo Labels
        self.label_tipo = QLabel("Tipo do patrimonio:")
        self.label_tipo.setStyleSheet("QLabel{font-size:12pt}")

        # tipo LineEdit
        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{font-size:12pt}")

        # Descrição do patrimônio labels
        self.label_descricao = QLabel("Descrição: ")
        self.label_descricao.setStyleSheet("QLabel{font-size:12pt}")

        # Descrição do parimônio LineEdit
        self.edit_descricao = QLineEdit()
        self.edit_descricao.setStyleSheet("QLineEdit{font-size:12pt}")

        # loalização labels
        self.label_localizacao = QLabel("Localização: ")
        self.label_localizacao.setStyleSheet("QLabel{font-size:12pt}")

        # Localização LineEdit
        self.edit_localizacao = QLineEdit()
        self.edit_localizacao.setStyleSheet("QLineEdit{font-size:12pt}")

        # Data da fabricação labels
        self.label_DataFabricacao = QLabel("Data da Fabricação: ")
        self.label_DataFabricacao.setStyleSheet("QLabel{font-size:12pt}")

        # data da fabricação QLineEdit
        self.edit_DataFabricacao = QLineEdit ()
        self.edit_DataFabricacao.setStyleSheet("QLineEdit{font-size:12pt}")

        # Data de aquisição lebels
        self.label_DataAquisicao = QLabel("Data de aquisição: ")
        self.label_DataAquisicao.setStyleSheet("QLabel{font-size:12pt}")

        # Data de aquisição QLineEdit
        self.edit_DataAquisicao = QLineEdit ()
        self.edit_DataAquisicao.setStyleSheet("QLineEdit{font-size:12pt}")



        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:red;color:white;font-size:12pt;font-weight:bold}")
        # Chamar a função de castro do  
        # cliente ao clicar no botão
        self.button.clicked.connect(self.cadastrar)





        # Adicionar a label nome e  lineedit ao
        # layout vertical
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        # Email
        self.layout_v.addWidget(self.label_numerodeserie)
        self.layout_v.addWidget(self.edit_numerodeserie)

        # Telefone
        self.layout_v.addWidget(self.label_nomedopatrimonio)
        self.layout_v.addWidget(self.edit_nomedopatrimonio)

        # Idade
        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)

        # Descrição
        self.layout_v.addWidget(self.label_descricao)
        self.layout_v.addWidget(self.edit_descricao)

        # Localização
        self.layout_v.addWidget(self.label_localizacao)
        self.layout_v.addWidget(self.edit_localizacao)

        # Data da fabricação 
        self.layout_v.addWidget(self.label_DataFabricacao)
        self.layout_v.addWidget(self.edit_DataFabricacao)

        #  Data da aquisição
        self.layout_v.addWidget(self.label_DataAquisicao)
        self.layout_v.addWidget(self.edit_DataAquisicao)

        # botao
        self.layout_v.addWidget(self.button)
                                
        # Adicionar o layout_v a tela
        self.setLayout(self.layout_v)
    def cadastrar(self):
        #  Vamos criar uma variavel que fará
        # referência ao um arquivo de texto
        arquivo = open("iventario.txt","+a",encoding="utf8")
        arquivo.write(f"Id :{self.edit_id.text()}\n")
        arquivo.write(f"Número de série: {self.edit_numerodeserie.text()}\n")
        arquivo.write(f"Nome do patrimônio: {self.edit_nomedopatrimonio.text()}\n")
        arquivo.write(f"Tipo: {self.edit_tipo.text()}\n")
        arquivo.write(f"Descrição: {self.edit_descricao.text()}\n")
        arquivo.write(f"Localização: {self.edit_localizacao.text()}\n")
        arquivo.write(f"Data da fabricação: {self.edit_DataFabricacao.text()}\n")
        arquivo.write(f"Data da aquisição {self.edit_DataAquisicao.text()}\n")
        arquivo.write("-----------------------------------------------")
        arquivo.close()

# app = QApplication(sys.argv)
# Instância da classe CadastroCliente
# para iniciar a janela 
# tela = Patrimonio()
#exibir a tela duarante a execução
# tela.show()
#  Ao clicar no botão fechar a tela
# deve fechar e sair da memória
# app.exec()