#entrada al parque

print("\tBienvenido a Luna park")
name = input("Cual es tu nombre?: ")
old = int(input("que edad tienes:"))

if old >= 12 and old <=16:
	print("hola {} tu puedes entrar a los carros chocones".format(name))
elif old <12:
	print("hola {} tu puedes entrar al castillo inflable".format(name))
elif old >16:
	print("hola {} tu puedes entrar a carros chocones, punteria o rueda de la fortuna".format(name))
