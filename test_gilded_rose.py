# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_vest_item_should_decrease_after_one_day(self):

        vest = "+5 Dexterity Vest"
        items = [Item(vest, 1, 2), Item(vest, 9, 19), Item(vest, 4, 6), ]
        gr = GildedRose(items)
        gr.update_quality()
        assert gr.get_items_by_name(vest) == [Item(vest, 0, 1), Item(vest, 8, 18), Item(vest, 3, 5)]

    def test_aged_brie_should_increase_quality_after_one_day(self):
        brie = "Aged Brie"
        items = [Item(brie, 2, 0), Item(brie, 1, 1), Item(brie, 0, 2)]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.get_items_by_name(brie) == [Item(brie, 1, 1), Item(brie, 0, 2), Item(brie, -1, 4)]


    def test_backstage_passes_quality_increase(self):
        pass_item = "Backstage passes to a TAFKAL80ETC concert"
        items = [Item(pass_item, 15, 20), Item(pass_item, 10, 30), Item(pass_item, 5, 40)]
        gr = GildedRose(items)

        gr.update_quality()
        assert gr.get_items_by_name(pass_item) == [Item(pass_item, 14, 21), Item(pass_item, 9, 32), Item(pass_item, 4, 43)]


    def test_sulfuras_quality_should_not_change(self):
        sulfuras = "Sulfuras, Hand of Ragnaros"
        items = [Item(sulfuras, 0, 80), Item(sulfuras, -1, 80)]
        gr = GildedRose(items)

        gr.update_quality()
        assert gr.get_items_by_name(sulfuras) == [Item(sulfuras, 0, 80), Item(sulfuras, -1, 80)]



    def test_conjured_item_quality_decreases_faster(self):
        conjured = "Conjured Mana Cake"
        items = [Item(conjured, 3, 6), Item(conjured, 1, 5), Item(conjured, 0, 4)]
        gr = GildedRose(items)

        gr.update_quality()

        assert gr.get_items_by_name(conjured) == [Item(conjured, 2, 5), Item(conjured, 0, 4), Item(conjured, -1, 2)]


if __name__ == '__main__':
    unittest.main()
