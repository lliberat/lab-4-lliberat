# PQueue Data Definition (SORTED LINKEDLIST IMPLEMENTATION, the end is actually beginning)
# A PQueue is PQueue(LinkedList, comes_before)
# the LinkedList is sorted by priority of elements, wherein highest priority elements are at the end of the list.
class PQueue:
   def __init__(self, sorted_list, comes_before):
      self.sorted_list = sorted_list
      self.size = 0
      self.comes_before = comes_before
   def __repr__(self):
      return "PQueue({}, {})".format(self.sorted_list, self.comes_before)
   def __eq__(self, other):
      return ((type(other) == PQueue)
        and (self.sorted_list == other.sorted_list) and (self.comes_before == other.comes_before)
        )

# OrderingFunction -> PQueue
# this function takes an ordering function and returns an empty priority queue.
def empty_pqueue(comes_before):
   return PQueue(None, comes_before)


# PQueue Value -> PQueue
# adds the value to the queue. This operation is typically written to add the element not at the end of the queue (as would be the case for a standard queue), but in the appropriate position within the internal list as determined by the ordering function.As such, searching for the position at which to insert should begin at the head of the backing list. 
def enqueue(p_queue, value):
   # put the element in the sorted PQueue. HIGHEST priority go at END of list.
   p_queue.sorted_list = insert(p_queue.sorted_list, value, p_queue.comes_before) # returns a LinkedList
   p_queue.size += 1
   return p_queue

# PQueue -> (removed_val, PQueue)
# removes the element at the beginning of the priority queue based on the ordering as determined by the ordering function. If there is no such element, raises an IndexError exception. REMOVAL -> O(1)
def dequeue(p_queue):
   if p_queue.size == 0:
      raise indexerror
   else:
      rm_val = p_queue.sorted_list.first
      p_queue.sorted_list = p_queue.sorted_list.rest 
      p_queue.size -= 1
      return (rm_val, p_queue)

# PQueue -> Value
# peek at the first value in the priority queue -- the HIGHEST priority value.
def peek(p_queue):
   if p_queue.size == 0:
      raise indexerror
   else:
      return p_queue.sorted_list.first

# PQueue -> int
# return the size of the PQueue
def size(p_queue):
   return p_queue.size

# PQueue -> bool
# return if empty PQueue or not.
def is_empty(p_queue):
   return p_queue.size == 0

# linked_list.py
# * dd: anylist data definition
# any_value can be of type string, float, int, etc
# anylist is one of
   # 1. none or
   # 2. pair(any_value, anylist)
class pair:
   def __init__(self, first, rest):
      self.first = first
      self.rest = rest
   def __repr__(self):
      return "pair({}, {})".format(self.first, self.rest)
   def __eq__(self, other):
      return str(self) == str(other)

# *** linked list ***

# signature: -> anylist
# purpose: takes no arguments and returns empty list
def empty_list():
   return none

# value is of any type
# index is an int
# signature: anylist index value -> anylist
# purpose: places the value at index position in the list (zero-based indexing; any element at the given index before this operation will now immediately follow the new element). if the index is invalid (i.e., less than 0 or greater than the current length), then this operation should raise an indexerror exception. (note that an index equal to the length is allowed and results in the new value being added to the end of the list.)
def add(linked_list, index, val, counter=0):
   if (linked_list == none):
      if index < 0 or index > counter: # out of bounds check. index = length allowed.
         raise indexerror
      return pair(val, none)
   else:
      if index == counter: # found the right index
         return pair(val, pair(linked_list.first, linked_list.rest))
      else:
         counter += 1
         return pair(linked_list.first, add(linked_list.rest, index, val, counter))

#signature: anylist -> int
# purpose: determines the length of anylist
def length(linked_list):
   if (linked_list == none):
      return 0
   else:
      return 1 + length(linked_list.rest)

# value is of an type
# index is an integer
# signature: anylist index -> value
# purpose: this function takes a list and an integer index as arguments and returns the value at the index position in the list (zero-based indexing). if the index is invalid (i.e., it falls outside the bounds of the list), then this operation should raise an indexerror exception.
def get(linked_list, index, counter=0):
   if (linked_list == none):
      if index < 0 or index >= counter: # out of bounds check. index = length not allowed.
         raise indexerror
   else:
      if index == counter: # found right index
         return linked_list.first
      else:
         counter += 1 
         return get(linked_list.rest, index, counter)

