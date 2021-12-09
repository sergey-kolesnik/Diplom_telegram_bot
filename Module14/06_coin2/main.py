def metal_detector_request_calculation():
  x_coordinate = float(input('Введите координату ИКС: '))
  y_coordinate = float(input('Введите координату ИГРЕК: '))
  radius = float(input('Введиту радиус: '))
  if (x_coordinate ** 2 + y_coordinate ** 2) ** 0.5 <= radius:
      print('Монетка рядом.')
  else:
      print('Монетки в области нет.')



metal_detector_request_calculation()
