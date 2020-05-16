#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_weight(self):
        """Test default product weight being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_prodcut_stealability(self):
        """Test variety of product stealability case."""
        prod_01 = Product('Test Product')
        prod_02 = Product('Test Product', 1, 3)
        prod_03 = Product('Test Product', 1, 1)
        self.assertEqual(prod_01.stealability(), 'Kinda stealable.')
        self.assertEqual(prod_02.stealability(), 'Not so stealable...')
        self.assertEqual(prod_03.stealability(), 'Very stealable!')

    def test_prodcut_explosion(self):
        """Test variety of product explosion case."""
        prod_01 = Product('Test Product')
        prod_02 = Product('Test Product', flammability=0.1)
        prod_03 = Product('Test Product', flammability=2.5)
        self.assertEqual(prod_01.explode(), '...boom!')
        self.assertEqual(prod_02.explode(), '...fizzle.')
        self.assertEqual(prod_03.explode(), '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):
    """Making sure AcmeReport Methods!"""

    def test_default_num_products(self):
        """Test it really does receive a list of length 30."""
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """Test default product price being 20."""
        ADJECTIVES = ['Awesome', 'Shiny',
                      'Impressive', 'Portable', 'Improved']
        NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']
        products = generate_products()
        for product in products:
            split = product.split()
            adj = split[0]
            noun = split[1]
            self.assertIn(adj, ADJECTIVES)
            self.assertIn(noun, NOUNS)


if __name__ == '__main__':
    unittest.main()
