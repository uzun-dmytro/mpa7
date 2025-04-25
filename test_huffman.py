import unittest
import io
import sys
from huffman import HuffmanNode, huffman_encoding, build_frequency_table, build_huffman_tree, build_codebook

class TestHuffmanEncoding(unittest.TestCase):
    def test_build_frequency_table(self):
        self.assertEqual(build_frequency_table("aabbbc"), {'a': 2, 'b': 3, 'c': 1})
        self.assertEqual(build_frequency_table(""), {})
        self.assertEqual(build_frequency_table("   "), {' ': 3})

    def test_build_huffman_tree(self):
        frequency = {'a': 2, 'b': 3, 'c': 1}
        tree = build_huffman_tree(frequency)
        self.assertEqual(tree.freq, 6)
        
    def test_build_codebook(self):
        left = HuffmanNode(char='a', freq=2)
        right_right = HuffmanNode(char='b', freq=3)
        right_left = HuffmanNode(char='c', freq=1)
        right = HuffmanNode(freq=4, left=right_left, right=right_right)
        root = HuffmanNode(freq=6, left=left, right=right)
        
        codebook = build_codebook(root)
        self.assertEqual(len(codebook), 3)
        self.assertEqual(set(codebook.keys()), {'a', 'b', 'c'})

    def test_huffman_encoding(self):
        result = huffman_encoding("aabbbc")
        self.assertEqual(len(result), 3)
        self.assertEqual(sorted(result.keys()), ['a', 'b', 'c'])
        # Перевірка унікальності кодів
        codes = list(result.values())
        self.assertEqual(len(codes), len(set(codes)))
        # Перевірка префіксності
        for code1 in codes:
            for code2 in codes:
                if code1 != code2:
                    self.assertFalse(code1.startswith(code2))

    def test_single_char(self):
        self.assertEqual(huffman_encoding("aaaaa"), {'a': '0'})

    def test_empty_string(self):
        self.assertEqual(huffman_encoding(""), {})

if __name__ == '__main__':
    unittest.main()