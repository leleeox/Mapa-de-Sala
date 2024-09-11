from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSlot


class LoginInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi('interfaceLogin.ui', self)

        # Remove a barra de título e as bordas da janela
        self.setWindowFlags(Qt.FramelessWindowHint)

        # Define a janela como transparente
        self.setAttribute(Qt.WA_TranslucentBackground)

        #Conectando os botões:
        self.botaoEntrar.clicked.connect(self.getUsuarioSenha)


    def getUsuarioSenha(self):
        usuario = self.inputUsuario.text()
        senha = self.inputSenha.text()

        if (usuario != '' and senha !=''):
            print(f'Usuário: {usuario} \nSenha: {senha}')
        else:
            texto = 'Dados incompletos!'
            self.respostaLogin.setText(texto)
            QTimer.singleShot(3000, lambda: self.limparCampos(self.respostaLogin))

        self.limparCampos(self.inputUsuario)
        self.limparCampos(self.inputSenha)

    def limparCampos(self, campo):
        campo.clear()


if __name__ == "__main__":
    app = QApplication([])
    widget = LoginInterface()
    widget.show()

    app.exec_()