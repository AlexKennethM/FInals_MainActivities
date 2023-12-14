class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def verticalTraversal(root, hd, m): #Recursively traverses the binary tree in a vertical order and stores nodes at each horizontal distance in the dictionary 'm'.


    if root is None:
        return

    try:
        m[hd].append(root.key)
    except:
        m[hd] = [root.key]

    verticalTraversal(root.left, hd + 1, m)
    verticalTraversal(root.right, hd - 1, m)


def display(root): #Displays the vertical order traversal of the binary tree fromr ightmost to leftmost level.


    m = dict()
    hd = 0
    verticalTraversal(root, hd, m)
    sample = []

    print()
    print("Vertical traversal from rightmost to leftmost: ")
    for index, value in enumerate(sorted(m, reverse=True)):
        for i in (m[value]):
            sample.append(i)

    print(str(sample[::-1]))  # Reverses the entire list


if __name__ == '__main__':
    # Example usage
    root = Node(1)
    root.right = Node(3)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.right = Node(8)
    root.right.right.right = Node(9)

    root.left = Node(2)
    root.left.right = Node(5)
    root.left.left = Node(4)
    display(root)
