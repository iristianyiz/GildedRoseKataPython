# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("fixme", items[0].name)

    def test_invalid_quality(self):  # quality is > 50
        items = [Item("apple", 0, 52)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(52, items[0].quality)

    def test_aged_brie_quality(self):  # quality
        items = [Item("Aged Brie", 1, 1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].quality) # should be 2

    def test_sulfuras_quality(self):  # Sulfuras never has to be sold or decreases in Quality
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 15)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(16, items[0].quality)  # should be 15


if __name__ == '__main__':
    unittest.main()
