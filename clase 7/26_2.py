import funciones_autos
auto1 = funciones_autos.hacer_auto('Toyota', 'Corolla', color='gris', airbags=True)
print("Import módulo:", auto1)
print("")
from funciones_autos import hacer_auto
auto2 = hacer_auto('Ford', 'Mustang', color='rojo', motor='V8')
print("From módulo import función:", auto2)
print("")
from funciones_autos import hacer_auto as ha
auto3 = ha('Honda', 'Civic', color='azul', transmisión='automática')
print("From módulo import función as alias:", auto3)
print("")
import funciones_autos as fa
auto4 = fa.hacer_auto('Chevrolet', 'Camaro', color='negro', convertible=True)
print("Import módulo as alias:", auto4)
print("")
from funciones_autos import *
auto5 = hacer_auto('BMW', 'M3', color='blanco', techo_solar=True)
print("From módulo import * :", auto5)