https://replit.com/join/qunlorqwme-fernandaportil3
def calcular_porcentaje_error(lecturas):
  lecturas_correctas = 0
  lecturas_incorrectas = 0

  rango_min = 10
  rango_max = 40

  for lectura in lecturas:
      if rango_min <= lectura <= rango_max:
          lecturas_correctas += 1
      else:
          lecturas_incorrectas += 1
  total_lecturas = len(lecturas)
  porcentaje_error = (lecturas_incorrectas / total_lecturas) * 100

  print(f"Lecturas correctas: {lecturas_correctas}")
  print(f"Lecturas incorrectas: {lecturas_incorrectas}")
  print(f"Porcentaje de error: {porcentaje_error:.2f}%")

lecturas_simuladas = [12, 15, 18, 25, 30, 42, 8, 38, 20, 10]
calcular_porcentaje_error(lecturas_simuladas)
