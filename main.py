"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

def foo(x):
    if x <= 1:
      return x
    else:
      return foo(x-1) + foo(x-2)

def longest_run(mylist, key):
    run = 0
    prevVal = False
    for i in range(mylist.len()):
      if mylist[i] == key:
        run+=1
        prevVal = True
      elif mylist[i] != key: 
        prevVal = False
      elif mylist[i] == key and prevVal == False:
        run = 1
        prevVal = True
    return run

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
  result = Result(0, 0, 0, False)
  if len(mylist) == 1 and mylist[0] == key:
    result.longest_run+=1
    result.is_entire_range = True
    return result
  elif len(mylist) == 1 and mylist[0] != key:
    if result.longest_size > result.left_size:
      result.left_size = result.longest_size
    result.longest_size = 0
    result.is_entire_range = False
    return result
  elif len(mylist) == 0:
    return result
  else:
    return max(longest_run_recursive(mylist[:len(mylist)//2], key).left_size, longest_run_recursive(mylist[len(mylist)//2 + 1:], key).left_size)

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


