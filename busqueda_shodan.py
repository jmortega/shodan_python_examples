import shodan

API_KEY= ""
shodan = shodan.Shodan(API_KEY)

try:
    resultados = shodan.search('elasticSearch')
    print("Numero de resutlados:",resultados.items())
    # mostrar los resultados
    print('Resultados: %s' % resultados['total'])
    for resultado in resultados['matches']:
        print('IP: %s' % resultado['ip_str'])
        print(resultado['data'])
except Exception as exception:
    print(str(exception))
