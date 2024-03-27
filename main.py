from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from logger import LogManagement

class MeuApp(QMainWindow):

    num1 = 0
    num2 = 0
    result = 0
    op = None


    log = LogManagement(__file__)


    def __init__(self):
        super().__init__()
        loadUi("calculadoraInterface.ui", self)

        self.log.info("Iniciei a interface")
        self.numeroZero.clicked.connect(lambda: self.btnNumeros(0))
        self.numeroUm.clicked.connect(lambda: self.btnNumeros(1))
        self.numeroDois.clicked.connect(lambda: self.btnNumeros(2))
        self.numeroTres.clicked.connect(lambda: self.btnNumeros(3))
        self.numeroQuatro.clicked.connect(lambda: self.btnNumeros(4))
        self.numeroCinco.clicked.connect(lambda: self.btnNumeros(5))
        self.numeroSeis.clicked.connect(lambda: self.btnNumeros(6))
        self.numeroSete.clicked.connect(lambda: self.btnNumeros(7))
        self.numeroOito.clicked.connect(lambda: self.btnNumeros(8))
        self.numeroNove.clicked.connect(lambda: self.btnNumeros(9))

        self.igual.clicked.connect(self.mostrarResultado)
        self.limparTudo.clicked.connect(self.limparNumeros)
        self.adicao.clicked.connect(lambda: self.definirOperacao(self.somarNumeros))
        self.subtracao.clicked.connect(lambda: self.definirOperacao(self.subtrairNumeros))
        self.divisao.clicked.connect(lambda: self.definirOperacao(self.divisaoNumeros))
        self.multiplicacao.clicked.connect(lambda: self.definirOperacao(self.multiplicarNumeros))
        self.maisMenos.clicked.connect(self.inverterNegativoPositivo)
        self.btnPorcentagem.clicked.connect(self.porcentagemNumeros)
        self.btnVirgula.clicked.connect(lambda: self.btnNumeros(self.btnNumeros))

    def mostrarDisplay(self, value):
        value = str(value).replace(",",".")
        self.resultado.setText(value)

    def pegarDisplay(self):
        value = self.resultado.text()
        value = value.replace(".", ",")
        try:
            value = int(value)
        except:
            value = float(value)
        return value

    def definirOperacao(self, operacao):
        self.op = operacao
        self.num1 = self.pegarDisplay()
        self.num2 = 0
        self.mostrarDisplay(0)

    def btnNumeros(self, btn):
        if btn.text() == ",":
            if isinstance(self.pegarDisplay(), int):
                ultimoValor = str(self.pegarDisplay())
                self.mostrarDisplay(ultimoValor + btn)

            else:
                if isinstance(self.pegarDisplay(), int):
                    if self.pegarDisplay() == 0:
                        self.mostrarDisplay(btn.text())
                    else:
                        ultimoValor = str(self.pegarDisplay())
                        self.mostrarDisplay(ultimoValor + btn.text())
                else:
                    if self.resultado.text()[-1] == ",":
                        ultimoValor = self.resultado.text()
                        self.mostrarDisplay(ultimoValor + btn.text())
                    else:
                        ultimoValor = str(self.pegarDisplay())
                        self.mostrarDisplay(ultimoValor + btn.text())


    def limparNumeros(self):
        self.num1 = 0
        self.num2 = 0
        self.numResult = 0
        self.resultado.clear()

    def somarNumeros(self):
        return self.num1 + self.num2
    
    def subtrairNumeros(self):
        return self.num1 - self.num2

    def multiplicarNumeros(self):
        return self.num1 * self.num2
    
    def divisaoNumeros(self):
        return self.num1 / self.num2
    
    def porcentagemNumeros(self):
        porcent = self.pegarDisplay() / 100
        if self.op == self.somarNumeros or self.op == self.subtrairNumeros:
            porcent = self.num1 * porcent
        self.mostrarDisplay(porcent)

    def inverterNegativoPositivo(self):
        numAtual = self.pegarDisplay()
        numAtual *= -1
        self.mostrarDisplay(numAtual)


    def resultadoFinal(self):
        if self.op:
            self.num2 = self.pegarDisplay()
            return self.op()
        else:
            print("Não tem operação feita!")

    def mostrarResultado(self):
        if self.op:
            if self.num2:
                self.num1 = self.pegarDisplay()
            else:
                self.num2 = self.pegarDisplay()

            self.numResult = self.op()
            self.mostrarDisplay(self.numResult)
            

if __name__ == "__main__":
    app = QApplication([])
    window = MeuApp()
    window.show()
    app.exec_()