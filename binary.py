# =====================================================================
# PART 1: STRING COMPRESSION & DECOMPRESSION
# =====================================================================

def compress_string(s: str) -> str:
    if not s:
        return ""
    compressed = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            compressed.append(s[i-1] + (str(count) if count > 1 else ""))
            count = 1
    compressed.append(s[-1] + (str(count) if count > 1 else ""))
    return "".join(compressed)


def decompress_string(s: str) -> str:
    decompressed = []
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        count = int(num_str) if num_str else 1
        decompressed.append(char * count)
    return "".join(decompressed)


# =====================================================================
# PART 2: VALIDATE BINARY SEARCH TREE (BST)
# =====================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: TreeNode) -> bool:
    def validate(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (validate(node.left, low, node.val) and 
                validate(node.right, node.val, high))
                
    return validate(root)


# =====================================================================
# RUNNING YOUR SPECIFIC INPUT EXAMPLE
# =====================================================================
if __name__ == "__main__":
   
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    # Validate and convert the boolean (True/False) to an integer (1/0)
    result = isValidBST(root)
    output = int(result)

    print(f"Output: {output}")
