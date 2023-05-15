total_preguntas = 10
lista_respuestas = []

archivo_math = open("test_math.csv","r")
encabezado = True
for linea in archivo_math:
    if (not encabezado):
        lista_respuestas.append(linea.split(sep=',')[1].replace('\n',''))
    else:
        encabezado = False
archivo_math.close()

if(len(lista_respuestas) != total_preguntas):
    i = 0
    while(i < total_preguntas):
        lista_respuestas.append('') 
        i+=1

opciones_esperadas = ['1a','1b','2a','2b','2c','2d','2e','2f','2g','2h','3']
continuar = True
while(continuar):
    print('HENRY CHALLENGE - MATEMÁTICA')
    print('****************************')
    print('Tus respuestas:')
    print('* 1a:', lista_respuestas[0])
    print('* 1b:', lista_respuestas[1])
    print('* 2a:', lista_respuestas[2])
    print('* 2b:', lista_respuestas[3])
    print('* 2c:', lista_respuestas[4])
    print('* 2d:', lista_respuestas[5])
    print('* 2e:', lista_respuestas[6])
    print('* 2f:', lista_respuestas[7])
    print('* 2g:', lista_respuestas[8])
    print('* 2h:', lista_respuestas[9])
    print('* 3 - Para terminar')
    op = input('Por favor, ingresa la opción que quieras cargar: ')
    if(op == '1a'):
        r = input('Ingresa tu respuesta: ')
        try:
            if(r!='NULL'):
                r = float(r)
                lista_respuestas[0] = str(r)
            else:
                lista_respuestas[0] = 'NULL'
        except:
            r = ''
            print('Por favor, ingresar un formato correcto')
    elif(op == '1b'):
        r = input('Ingresa tu respuesta: ')
        try:
            if(r!='NULL'):
                r = float(r)
                lista_respuestas[1] = str(r)
            else:
                lista_respuestas[1] = 'NULL'
        except:
            r = ''
            print('Por favor, ingresar un formato correcto')
    elif(op == '2a'):
        r = input('Ingresa tu respuesta: ').lower()
        if (r == 'verdadero'):
            lista_respuestas[2] = 'Verdadero'
        elif (r == 'falso'):
            lista_respuestas[2] = 'Falso'
        else:
            print('Por favor, ingresar Verdadero o Falso')
    elif(op == '2b'):
        r = input('Ingresa tu respuesta: ').lower()
        if (r == 'verdadero'):
            lista_respuestas[3] = 'Verdadero'
        elif (r == 'falso'):
            lista_respuestas[3] = 'Falso'
        else:
            print('Por favor, ingresar Verdadero o Falso')
    elif(op == '2c'):
        r = input('Ingresa tu respuesta: ').lower()
        if (r == 'verdadero'):
            lista_respuestas[4] = 'Verdadero'
        elif (r == 'falso'):
            lista_respuestas[4] = 'Falso'
        else:
            print('Por favor, ingresar Verdadero o Falso')
    elif(op == '2d'):
        r = input('Ingresa tu respuesta: ').lower()
        if (r == 'verdadero'):
            lista_respuestas[5] = 'Verdadero'
        elif (r == 'falso'):
            lista_respuestas[5] = 'Falso'
        else:
            print('Por favor, ingresar Verdadero o Falso')
    elif(op == '2e'):
        r = input('Ingresa tu respuesta: ').lower()
        if (r == 'verdadero'):
            lista_respuestas[6] = 'Verdadero'
        elif (r == 'falso'):
            lista_respuestas[6] = 'Falso'
        else:
            print('Por favor, ingresar Verdadero o Falso')
    elif(op == '2f'):
        r = input('Ingresa tu respuesta: ').lower()
        if (r == 'verdadero'):
            lista_respuestas[7] = 'Verdadero'
        elif (r == 'falso'):
            lista_respuestas[7] = 'Falso'
        else:
            print('Por favor, ingresar Verdadero o Falso')
    elif(op == '2g'):
        r = input('Ingresa tu respuesta: ').lower()
        if (r == 'verdadero'):
            lista_respuestas[8] = 'Verdadero'
        elif (r == 'falso'):
            lista_respuestas[8] = 'Falso'
        else:
            print('Por favor, ingresar Verdadero o Falso')
    elif(op == '2h'):
        r = input('Ingresa tu respuesta: ').lower()
        if (r == 'verdadero'):
            lista_respuestas[9] = 'Verdadero'
        elif (r == 'falso'):
            lista_respuestas[9] = 'Falso'
        else:
            print('Por favor, ingresar Verdadero o Falso')
    elif(op == '3'):
        continuar = False
    else:
        print('Debes ingresar una de las opciones esperadas. Gracias.')

archivo_math = open("test_math.csv","w")
archivo_math.write('pregunta,respuesta\n')
i = 0
while (i < total_preguntas):
    archivo_math.write(opciones_esperadas[i]+','+str(lista_respuestas[i])+'\n')
    i+=1
archivo_math.close()
