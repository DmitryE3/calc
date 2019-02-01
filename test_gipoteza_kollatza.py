import unittest
import Gipoteza_kollatza

class TestKollatza(unittest.TestCase):
    def test_gipoteza_kollatza(self):
        self.assertEqual(Gipoteza_kollatza.gipoteza_kollatza(12),9)

if __name__=='__main__':
    unittest.main()