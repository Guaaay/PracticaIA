import os
estaciones = os.path.dirname(__file__)
files = os.listdir(estaciones)
linea3dir = estaciones + '\\linea3\\'
linea3 = os.listdir(estaciones + '\\linea3\\')
#linea 3
print(linea3)
for i, file in enumerate(linea3):
    if(i<18):
        num = 310 + i
        os.rename(os.path.join(linea3dir, file),os.path.join(linea3dir, str(num) + '.png'))
