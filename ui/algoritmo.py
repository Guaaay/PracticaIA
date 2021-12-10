from queue import PriorityQueue
from database import *
'''
diccionario de arrays que tiene como key el nombre de la estación y como value el array de los vecinos de dicha estación
calculamos el tiempo total como la suma de los caminos entre nodos vecinos y al final le sumamos el total de paradas realizadas por el metro*20s
nuestra función recibe como parámetros de entrada el nodo de inicio y del final del trayecto
'''
''' def reconstruct_path(came_from, actual, draw):
		while actual in came_from:
        	actual = came_from[actual]
        	actual.make_path()
        	draw() '''


class Algoritmo():
    def __init__(self, start, end, map):
        self.start = lines_number_station[start]
        self.end = lines_number_station[end]
        self.map = map

    def best_route(self):
        count = 0
        open_set = PriorityQueue()
        open_set.put((0, count, self.start))
        came_from = {}
        g_n = {}
        for nodo in self.map:
            g_n[nodo] = float("inf")
        #g_n = {spot: float("inf") for row in grid for spot in row}
        g_n[self.start] = 0
        #f_n = {spot: float("inf") for row in grid for spot in row}
        f_n = {}
        for nodo in self.map:
            f_n[nodo] = float("inf")
        # poner nuestra estimación
        f_n[self.start] = self.h(self.start, self.end)
        open_set_hash = {self.start}

        while not open_set.empty():
            # for event in pygame.event.get():
            # 	if event.type == pygame.QUIT:
            # 		pygame.quit()

            actual = open_set.get()[2]
            open_set_hash.remove(actual)

            if actual == self.end:
                res = [actual]
                while actual in came_from:
                    actual = came_from[actual]
                    res.append(actual)

                return res.reverse()
            for vecino in self.map[actual]:
                temp_g_n = g_n[actual] + get_time(actual, vecino) ## función de ruben y vinh que devuelve el tiempo entre estaciones vecinas
                if temp_g_n < g_n[vecino]:
                    came_from[vecino] = actual
                    g_n[vecino] = temp_g_n
                    f_n[vecino] = temp_g_n + self.h(vecino, self.end)
                    if vecino not in open_set_hash:
                        count += 1
                        open_set.put((f_n[vecino], count, vecino))
                        open_set_hash.add(vecino)
                        #vecino.make_open() # grafico: marcar nodo como abierto

            if actual != self.start:
                pass
                #actual.make_closed() # grafico: marcar nodo como visitado

        return None

    def h(self,p1, p2):
        return get_time(p1,p2) * 1.5

	