# value is of any type
# index is an integer
# signature: anylist index value -> anylist
# purpose: takes anylist, an integer index and another value and replaces the element at the index position in the list with the given value. if invalid, raise indexerror
def set(linked_list, index, val, counter=0):
   if (linked_list == none):
      if index < 0 or index >= counter: # out of bounds check. index = length not allowed.           
         raise indexerror
   else:
      if index == counter:
         return pair(val, linked_list.rest)
      else:
         counter += 1
         return pair(linked_list.first, set(linked_list.rest, index, val, counter))

# index is an integer
# signature: anylist index -> tuple 
# purpose: takes anylist and index and removes the element at the index position from the list. if index is invalid, raise indexerror. returns a tuple in this form: (element removed, new list)
def remove(linked_list, index):
   if linked_list == none or index < 0: # out of bounds check
      raise indexerror
   elif index == 0: # if the index is 0 we went down the list far enough to the index we're searching fori
      return (linked_list.first, linked_list.rest) # return (val to be removed, rest of the list after that val)
   else:
      result = remove(linked_list.rest, index - 1)  # result  = (val to be removed, rest of the list after that val)
      #print('result: {}'.format(result))
      new_linked_list = pair(linked_list.first, result[1]) # new_linked_list = pair(first val of list, rest of list after removed val)
      #print('new linked list: {}'.format(new_linked_list))
      prev_val = result[0] # prev_val = val removed
      #print((prev_val, new_linked_list))
      return (prev_val, new_linked_list) # (val removed, pair(first val of list, rest of list after removed val))

# signature: AnyList FunctionName -> None
# purpose: this function takes a list and a function as arguments and applies the provided function to the value at each position in the list (from left-to-right). this function does not return a meaningful value (i.e., in python it returns none).
def foreach(linked_list, func_to_do):
   if linked_list == none:
      return None
   else:
      #print('new_linked_list length: {} linked_list val {}'.format(length(new_linked_list), linked_list.first))
      func_to_do(linked_list.first)
      #print('new linked list: {}'.format(new_linked_list))
      foreach(linked_list.rest, func_to_do)

# linkedlist function -> linkedlist
# sorts the linkedlist based on less_than_function
def sort(lst, less_than_function, new_list = None):
   #print('my initial lst: {}'.format(lst))
   if lst == None:
      #print(new_list)
      return new_list
   else:
      new_list = insert(new_list, lst.first, less_than_function)
      return sort(lst.rest, less_than_function, new_list)

# linkedlist item function -> linkedlist
# inserts item into linkedlist
def insert(lst, item_to_insert, less_than_function):
   #print('my lst: {} item to insert: {}'.format(lst, item_to_insert))
   if (lst == None):
      return pair(item_to_insert, None)
   else:
      if less_than_function(lst.first, item_to_insert) == True:
         return pair(lst.first, insert(lst.rest, item_to_insert, less_than_function))
      else:
         return pair(item_to_insert, pair(lst.first, lst.rest))


import unittest


class TestPQueue(unittest.TestCase):
   def test00_interface(self):
      pass
      # test_p_queue = empty_pqueue()
      # test_p_queue = enqueue(test_p_queue, "foo")
      # print(test_p_queue)
      # test_p_queue = enqueue(test_p_queue, "hi")
      # print(test_p_queue)
      # val = peek(test_queue)
      # (dequeued_val, test_queue) = dequeue(test_queue)
      # size(test_queue)
      # is_empty(test_queue)

   def test_enqueue(self):
      def comes_before(value_one, value_two):
         if value_one < value_two:
            return True
         elif value_one > value_two:
            return False

      test_pqueue = empty_pqueue(comes_before)
      enqueue(test_pqueue, 5)
      enqueue(test_pqueue, 0)
      enqueue(test_pqueue, -1)
      enqueue(test_pqueue, -1.5)
      enqueue(test_pqueue, 1000)
      # print(test_pqueue)
      # highest priority elements go at END of list
      # self.assertEqual(test_p_queue, PQueue(Pair(1000, Pair(5, Pair(0, Pair(-1, Pair(-1.5, None))))), comes_before))

   def test_dequeue(self):
      def comes_before(value_one, value_two):
         if value_one < value_two:
            return True
         elif value_one > value_two:
            return False

      test_pqueue = empty_pqueue(comes_before)
      enqueue(test_pqueue, 5)
      enqueue(test_pqueue, 0)
      enqueue(test_pqueue, -1)
      enqueue(test_pqueue, -1.5)
      enqueue(test_pqueue, 1000)

      dequeue(test_pqueue)
      print('dqed: {}'.format(test_pqueue))

      '''with self.assertRaises(IndexError):
         dequeue(test_p_queue)'''

   def coverage(self):
      def comes_before(value_one, value_two):
         if value_one < value_two:
            return True
         elif value_one > value_two:
            return False

      repr(empty_pqueue(comes_before))


if __name__ == "__main__":
   unittest.main()