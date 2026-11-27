import unittest

from buscas import BuscaLinearSentinela, busca_binaria
from medicoes import medir_sort_nativo
from ordenacao import insertion_sort, merge_sort, selection_sort


class TestOrdenacoes(unittest.TestCase):
    def test_ordena_listas(self):
        casos = ([], [7], [1, 2, 3], [3, 2, 1], [3, -1, 3, 0])

        for ordenar in (selection_sort, insertion_sort, merge_sort):
            for lista in casos:
                with self.subTest(algoritmo=ordenar.__name__, lista=lista):
                    self.assertEqual(ordenar(lista.copy()), sorted(lista))


class TestBuscas(unittest.TestCase):
    def test_busca_binaria(self):
        casos = (
            ([-7, 9, 20], -7, 0),
            ([-7, 9, 20], 9, 1),
            ([-7, 9, 20], 20, 2),
            ([-7, 9, 20], 8, -1),
            ([], 20, -1),
        )

        for lista, alvo, indice in casos:
            with self.subTest(lista=lista, alvo=alvo):
                self.assertEqual(busca_binaria(lista, alvo), indice)

    def test_busca_linear_com_sentinela(self):
        casos = (
            ([0, 9, -7], 0, (0, 0)),
            ([5, 9, 9], 9, (1, 9)),
            ([20, 9, -7], -7, (2, -7)),
            ([20, 9, -7], 40, (-1, 0)),
            ([], 20, (-1, 0)),
        )

        for lista, alvo, esperado in casos:
            with self.subTest(lista=lista, alvo=alvo):
                entrada = lista.copy()
                self.assertEqual(BuscaLinearSentinela(entrada, alvo), esperado)
                self.assertEqual(entrada, lista)


class TestMedicoes(unittest.TestCase):
    def test_sort_nativo_preserva_lista_original(self):
        lista = [3, -1, 3, 0]

        tempo = medir_sort_nativo(lista, 3)

        self.assertIsInstance(tempo, int)
        self.assertGreaterEqual(tempo, 0)
        self.assertEqual(lista, [3, -1, 3, 0])
