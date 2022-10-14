import unittest
import pizzaria as pizza
from unittest.mock import Mock

from datetime import date

def setUpModule():
    print("Iniciando módulo de teste...")
    
def tearDownModule():
    print("Encerrando módulo de teste...")

class TestModuloDivisores(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("\nExecutando setUpClass")
            
    @classmethod
    def tearDownClass(cls):
        print("\nExecutando tearDownClass")
        
    def setUp(self):
        print("\nExecutando setUp")
        
    def tearDown(self):
        print("\nExecutando tearDown")
        
    # Caso de teste: entrada 0
    def teste_nome(self):
        ingredientes = {"massa":{"fina":3.4, "grossa":5.6}, "queijo":{"cheddar":5, "prato":3}, "cobertura":{"frango":4, "presunto":10}}
        self.assertEqual(ingredientes, 31)
        pass
    
    
if __name__ == "__main__":
    unittest.main(verbosity=2)
