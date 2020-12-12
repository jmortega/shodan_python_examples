#!/usr/bin/env python

import shodan
import re


class ShodanSearch:
	""" Clase para buscar en Shodan """

	def __init__(self, API_KEY):
		self.api = shodan.Shodan(API_KEY)

	def buscar(self, cadena):
		""" Busca segun la cadena dada """
		try:
			# Buscamos lo de la cadena pasada como parametro
			resultado = self.api.search(str(cadena))
			return resultado
		except Exception as exception:
			print('Ha ocurrido un error: %s' % exception)
			resultado = []
		return resultado

	def obtener_info_host(self, IP):
		""" Obtiene la info que pueda tener shodan sobre una IP """
		try:
			resultados = self.api.host(IP)
			return resultados
		except Exception as exception:
			print('Ha ocurrido un error: %s' % exception)
			resultados = []
		return resultados


def uso():
	print("""Uso: ShodanSearch.py {OPTION} {CADENA | HOST}
	 OPCIONES:
	  -s, --search: Para buscar segun una determinada cadena
	  -h, --host: Para obtener la informacion de un host segun su IP
	 EJEMPLOS
	  ShodanSearch.py -s apache
	  ShodanSearch.py -h 8.8.8.8""")


def banner():
	print("""
		 ____  _               _             _____      
				/ ___|| |__   ___   __| | __ _ _ __
				\___ \| '_ \ / _ \ / _` |/ _` | '_ \  
				 ___) | | | | (_) | (_| | (_| | | | |  
				|____/|_| |_|\___/ \__,_|\__,_|_| |_|
											   Search
	""")


def main():
	import sys
	import time

	API_KEY = ''
	shodan = ShodanSearch(API_KEY)
	if len(sys.argv) < 3:
		uso()
		sys.exit(2)
	else:
		if sys.argv[1] == '-s' or sys.argv[1] == '--search':
			banner()
			time.sleep(3)
			resultados = shodan.buscar(sys.argv[2])

			if len(resultados) != 0:
				print('Cantidad de resultados encontrados: %s' % resultados['total'])
				for resultado in resultados['matches']:
					print('Ciudad: %s' % resultado['location']['city'])
					print('Pais: %s' % resultado['location']['country_name'])
					print('IP: %s' % resultado.get('ip_str'))
					print('O.S: %s' % resultado.get('os', 'Unknown'))
					print('Puerto: %s' % resultado.get('port'))
					print('Hostnames: %s' % resultado.get('hostnames'))
					print('Latitude: %s' % resultado['location']['latitude'])
					print('Longitude: %s' % resultado['location']['longitude'])
					print('Actualizado en: %s' % resultado.get('timestamp'))
					print(resultado['data'])

				if 'organizations' in resultados.keys():
					for key, value in resultados['organizations'].items():
						print(key + ":" + value)
				if 'countries' in resultados.keys():
					for key, value in resultados['countries'].items():
						print(key + ":" + value)
				if 'cities' in resultado.keys():
					for key, value in resultados['cities'].items():
						print(key + ":" + value)

		elif sys.argv[1] == '-h' or sys.argv[1] == '--host':
			banner()
			time.sleep(3)
			host = shodan.obtener_info_host(sys.argv[2])
			if len(host) != 0:
				# Imprimiendo la informacion obtenida
				if 'ip' in host.keys():
					print('IP: %s' % host.get('ip_str'))
				if 'country_name' in host.keys():
					print('Pais: %s' % host.get('country_name', 'Unknown'))
				if 'country_code' in host.keys():
					print('Codigo pais: %s' % host.get('country_code', 'Unknown'))
				if 'city' in host.keys():
					print('City: %s' % host.get('city', 'Unknown'))
				if 'latitude' in host.keys():
					print('Latitude: %s' % host.get('latitude'))
				if 'longitude' in host.keys():
					print('Longitude: %s' % host.get('longitude'))
				if 'hostnames' in host.keys():
					print('Hostnames: %s' % host.get('hostnames'))
				print("----------------------------------")
				# Imprimimos los banners de los servidores
				try:
					for i in host['data']:
						print('Puerto: %s' % i['port'])
						print('Banner: %s' % i['data'])
				except Exception as exception:
					print(exception)
					pass
		else:
			uso()
			sys.exit(2)


if __name__ == '__main__':
	main()
