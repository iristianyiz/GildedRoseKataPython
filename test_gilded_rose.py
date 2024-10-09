# -*- coding: utf-8 -*-
import unittest


from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_aged_brie_quality(self):  # quality is > 50
        items = [Item("Aged Brie", 0, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_apple_quality(self):  # quality
        items = [Item("apple", 1, 12)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(11, items[0].quality)

    def test_sulfuras_quality(self):  # Sulfuras never has to be sold or decreases in Quality
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 15)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(15, items[0].quality)  # should be 15

if __name__ == '__main__':
    unittest.main()
