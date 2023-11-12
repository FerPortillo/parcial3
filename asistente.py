https://replit.com/join/kuggrjxspl-fernandaportil3 
def detectar_alexa(texto):
  texto_en_minusculas = texto.lower()

  palabras = texto_en_minusculas.split()

  veces_alexa = palabras.count('alexa')

  if veces_alexa == 1:
      print("Hola, soy Alexa.")
  elif veces_alexa > 1:
      print("Tranquilo, solo di mi nombre una vez.")
  else:
      print("No mencionaste mi nombre.")

texto_usuario = input("Escribe algo: ")
detectar_alexa(texto_usuario)
