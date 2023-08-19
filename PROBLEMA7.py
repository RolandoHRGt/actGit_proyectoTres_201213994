textos = []
for i in range(15):
    texto = input(f"Ingrese el texto {i + 1}: ")
    textos.append(texto)

textos_finaliza_con_vocal = [i for i in textos if i[-1].lower() in 'aeiou']
textos_menos_10_caracteres = [j for j in textos if len(j) < 10]
contador_hola = textos.count('hola')

print("Textos que finalizan con vocal:", textos_finaliza_con_vocal)
print("Textos con menos de 10 caracteres:", textos_menos_10_caracteres)
print("Cantidad de veces que se repite 'hola':", contador_hola)