import argparse
import random
import timeit
from timeit import Timer

def get_me_random_list(n):
  a_list = random.sample(range(n), 500)
  random.shuffle(a_list)
  return a_list

t1 = get_me_random_list(500)
t2 = get_me_random_list(1000)
t3 = get_me_random_list(5000)
    
def sequential_search(a_list, item):
  pos = 0
  found = False

  while pos < len(a_list) and not found:
    if a_list[pos] == item:
      found = True
    else:
      pos = pos + 1

  return found


def ordered_sequential_search(a_list, item):
  pos = 0
  found = False
  stop = False
  while pos < len(a_list) and not found and not stop:
    if a_list[pos] == item:
      found = True
    else:
      if a_list[pos] > item:
        stop = True
      else:
        pos = pos+1
  
  a_list = a_list.sort()

  return found


def binary_search_iterative(a_list, item):
  first = 0
  last = len(a_list) - 1
  found = False

  while first <= last and not found:
    midpoint = (first + last) // 2
    if a_list[midpoint] == item:
      found = True
    else: 
      if item < a_list[midpoint]:
        last = midpoint - 1
      else: 
        first = midpoint + 1

  a_list = a_list.sort()

  return found
    
    
def binary_search_recursive(a_list,item):
  if len(a_list) == 0:
    return False
  else:
    midpoint = len(a_list) // 2
    if a_list[midpoint] == item:
      return True
      a_list = a_list.sort()
    else:
      if item < a_list[midpoint]:
        return binary_search_recursive(a_list[:midpoint], item)
      else:
        return binary_search_recursive(a_list[midpoint + 1:], item)


sequential_search_t1 = Timer('sequential_search(t1, 99999999)', 'from __main__ import sequential_search, t1, random')
sequential_search_t2 = Timer('sequential_search(t2, 99999999)', 'from __main__ import sequential_search, t2, random')
sequential_search_t3 = Timer('sequential_search(t3, 99999999)', 'from __main__ import sequential_search, t3, random')

ordered_sequential_search_t1 = Timer('ordered_sequential_search(t1, 99999999)', 'from __main__ import ordered_sequential_search, t1, random')
ordered_sequential_search_t2 = Timer('ordered_sequential_search(t2, 99999999)', 'from __main__ import ordered_sequential_search, t2, random')
ordered_sequential_search_t3 = Timer('ordered_sequential_search(t3, 99999999)', 'from __main__ import ordered_sequential_search, t3, random')

binary_search_iterative_t1 = Timer('binary_search_iterative(t1, 99999999)', 'from __main__ import binary_search_iterative, t1, random')
binary_search_iterative_t2 = Timer('binary_search_iterative(t2, 99999999)', 'from __main__ import binary_search_iterative, t2, random')
binary_search_iterative_t3 = Timer('binary_search_iterative(t3, 99999999)', 'from __main__ import binary_search_iterative, t3, random')

binary_search_recursive_t1 = Timer('binary_search_recursive(t1, 99999999)', 'from __main__ import binary_search_recursive, t1, random')
binary_search_recursive_t2 = Timer('binary_search_recursive(t2, 99999999)', 'from __main__ import binary_search_recursive, t2, random')
binary_search_recursive_t3 = Timer('binary_search_recursive(t3, 99999999)', 'from __main__ import binary_search_recursive, t3, random')


def sequential_timer(a_list, item, timer_function):
  return sequential_search(a_list, item), 'Sequential Search of took %10.7f seconds to run, on average' % (timer_function.timeit(number=100))


def ordered_sequential_timer(a_list, item, timer_function):
  return ordered_sequential_search(a_list, item), 'Ordered Sequential Search of took %10.7f seconds to run, on average' % (timer_function.timeit(number=100))


def binary_search_iterative_timer(a_list, item, timer_function):
  return binary_search_iterative(a_list, item), 'Binary Search Iterative of took %10.7f seconds to run, on average' % (timer_function.timeit(number=100))


def binary_search_recursive_timer(a_list, item, timer_function):
  return binary_search_recursive(a_list, item), 'Binary Search Recursive of took %10.7f seconds to run, on average' % (timer_function.timeit(number=100))


def main():
  print(sequential_timer(t1, 99999999, sequential_search_t1))
  print(sequential_timer(t2, 99999999, sequential_search_t2))
  print(sequential_timer(t3, 99999999, sequential_search_t3))
  print(ordered_sequential_timer(t1, 99999999, ordered_sequential_search_t1)) 
  print(ordered_sequential_timer(t2, 99999999, ordered_sequential_search_t2)) 
  print(ordered_sequential_timer(t3, 99999999, ordered_sequential_search_t3)) 
  print(binary_search_iterative_timer(t1, 99999999, binary_search_iterative_t1)) 
  print(binary_search_iterative_timer(t2, 99999999, binary_search_iterative_t2)) 
  print(binary_search_iterative_timer(t3, 99999999, binary_search_iterative_t3)) 
  print(binary_search_recursive_timer(t1, 99999999, binary_search_recursive_t1)) 
  print(binary_search_recursive_timer(t2, 99999999, binary_search_recursive_t2)) 
  print(binary_search_recursive_timer(t3, 99999999, binary_search_recursive_t3))


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main()