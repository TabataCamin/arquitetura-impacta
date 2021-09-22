from abc import ABC, abstractmethod
from unittest import TestCase, main

class Calculadora:
    def calcular(self,valor1,valor2,operador):
        validaOperador = OperacaoFabrica()
        operacao = validaOperador.criar(operador)
        if (operador == None):
            return 0
        else: 
            resultado = operacao.executar(valor1,valor2)
            return resultado

class OperacaoFabrica:
    def criar(self,operador):
        if (operador == "soma"):
            return Soma()
        elif (operador == "subtracao"):
            return Subtracao()
        elif (operador == "divisao"):
            return Divisao()
        elif (operador == "multiplicacao"):
            return Multiplicacao()       
            
class Operacao(ABC):
    @abstractmethod
    def executar(self,valor1,valor2):
        pass

class Soma(Operacao):
    def executar(self,valor1,valor2):
        resultado = valor1 + valor2
        return resultado

class Subtracao(Operacao):
    def executar(self,valor1,valor2):
        resultado = valor1 - valor2
        return resultado

class Divisao(Operacao):
    def executar(self,valor1,valor2):
        resultado = valor1 / valor2
        return resultado

class Multiplicacao(Operacao):
    def executar(self,valor1,valor2):
        resultado = valor1 * valor2
        return resultado

class Testes(TestCase):
    def test_soma(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(10,10,"soma"),20)

    def test_soma2(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(100,100,"soma"),200)

    def test_subtracao(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(100,50,"subtracao"),50)
    
    def test_subtracao2(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(150,300,"subtracao"),-150)

    def test_divisao(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(100,2,"divisao"),50)
    
    def test_divisao2(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(10,2,"divisao"),5)

    def test_multiplicacao(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(10,10,"multiplicacao"),100)

    def test_multiplicacao2(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(5,-5,"multiplicacao"),-25)

    def test_valor_invalido(self):
        resultadoTest = Calculadora()
        self.assertEqual(resultadoTest.calcular(None,5,None),0)
    
if __name__ == "__main__":
    main()
