#! /usr/python3
"""Trie implementation for Python3
I am writing this on a train so be nice.
It's for fun, okay?"""

class Trie(object):
    def __init__(self):
        self.root = Node("", 0)


class Node(object):
    """fields:
    key: the word
    value: the times this word has been mapped in this spot
    children: a list of child nodes
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.children = []

    def add_child(self, key):
        child = self.get_child(key)
        if not child:
            child = Node(key, 0)
            self.children.append(child)
        child.value += 1
        return child

    def get_child(self, key):
        for child in self.children:
            if child.key == key:
                return child
        return None
    
    def __str__(self):
        return self.key

    def __repr__(self):
        return "Key: {}, Value: {}".format(self.key, self.value)

def write_to_trie(s):
    sentences = s.split("\n")
    for i, sentence in enumerate(sentences):
        sentence = sentence.strip()
        sentences[i] = sentence.split()
    # eliminate blank lines
    sentences = [s for s in sentences if s]
    trie = Trie()
    cur = trie.root
    for sentence in sentences:
        if sentence:
            for word in sentence:
                cur = cur.add_child(word)
            cur.add_child("EOS")
        else:
            print("BLANK LINE")
        cur = trie.root
    return trie