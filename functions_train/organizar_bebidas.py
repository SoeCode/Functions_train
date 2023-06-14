#programa para categorizar os produtos de uma revendedora de bebidas.
#Cada produto tem um código. O tipo de produto é dado pelas 3 primeiras letras do código.
# bebidas não alcóolicas começam com BSA e bebidas alcoolicas começam com BEB.
#programa que analise uma lista de produtos e envie instruções para a equipe de estoque dizendo quais produtos devem ser enviados para a área de bebidas alcóolicas.
produtos = ['beb46275','TFA23962','TFA64715',
            'TFA69555','TFA56743','BSA45510',
            'TFA44968','CAR75448','CAR23596',
            'CAR13490','BEB21365','BEB31623',
            'BSA62419','BEB73344','TFA20079',
            'BEB80694','BSA11769','BEB19495',
            'TFA14792','TFA78043','BSA33484',
            'BEB97471','BEB62362','TFA27311',
            'TFA17715','BEB85146','BEB48898',
            'BEB79496','CAR38417','TFA19947',
            'TFA58799','CAR94811','BSA59251',
            'BEB15385','BEB24213','BEB56262',
            'BSA96915','CAR53454','BEB75073'
]
def ehalcoolico(bebida):
    bebida = bebida.upper()
    if 'BEB' in bebida:
        return True
    else:
        return False
    
#percorrer lista
#verificar se a bebida é alcoolica
#imprimir para mandar para o setor
for produto in produtos:
    if ehalcoolico(produto):
        print(f' Enviar {produto} para o setor de bebidas alcóolicas.')
#argumento simples