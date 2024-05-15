import unittest
import sys
import os

# Agregar la ruta completa del directorio que contiene 'grafo.py' al path
sys.path.append("C:/Users/2004e/HDT10/src")


from grafo import Grafo, leer_archivo_logistica

class TestGrafo(unittest.TestCase):
    def setUp(self):

        # Crea un grafo de ejemplo para las pruebas
        self.grafo = Grafo(4)
        self.grafo.agregar_arista(0, 1, 10)
        self.grafo.agregar_arista(0, 2, 15)
        self.grafo.agregar_arista(2, 3, 10)

    def test_floyd_warshall(self):
        distancias_esperadas = [
            [0, 10, 15, 25],
            [float('inf'), 0, float('inf'), float('inf')],
            [float('inf'), float('inf'), 0, 10],
            [float('inf'), float('inf'), float('inf'), 0]
        ]
        self.assertEqual(self.grafo.floyd_warshall(), distancias_esperadas)

    def test_leer_archivo_logistica(self):
        # Especificamos la dirección completa del archivo logistica.txt
        grafo_logistica = leer_archivo_logistica("C:/Users/2004e/HDT10/src/logistica.txt")
     
        self.assertEqual(grafo_logistica.num_vertices, 4)
        self.assertEqual(grafo_logistica.adj_matrix[0][1], 10)
        self.assertEqual(grafo_logistica.adj_matrix[0][2], 15)
        self.assertEqual(grafo_logistica.adj_matrix[2][3], 10)

if __name__ == '__main__':
    unittest.main()
