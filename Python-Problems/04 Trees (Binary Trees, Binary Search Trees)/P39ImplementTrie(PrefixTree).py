"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
Implement the Trie class:
Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 
Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""
"""
Insert:
"app"
"apple"
"bat"
"ball"

Trie looks like:
root
 ├── a
 │   └── p
 │       └── p (end of "app")
 │           └── l
 │               └── e (end of "apple")
 └── b
     └── a
         ├── t (end of "bat")
         └── l
             └── l (end of "ball")
"""


# Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        # Dictionary to store child nodes: char -> TrieNode
        self.children = {}
        # Flag to indicate the end of a valid word
        self.is_end_of_word = False


class Trie(object):

    def __init__(self):
        # The root node doesn't contain any character
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        # Traverse each character in the word
        for char in word:
            # If the character is not yet in the current node's children, add it
            if char not in node.children:
                node.children[char] = TrieNode()
            # Move to the child node to add next chars subsequently
            node = node.children[char]
        # # After inserting all characters, mark the last node as the end of a word
        node.is_end_of_word = True


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            # If the character is not yet in the current node's children, add it
            if char not in node.children:
                return False
            # Move to the child node to add next chars subsequently
            node = node.children[char]
        # Return True only if the last node is marked as the end of a word
        return node.is_end_of_word


    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            # If the character is not yet in the current node's children, add it
            if char not in node.children:
                return False
            # Move to the child node to add next chars subsequently
            node = node.children[char]
        # If all characters in the prefix are found, return True
        return True


# Your Trie object will be instantiated and called as such:
obj = Trie()
print(obj)
print(obj.insert("apple"))
print(obj.search("apple"))
print(obj.search("app"))
print(obj.startsWith("app"))
print(obj.insert("app"))
print(obj.search("app"))
