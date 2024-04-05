from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
from os import path

class MeuApp(QMainWindow):

    num1 = 0
    num2 = 0
    numResultado = 0
    op = None


    def __init__(self):
        super().__init__()
        loadUi("calculadoraInterface.ui", self)
        self.acoesBotao()

    def localPath(self, relativo):
        return f'{path.dirname(path.realpath(__file__))}\\{relativo}'

    def acoesBotao(self):
        self.numeroZero.clicked.connect(lambda: self.btnNumeros(self.numeroZero))
        self.numeroUm.clicked.connect(lambda: self.btnNumeros(self.numeroUm))
        self.numeroDois.clicked.connect(lambda: self.btnNumeros(self.numeroDois))
        self.numeroTres.clicked.connect(lambda: self.btnNumeros(self.numeroTres))
        self.numeroQuatro.clicked.connect(lambda: self.btnNumeros(self.numeroQuatro))
        self.numeroCinco.clicked.connect(lambda: self.btnNumeros(self.numeroCinco))
        self.numeroSeis.clicked.connect(lambda: self.btnNumeros(self.numeroSeis))
        self.numeroSete.clicked.connect(lambda: self.btnNumeros(self.numeroSete))
        self.numeroOito.clicked.connect(lambda: self.btnNumeros(self.numeroOito))
        self.numeroNove.clicked.connect(lambda: self.btnNumeros(self.numeroNove))
        self.btnVirgula.clicked.connect(lambda: self.btnNumeros(self.btnVirgula))
 
        
        self.btnResultado.clicked.connect(self.mostrarResultado)

        self.btnLimpar.clicked.connect(self.limparNumeros)
        self.btnTrocarSinal.clicked.connect(self.trocaSinal)
        self.btnPorcentagem.clicked.connect(self.porcentagemNum) 


        self.btnAdicao.clicked.connect(lambda: self.definirOperacao(self.somarNumeros))
        self.btnSubtracao.clicked.connect(lambda: self.definirOperacao(self.subtrairNumeros))
        self.btnDivisao.clicked.connect(lambda: self.definirOperacao(self.divisaoNumeros))
        self.btnMultiplicacao.clicked.connect(lambda: self.definirOperacao(self.multiplicarNumeros))

  
    def mostrarDisplay(self, value):
        value = str(value).replace('.', ',')
        self.resultadoDisplay.setText(value)

    def pegarDisplay(self):
        value = self.resultadoDisplay.text()
        value = value.replace(',', '.')
        try:
            value = int(value)
        except:
            value = float(value)
        return value

    def btnNumeros(self, btn):
        ultimoValor = str(self.pegarDisplay())
        if btn.text() == ",":
            if isinstance(self.pegarDisplay(), float):
                return
        else:
            if isinstance(self.pegarDisplay(), int):
                if self.pegarDisplay() == 0:
                    ultimoValor = ""
            else:
                if self.resultadoDisplay.text()[-1] == ",":
                    ultimoValor = self.resultadoDisplay.text()
        self.mostrarDisplay(ultimoValor + btn.text())
    
    def limparNumeros(self):
        self.num1 = 0
        self.num2 = 0
        self.numResultado = 0
        self.op = None
        self.mostrarDisplay(0)
        
    def somarNumeros(self):
        #print(f'Soma({self.num1}+{self.num2}) = ', end='')
        return self.num1 + self.num2
   
    def subtrairNumeros(self):
        #print(f'Sub({self.num1} - {self.num2})= ', end='')
        return self.num1 - self.num2
    
    def multiplicarNumeros(self):
        #print(f'Mult({self.num1} * {self.num2})= ', end='')
        return self.num1 * self.num2
   
    def divisaoNumeros(self):
        #print(f'Div({self.num1} / {self.num2})= ', end='')
        return self.num1 / self.num2
   
    def porcentagemNum(self):
        porcento = self.pegarDisplay() / 100
        if self.op == self.somarNumeros or self.op == self.subtrairNumeros:
            porcento = self.num1 * porcento
        self.mostrarDisplay(porcento)
            
    def resultadoFinal(self):
        if self.op:
            self.num2 = self.pegarDisplay()
            return self.op()
        else:
            print("Não tem operação feita!")

    def definirOperacao(self, operacao):
        self.op = operacao
        self.num1 = self.pegarDisplay()
        self.num2 = 0
        self.mostrarDisplay(0)

    def mostrarResultado(self):
       if self.op:
            if self.num2:
                self.num1 = self.pegarDisplay()
            else:
                self.num2 = self.pegarDisplay()
 
            self.numResult = self.op()
            self.mostrarDisplay(self.numResult)
            #print(self.numResult)

    def trocaSinal(self):
        numeroAtual = self.pegarDisplay()
        numero *= -1
        self.mostrarDisplay(numeroAtual)

if __name__ == "__main__":
    app = QApplication([])
    window = MeuApp()
    window.show()
    app.exec_()