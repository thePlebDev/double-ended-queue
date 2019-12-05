from collections import deque
class ArrayDeque:
    '''full implementation of a deque. Deque is used for the underlying storage
    trying to keep the deque circular using cyclic shifts'''
    DEFAULT_CAPACITY = 10
    '''the length of the deque is predefined, in order to keep the deque circular'''

    def __init__(self):
        self._data = deque([None]) * ArrayDeque.DEFAULT_CAPACITY 
        '''this is creating the deque with the max length'''
        self._size = 0
        self._front = 0

    def is_empty(self):
        '''checks to see if the instance varible _size is 0 (meaning the deque
        is empty. returns a boolean value'''

        return self._size == 0

    def first(self):
        ''' raises an exception if the deque is empty

        returns but does not remove the element at the front of the deque'''
        if self.is_empy():
            raise Empty('the deque is empty')
        return self._data[self._front]
    
        
    def __len__(self):
        ''' Returns the number of the instance varible _size
        it is the number of actual elements in the list '''
        return self._size

    def last():
        ''' return but do not remove the last element of the deque. an error
    occurs if the deque is empty'''
        if self.is_empty():
            raise Empty('the deque is empyt')
        back = (self._front +self._size - 1) % len(self._data)
        return self._data[back]
        
