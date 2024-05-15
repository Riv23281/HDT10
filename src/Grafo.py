class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]
        for i in range(num_vertices):
            self.adj_matrix[i][i] = 0

    def agregar_arista(self, inicio, fin, peso):
        if inicio < self.num_vertices and fin < self.num_vertices:
            self.adj_matrix[inicio][fin] = peso
        else:
            print("Error: Los índices de los vértices están fuera de rango.")

    def floyd_warshall(self):
        distancias = [row[:] for row in self.adj_matrix]
        for k in range(self.num_vertices):
            for i in range(self.num_vertices):
                for j in range(self.num_vertices):
                    distancias[i][j] = min(distancias[i][j], distancias[i][k] + distancias[k][j])
        return distancias

    def imprimir_matriz_adyacencia(self):
        for fila in self.adj_matrix:
            print(fila)


def leer_archivo_logistica(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()
        ciudades = {}
        indice = 0
        for linea in lineas:
            if not linea.startswith("Ciudad"):  # Omitir la línea de encabezado
                ciudad1, ciudad2, tiempo_normal, _, _, _ = linea.split()
                if ciudad1 not in ciudades:
                    ciudades[ciudad1] = indice
                    indice += 1
                if ciudad2 not in ciudades:
                    ciudades[ciudad2] = indice
                    indice += 1
        num_ciudades = len(ciudades)
        print("Número de ciudades:", num_ciudades)
        grafo = Grafo(num_ciudades)
        for linea in lineas:
            if not linea.startswith("Ciudad"):  # Omitir la línea de encabezado
                ciudad1, ciudad2, tiempo_normal, _, _, _ = linea.split()
                inicio = ciudades[ciudad1]
                fin = ciudades[ciudad2]
                grafo.agregar_arista(inicio, fin, int(tiempo_normal))
        return grafo


# Ejemplo de uso
grafo = leer_archivo_logistica("C:/Users/2004e/HDT10/src/logistica.txt")

print("Matriz de adyacencia:")
grafo.imprimir_matriz_adyacencia()

distancias = grafo.floyd_warshall()
print("\nMatriz de distancias más cortas:")
for fila in distancias:
    print(fila)
