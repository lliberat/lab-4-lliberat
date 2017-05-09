class BinarySearchTree:
    def __init__(self, left, right, value, func):
        self.left = left
        self.right = right
        self.value = value
        self.func = func

    def __eq__(self, other):
        return ((type(other) == BinarySearchTree)
          and self.left == other.left
          and self.right == other.right
          and self.value == other.value
          and self.func == other.func
        )

    def __repr__(self):
        return ("BinarySearchTree({!r}, {!r}, {!r}, {!r})".format(self.left, self.right, self.value, self.func))

def is_empty(bst):
    return bst == None

def insert(bst,val):
    if(bst.left == None and bst.right == None):
        bst.value = val
        return bst
    elif(bst.func(val,bst.value) == True):
        return insert(bst.left,val)
    else:
        return insert(bst.right,val)

def lookup(bst,val):
    if(val == bst.value):
        return True
    elif(bst.left == None and bst.right == None):
        return False
    elif(bst.func(val,bst.value) == True):
        return lookup(bst.left, val)
    else:
        return lookup(bst.right,val)

def delete(bst,val):
    if (val == bst.value):
        if(bst.func(bst.left,bst.right) == True):
            bst = bst.left
        else:
            bst = bst.right
        return bst
    elif (bst.func(val, bst.value) == True):
        return delete(bst.left, val)
    else:
        return delete(bst.right, val)

