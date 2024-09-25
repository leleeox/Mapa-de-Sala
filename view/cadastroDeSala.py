from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot

class cadastrarSalas(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('view/ui/cadastroSalas.ui', self)

    @pyqtSlot()
    def on_cadastrarSalaBtn_clicked(self):
        nomeSala = self.getNomeSala()
        if nomeSala:
            self.registrarSala(nomeSala)
        else:
            self.mostrarErro("O nome da sala não pode estar vazio.")

    def getNomeSala(self):
        return self.nomeSala.text().strip()

    def registrarSala(self):
        self.nomeSala.clear()


if __name__ == "__main__":
    app = QApplication([])
    widget = cadastrarSalas()
    widget.show()
    app.exec_()
