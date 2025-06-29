archivo = open("tsds/words.txt")
diccionario = dict()
for linea in archivo:
      for palabra in linea.split():
        if not palabra in diccionario:
            diccionario[palabra] = 1
        else:
            diccionario[palabra] += 1
#print(diccionario)

archivo = open("tsds/words.txt")
diccionario = dict()
for linea in archivo:
      for palabra in linea.split():
        diccionario[palabra] = diccionario.get(palabra, 0) + 1
#print(diccionario)

archivo = open("tsds/words.txt")
diccionario2 = dict()
for linea in archivo:
    for palabra in linea.split(): 
        for letra in palabra:  
            letra = letra.lower()
            if letra.isalpha():
             if letra not in diccionario2:
                diccionario2[letra] = 1
             else:
                diccionario2[letra] += 1
#print(diccionario2)

archivo = open("tsds/words.txt")
diccionario2 = dict()
for linea in archivo:
    for palabra in linea.split(): 
        for letra in palabra:  
            letra = letra.lower()
            if letra.isalpha():
                diccionario2[letra] = diccionario2.get(letra, 0) + 1
                
print(diccionario2)