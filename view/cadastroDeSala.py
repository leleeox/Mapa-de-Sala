from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot

class cadastrarSalas(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('view/ui/cadastroSalas.ui', self)

    @pyqtSlot()
    def on_cadastrarSalaBtn_clicked(self):
        return self.getNomeSala()
    
    def getNomeSala(self):
        sala = self.inputSala.text().strip()
        return (sala)