import random
from PyQt5 import QtWidgets, uic

coordenadas = []

class telas:
    def __init__(self):
        self.lista = [f"{row}{col}" for row in 'ABCDEFGHIJ' for col in range(1, 11)]

        self.coordenada_1 = random.choice(self.lista)
        coordenadas.append(coordenada_1)
        self.lista.remove(coordenada_1)

        self.coordenada_2 = random.choice(self.lista)
        coordenadas.append(coordenada_2)
        self.lista.remove(coordenada_2)
        

        app = QtWidgets.QApplication([])
        self.tela_inicial = uic.loadUi("telas/tela_inicial.ui")
        self.tela_jogo = uic.loadUi("telas/tela_jogo.ui")
        self.tela_inicial.show()
        self.tela_inicial.btn_jogar.clicked.connect(self.mudar_tela)
        
        for button in self.tela_jogo.findChildren(QtWidgets.QPushButton):
            button.clicked.connect(self.botao_clicado)

        app.exec()
        
    def mudar_tela(self):
        self.tela_inicial.close()
        self.tela_jogo.show()
        
    def botao_clicado(self):
        sender = self.tela_jogo.sender()
        coordenada_atual = sender.objectName()
        if coordenada_atual == self.coordenada_1:
            sender.setStyleSheet("background-image: url('imagens/quadrado_1.png'); border: none")
        
if __name__ == '__main__':
    c = telas()
    