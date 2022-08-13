from typing import Dict, Optional

Graph = Dict[Optional[str], Optional["Graph"]]


class Trie:
    def __init__(self):
        self.graph = {}

    def insert(self, word: str) -> None:
        node = self.graph
        for char in word:
            node = node.setdefault(char, {})
        node[None] = None

    def traverse(self, word: str) -> Graph:
        node = self.graph
        for char in word:
            if char in node:
                node = node[char]
            else:
                return {}
        return node

    def search(self, word: str) -> bool:
        return None in self.traverse(word)

    def starts_with(self, prefix: str) -> bool:
        return bool(self.traverse(prefix))