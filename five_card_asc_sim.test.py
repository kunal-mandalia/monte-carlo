import unittest
import five_card_asc_sim

class TestStringMethods(unittest.TestCase):
    def test_low_five_card_asc_sim(self):
        # arrange
        n = 0
        expected = set([1, 13, 25, 37])

        # act
        actual = five_card_asc_sim.get_ascending_card_range(n)

        # assert
        self.assertEquals(actual, expected)
    
    def test_high_five_card_asc_sim(self):
        # arrange
        n = 15
        expected = set([4, 16, 28, 40])

        # act
        actual = five_card_asc_sim.get_ascending_card_range(n)

        # assert
        self.assertEquals(actual, expected)

if __name__ == '__main__':
    unittest.main()
