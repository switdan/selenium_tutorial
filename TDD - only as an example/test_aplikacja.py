import unittest
from TDD.aplikacja import Czlowiek

class TestCzlowiek(unittest.TestCase):
    def setUp(self):
        self.czlowiek = Czlowiek("Stasio")
    # Metody testowe muszą się zaczynać od słowa "test"
    def testPierwszy(self):
        przedstawienie_str = self.czlowiek.przedstaw_sie()
        self.assertEqual("Cześć, jestem Stasio", przedstawienie_str)
    def tearDown(self):
        del self.czlowiek

if __name__ == '__main__':
    unittest.main()