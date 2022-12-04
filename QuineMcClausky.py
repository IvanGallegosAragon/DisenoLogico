import numpy as np

def decimalBinario(numeroDecimal,numeroDeCeros):
    numeroBinario = 0
    multiplicador = 1
    while numeroDecimal != 0:
        numeroBinario = numeroBinario + numeroDecimal % 2 * multiplicador
        numeroDecimal //= 2
        multiplicador *= 10
    numeroBinario = str(numeroBinario)
    if not len(numeroBinario) == numeroDeCeros:
      for cero in range( numeroDeCeros - len(numeroBinario) ):
        numeroBinario = "0" + numeroBinario 
    return numeroBinario 

def obtenerMinterminos(listMinterminos):
  maximo = np.array(listMinterminos).max()
  noVariables = 0
  listaMinterminosBinarios = []
  #Generar el numero de variables
  while np.power(2, noVariables) < maximo:
    noVariables += 1
  for numero in listMinterminos:
    listaMinterminosBinarios.append(decimalBinario(numero,noVariables))
  return listaMinterminosBinarios

def generarBloques(listaMinterminosBinarios):
  numeroBloques = len(listaMinterminosBinarios[0])
  bloques = [ [] for noBloque in range(numeroBloques + 1)]
  for numero in listaMinterminosBinarios:
    bloques[numero.count("1")].append(numero)
  for bloque in bloques:
    if len(bloque) == 0:
      bloques.remove(bloque)
    else:
      pass
  return bloques

def comparadorBloques(bloque1,bloque2,numerosComparados,numerosNoComparados):
  bloqueComparado = []
  for elem1 in bloque1:
    for elem2 in bloque2:
      contador = 0
      nuevoElemento = ""
      for position in range(len(elem1)):
        if elem1[position] != elem2[position]:
          contador += 1
        else:
          pass   
      if contador == 1:
        for position in range(len(elem1)):
          if elem1[position] != elem2[position]:
            nuevoElemento += "*"
          else:
            nuevoElemento += elem1[position] 
        if elem1 not in numerosComparados:
          if elem1 in numerosNoComparados:
            numerosNoComparados.remove(elem1)
          numerosComparados.append(elem1)
        if elem2 not in numerosComparados:
          if elem2 in numerosNoComparados:
            numerosNoComparados.remove(elem2)
          numerosComparados.append(elem2)
        if nuevoElemento not in bloqueComparado:
          bloqueComparado.append(nuevoElemento)
      else:
        if elem1 not in numerosComparados and elem1 not in numerosNoComparados:
          numerosNoComparados.append(elem1)
        if elem2 not in numerosComparados and elem2 not in numerosNoComparados:
          numerosNoComparados.append(elem2) 
  return bloqueComparado , numerosComparados , numerosNoComparados


def minterminoModificadoVariableNoComparados(lista):
  alphabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  salida = ""
  for elemento in lista:
    contadorLetra = 0
    for letra in elemento:
      if letra == "0":
        salida += f"(¬{alphabeto[contadorLetra]})"
      elif letra == "1":
        salida += f"{alphabeto[contadorLetra]}"
      else:
        pass
      contadorLetra += 1
    if elemento != lista[-1]:
        salida += " + "  
  return salida

def minterminoModificadoVariableBloques(lista):
  alphabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  salida = ""
  for elemento in lista:
    for elementoInterno in elemento:
      contadorLetra = 0
      for letra in elementoInterno:
        if letra == "0":
          salida += f"(¬{alphabeto[contadorLetra]})"
        elif letra == "1":
          salida += f"{alphabeto[contadorLetra]}"
        else:
          pass
        contadorLetra += 1
      if elemento != lista[-1]:
          salida += " + "  
  return salida

def quineMcCluskey(lista):
  """Recibe una lista de minterminos cuales sea"""
  comparados = []
  noComparados = []
  bloques = generarBloques(obtenerMinterminos(lista))   
  noBloques = len(bloques)

  while noBloques != 1:
    borradorBloques = []
    contadorProcesos = 0
    for bloque in bloques:
      bloqueNuevo, comparados, noComparados = comparadorBloques(bloques[contadorProcesos],bloques[contadorProcesos+1],comparados,noComparados)
      borradorBloques.append(bloqueNuevo)
      contadorProcesos += 1
      if contadorProcesos == noBloques - 1:
        break   
    noBloques -= 1
    if len(borradorBloques) == 1:
        pass    
    bloques = borradorBloques  
  if len(noComparados) == 0:
    salida = minterminoModificadoVariableBloques(bloques)
  else:  
    salida = minterminoModificadoVariableNoComparados(noComparados)
  print(f"La función booleana reducida es: {salida}")
  
lista = [10,11,12,14,15,34,257,500]
quineMcCluskey(lista)












