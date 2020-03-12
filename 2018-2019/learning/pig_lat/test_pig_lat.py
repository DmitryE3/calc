import unittest
import pig_lat


class TestPigLat(unittest.TestCase):
    def test_pig_lat(self):
        self.assertEqual(pig_lat.make_pig_lat("banana"), "ananabay")


if __name__ == "__main__":
    unittest.main()
