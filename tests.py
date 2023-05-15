import unittest
import os
import checkpoint as ch

class HenryChallenge(unittest.TestCase):
    def test_NumeroCapicua_01(self):
      valor_test = ch.numeroCapicua(1234)
      valor_esperado = False
      self.assertEqual(valor_test, valor_esperado)

    def test_NumeroCapicua_02(self):
      valor_test = ch.numeroCapicua(358853)
      valor_esperado = True
      self.assertEqual(valor_test, valor_esperado)

    def test_NumeroCapicua_03(self):
      valor_test = ch.numeroCapicua('hola')
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)
    
    def test_Factorial_01(self):
      valor_test = ch.factorial(6)
      valor_esperado = 720
      self.assertEqual(valor_test, valor_esperado)

    def test_Factorial_02(self):
      valor_test = ch.factorial(9)
      valor_esperado = 362880
      self.assertEqual(valor_test, valor_esperado)
    
    def test_ProximoPrimo_01(self):
      valor_test = ch.proximoPrimo(61)
      valor_esperado = 67
      self.assertEqual(valor_test, valor_esperado)

    def test_ProximoPrimo_02(self):
      valor_test = ch.proximoPrimo(139)
      valor_esperado = 149
      self.assertEqual(valor_test, valor_esperado)

    def test_ProximoPrimo_03(self):
      valor_test = ch.proximoPrimo(200)
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)
    
    def test_FactorizarNumero_01(self):
      valor_test = ch.factorizarNumero(5)
      valor_esperado = [[5],[1]]
      self.assertEqual(valor_test, valor_esperado)

    def test_FactorizarNumero_02(self):
      valor_test = ch.factorizarNumero(1428)
      valor_esperado = [[2,3,7,17], [2,1,1,1]]
      self.assertEqual(valor_test, valor_esperado)

    def test_FactorizarNumero_03(self):
      valor_test = ch.factorizarNumero('cinco')
      valor_esperado = None
      self.assertEqual(valor_test, valor_esperado)
    
    def test_ListaDeListas_01(self):
      lista_test = ch.listaDeListas((100,101))
      lista_esperada = None
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaDeListas_02(self):
      lista_test = ch.listaDeListas([0,1,[2,3],[[4,5],6],[[7]],8,[8,9,10]])
      lista_esperada = [0,1,2,3,4,5,6,7,8,8,9,10]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaDeListas_03(self):
      lista_test = ch.listaDeListas(['a','b',1,2,['a1','b3'],[['a'],2]])
      lista_esperada = ['a','b',1,2,'a1','b3','a',2]
      self.assertEqual(lista_test, lista_esperada)
    
    def test_ClaseVehiculo_01(self):
      a = ch.claseVehiculo('auto','gris')
      valor_test = a.Acelerar(50)
      valor_test = a.Acelerar(100)
      valor_test = a.Acelerar(-30)
      valor_esperado = 70
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseVehiculo_02(self):
      a = ch.claseVehiculo('camion','blanco')
      valor_test = a.Acelerar(20)
      valor_test = a.Acelerar(-30)
      valor_esperado = 0
      self.assertEqual(valor_test, valor_esperado)

    def test_ClaseVehiculo_03(self):
      a = ch.claseVehiculo('moto','negra')
      valor_test = a.Acelerar(10)
      valor_esperado = 10
      self.assertEqual(valor_test, valor_esperado)
    
    def test_ListaDivisibles_01(self):
      lista_test = ch.listaDivisibles(12, 10)
      lista_esperada = []
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaDivisibles_02(self):
      lista_test = ch.listaDivisibles(12, 100)
      lista_esperada = [12,24,36,48,60,72,84,96]
      self.assertEqual(lista_test, lista_esperada)

    def test_ListaDivisibles_03(self):
      lista_test = ch.listaDivisibles(3, 9)
      lista_esperada = [3,6,9]
      self.assertEqual(lista_test, lista_esperada)
    
resultado_test = unittest.main(argv=[''], verbosity=2, exit=False)

hc_tests = resultado_test.result.testsRun
hc_fallas = len(resultado_test.result.failures)
hc_errores = len(resultado_test.result.errors)
hc_ok = hc_tests - hc_fallas - hc_errores

archivo_test = open('resultado_test.csv', 'w')
archivo_test.write('Total_Tests,Total_Fallas,Total_Errores,Total_Correctos\n')
archivo_test.write(str(hc_tests)+','+str(hc_fallas)+','+str(hc_errores)+','+str(hc_ok)+'\n')
archivo_test.close()

print('Resumen')
print('Total Tests:', str(hc_tests))
print('Total Fallas:', str(hc_fallas))
print('Total Errores:', str(hc_errores))
print('Total Correctos:', str(hc_ok))