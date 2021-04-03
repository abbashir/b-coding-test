
# ********* Problem-1 ************
def print_depth(my_dict, initial=0):
    for key, value in my_dict.items():
        print(key, initial + 1)
        if isinstance(value, dict):
            print_depth(value, initial=initial+1)


a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
        }
    }
}

print_depth(a)

# ********* Problem-2 ************
class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


person_a = Person("User", "1", None)
person_b = Person("User", "2", person_a)


def print_depth(my_dict, initial=0):
    for key, value in my_dict.items():
        print(key, initial + 1)
        if isinstance(value, dict):
            print_depth(value, initial=initial+1)
        elif isinstance(value, Person):
            return print_depth(vars(value),initial=initial+1)

a = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4,
            "user": person_b,
        }
    },
}
print_depth(a)

# ********* Problem-3 ************

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def findPath(root, path, k):

    if root is None:
        return False

    path.append(root.key)

    if root.key == k:
        return True

    if ((root.left != None and findPath(root.left, path, k)) or
            (root.right != None and findPath(root.right, path, k))):
        return True

    path.pop()
    return False


def findLCA(root, n1, n2):
    path1 = []
    path2 = []

    if (not findPath(root, path1, n1) or not findPath(root, path2, n2)):
        return -1

    i = 0
    while(i < len(path1) and i < len(path2)):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i-1]


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

root.left.left.left = Node(8)
root.left.left.right = Node(9)

print("LCA(9, 4) = ", findLCA(root, 9, 4))
print("LCA(8, 5) = ", findLCA(root, 8, 5))

print("LCA(6, 7) = ", findLCA(root, 6, 7))
print("LCA(3, 7) = ", findLCA(root, 3, 7))


# TEST METHOD
def my_sum(a,b):
    return a+b
