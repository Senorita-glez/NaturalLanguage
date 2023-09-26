def eliminarCaracteres(cadena):
    caracteresP = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZéíóúá '
    cadenaN = ''
    for c in cadena:
        if c in caracteresP:
            cadenaN += c
    return cadenaN

def detalles(cadena):
    detalles = []
    detalles.append(cadena.split())
    detalles.append([''] * len(detalles[0]))
    detalles.append([''] * len(detalles[0]))
    return detalles

def sujeto(detalles):
    for i in range(len(detalles)):
        palabra = detalles[0][i]
        if palabra[0].isupper():
            detalles[1][i] = 'sujeto'
            return detalles

def verbo(detalles):
    for i in range(len(detalles)+1):
        palabra = detalles[0][i]
        if detalles[1][i] == '':
            if palabra[len(palabra)-1] in 'áéíóú':
                detalles[1][i] = 'verbo pasado'
                detalles[2][i] = palabra[:-1]
                return detalles
            elif palabra[-2:] == 'ar' or palabra[-2:] == 'er' or palabra[-2:] == 'ir':
                detalles[1][i] = 'verbo infinitivo'
                detalles[2][i] = palabra[:-2]
                return detalles
            elif (palabra[-4:] == 'ando' ):
                detalles[1][i] = 'verbo gerundio'
                detalles[2][i] = palabra[:-4]
                return detalles
            elif palabra[-5:] == 'iendo':
                detalles[1][i] = 'verbo gerundio'
                detalles[2][i] = palabra[:-5]
                return detalles
            elif (palabra[-3:] == 'aba'):
                detalles[1][i] = 'verbo pretérito imperfecto del singular 3ra o 1era persona '
                detalles[2][i] = palabra[:-3]
                return detalles
            elif palabra[-4:] == 'aban':
                detalles[1][i] = 'verbo pretérito imperfecto tercera persona del plural'
                detalles[2][i] = palabra[:-4]
                return detalles
            elif palabra[-6:] == 'abamos' or palabra[-6:] == 'ábamos':
                detalles[1][i] = 'verbo pretérito imperfecto primera persona del plural'
                detalles[2][i] = palabra[:-6]
                return detalles
            elif palabra[-4:] == 'abas':
                detalles[1][i] = 'verbo pretérito imperfecto singular'
                detalles[2][i] = palabra[:-4]
                return detalles

def sustantivo(detalles):
    for i in range(len(detalles[0])):
        palabra = detalles[0][i]
        cont = 0;
        if detalles[1][i] == '':
            if palabra[-1] == 's':
                detalles[1][i] = 'plural '
                cont =cont + 1
            else:
                detalles[1][i] = 'singular '
            if palabra[-1] == 'o' or palabra[-2] == 'o':
                detalles[1][i] += 'masculino'
                cont =cont + 1
            elif palabra[-1] == 'a' or palabra[-2] == 'a':
                detalles[1][i] += 'femenino'
                cont =cont + 1
            else:
                detalles[1][i] += 'género desconocido'
            if cont != 0:
                detalles[2][i] = palabra[:-cont]
            else: 
                detalles[2][i] = 'la misma palabra'
    return detalles

def tokenize(oracion):
    res = eliminarCaracteres(oracion)
    res = detalles(res)
    res = sujeto(res)
    res= verbo(res)
    res = sustantivo(res)
    print(oracion)
    print()
    for i in range(len(res[0])):
        if res[1][i] == 'sujeto':  
            print(f"{res[0][i]} -> Es un {res[1][i]}")
        else:
            print(f"{res[0][i]} -> Es {res[1][i]} y su raíz es {res[2][i]}")
        

oracion = 'hablabamos Nosotros morse'
tokenize(oracion);
