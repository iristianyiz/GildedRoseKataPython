# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod # ABC: Abstract Base Class


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemStrategy(ABC):
    """Abstract base class for all Item strategies."""

    # A blueprint for item strategies.
    # Each concrete strategy must implement the update_quality method.
    @abstractmethod
    def update_quality(self, item: Item):
        pass


class NormalItemStrategy(ItemStrategy):
    """Strategy for normal items that degrade in quality over time."""

    def update_quality(self, item: Item):
        if item.quality > 0:
            item.quality -= 1
        item.sell_in -= 1
        if item.sell_in < 0 < item.quality: # item.sell_in < 0 and item.quality > 0
            item.quality -= 1


class AgedBrieStrategy(ItemStrategy):
    """Strategy for Aged Brie, which increases in quality as it gets older."""

    def update_quality(self, item: Item):
        if item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0 and item.quality < 50:
            item.quality += 1


class BackstagePassStrategy(ItemStrategy):
    """Strategy for Backstage passes, which increase in quality as the concert date approaches."""

    def update_quality(self, item: Item):
        if item.quality < 50:
            item.quality += 1
        if item.sell_in < 11 and item.quality < 50:
            item.quality += 1
        if item.sell_in < 6 and item.quality < 50:
            item.quality += 1
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0


class SulfurasStrategy(ItemStrategy):
    """Strategy for Sulfuras, which never changes in quality or sell-in."""

    def update_quality(self, item: Item):
        pass  # Sulfuras doesn't need any updates


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def _get_item_strategy(self, item: Item) -> ItemStrategy:
        if item.name == "Aged Brie":
            return AgedBrieStrategy()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassStrategy()
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasStrategy()
        else:
            return NormalItemStrategy()

    def update_quality(self):
        for item in self.items:
            strategy = self._get_item_strategy(item)
            strategy.update_quality(item)