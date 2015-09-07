# -*- coding: utf-8 -*-

def edades(edad):
	"""
	Ademas de ser comenatios se puede utilizar para hacer pruebas sencillas
	>>> edades(5)
	Eres niño
	
	"""
	if edad < 0:
		print ("No existes")
	elif edad < 13:
		print ("Eres niño")
	elif edad < 18:
		print ("Eres adolecente") 
	elif edad < 65:
		print ("Eres adulto")
	elif edad < 120:
		print ("Eres adulto mayor")
	else:
		print ("Eres mum-ra")


if __name__=="__main__":
	import doctest
	doctest.testmod()
