import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_frequency_table(text):
    frequency = defaultdict(int)
    for char in text:
        frequency[char] += 1
    return frequency

def build_huffman_tree(frequency):
    priority_queue = []
    for char, freq in frequency.items():
        node = HuffmanNode(char=char, freq=freq)
        heapq.heappush(priority_queue, node)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(freq=left.freq + right.freq, left=left, right=right)
        heapq.heappush(priority_queue, merged)
    
    return heapq.heappop(priority_queue) if priority_queue else None

def build_codebook(root, current_code="", codebook=None):
    if codebook is None:
        codebook = {}
    
    if root is None:
        return
    
    if root.char is not None:
        codebook[root.char] = current_code
        return
    
    build_codebook(root.left, current_code + "0", codebook)
    build_codebook(root.right, current_code + "1", codebook)
    
    return codebook

def huffman_encoding(text):
    if not text:
        return {}
    
    frequency = build_frequency_table(text)
    
    if len(frequency) == 1:
        char = next(iter(frequency.keys()))
        return {char: "0"}
    
    huffman_tree = build_huffman_tree(frequency)
    codebook = build_codebook(huffman_tree)
    
    return codebook

def main():
    text = input("Введіть рядок для кодування Гафмана: ")
    codebook = huffman_encoding(text)
    
    for char, code in codebook.items():
        print(f'"{char}": {code}')

if __name__ == "__main__":
    main()