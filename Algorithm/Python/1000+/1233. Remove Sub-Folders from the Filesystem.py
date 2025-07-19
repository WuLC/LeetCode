from collections import defaultdict

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = Node("")
        folder.sort()
        return [f for f in folder if not self.is_subfolder(f, root)]
    
    def is_subfolder(self, folder, root):
        curr, result = root, False
        for s in folder.strip('/').split('/'):
            if s in curr.next:
                if curr.next[s].is_folder:
                    result = True
            else:
                curr.next[s] = Node(s)
            curr = curr.next[s]
        curr.is_folder = True
        return result

class Node:
    def __init__(self, val):
        self.val = val
        self.is_folder = False
        self.next = defaultdict(Node)