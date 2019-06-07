Bienvenidos a Peloni Pizzas.

pizzas = ["Suprema" , "Cuatro estaciones", "Salmon ahumado y queso crema", 
"De pan frances", " De ziti", "Jamon y queso",
"Pizza blanca", "De ensalada", "Pizza baggel",
"Siciliana", "Cuatro quesos", "De atun y maiz dulce"]

def imprimir_menu():
	print("1 mostrar pizza ")
	print("2 mostrar pizza ")
	print("3 agregar pizza ")
	print("4 agregar pizza ")
	print("5 agregar pizza ")
	print("6 agregar pizza ")
	print("7 agregar pizza ")
	print("8 agregar pizza ")
	print("9 agregar pizza ")
	print("10 agregar pizza ")
	print("11 agregar pizza ")
	print("12 salir ")
	valor = input("ingrese el valor de la accion: ")
	return valor 

continuar = True 

while continuar:
	#v_retornado = Valor Retornado
	v_retornado = imprimir_menu()
	if int(v_retornado) == 1:
		for pizza in pizzas:
			print(pizza)
	elif int(v_retornado) == 2 :
		pizzas  = []
	elif int(v_retornado) == 3:
		valor = input("ingrese la pizza  a agregar")
		pizza.append (valor)
	elif int(v_retornado) == 4: 	
		pizzas  = []
	elif int(v_retornado) == 5:
		pizzas  = []
	elif int(v_retornado) == 6:
		pizzas  = []
	elif int(v_retornado) == 7:
		pizzas  = []
	elif int(v_retornado) == 8:
		pizzas  = []
	elif int(v_retornado) == 9:
		pizzas  = []
	elif int(v_retornado) == 10:
		pizzas  = []
	elif int(v_retornado) == 11:
		pizzas  = []
	elif int(v_retornado) == 12: 	
		continuar = False
	else:
		print("opcion no controlada")
