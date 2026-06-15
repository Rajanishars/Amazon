import collections

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


# Helper function to build a tree from user level-order array input
def build_tree_from_list(nodes_list):
    if not nodes_list or nodes_list[0] is None:
        return None
    
    root = TreeNode(nodes_list[0])
    queue = collections.deque([root])
    i = 1
    
    while queue and i < len(nodes_list):
        curr = queue.popleft()
        
        # Left Child
        if i < len(nodes_list) and nodes_list[i] is not None:
            curr.left = TreeNode(nodes_list[i])
            queue.append(curr.left)
        i += 1
        
        # Right Child
        if i < len(nodes_list) and nodes_list[i] is not None:
            curr.right = TreeNode(nodes_list[i])
            queue.append(curr.right)
        i += 1
        
    return root


# =====================================================================
# INTERACTIVE USER INPUT EXECUTION
# =====================================================================
if __name__ == "__main__":
    print("=== STRING OPERATIONS ===")
    user_str = input("Enter a string to compress (e.g., AAACCCBBD): ").strip()
    comp = compress_string(user_str)
    print(f"Compressed Output: {comp}")
    print(f"Decompressed back: {decompress_string(comp)}\n")

    print("=== BINARY SEARCH TREE (BST) VALIDATOR ===")
    print("Enter tree nodes row-by-row (Level-Order) separated by spaces.")
    print("Use 'None' or 'null' for missing/empty nodes.")
    print("Example for your valid tree (2 / \\ 1 3), enter: 2 1 3")
    
    tree_input = input("Enter tree nodes: ").strip().split()
    
    # Parse input strings into integers or None
    parsed_list = []
    for item in tree_input:
        if item.lower() in ["none", "null"]:
            parsed_list.append(None)
        else:
            parsed_list.append(int(item))
            
    # Build the tree from the parsed list
    root_node = build_tree_from_list(parsed_list)
    
    # Validate and display result as 1 or 0
    is_bst = isValidBST(root_node)
    print(f"Output: {int(is_bst)}")
