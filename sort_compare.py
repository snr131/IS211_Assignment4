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
    

def insertion_sort(a_list):
  for index in range(1, len(a_list)):

    current_value = a_list[index]
    position = index

    while position > 0 and a_list[position - 1] > current_value:
      a_list[position] = a_list[position - 1]
      position = position - 1

    a_list[position] = current_value


def shell_sort(a_list):
  sublist_count = len(a_list) // 2
  while sublist_count > 0:
    for start_position in range(sublist_count):
      gap_insertion_sort(a_list, start_position, sublist_count)

    #print('After increments of size', sublist_count, 'the list is', a_list)
    sublist_count = sublist_count // 2

def gap_insertion_sort(a_list, start, gap):
  for i in range(start + gap, len(a_list), gap):
    current_value = a_list[i]
    position = i

    while position >= gap and a_list[position - gap] > current_value:
      a_list[position] = a_list[position - gap]
      position = position - gap

  a_list[position] = current_value


def python_sort(a_list):
  a_list = a_list.sort()
  return a_list


insertion_sort_t1 = Timer('insertion_sort(t1)', 'from __main__ import insertion_sort, t1, random')
insertion_sort_t2 = Timer('insertion_sort(t2)', 'from __main__ import insertion_sort, t2, random')
insertion_sort_t3 = Timer('insertion_sort(t3)', 'from __main__ import insertion_sort, t3, random')

shell_sort_t1 = Timer('shell_sort(t1)', 'from __main__ import shell_sort, t1, random')
shell_sort_t2 = Timer('shell_sort(t2)', 'from __main__ import shell_sort, t2, random')
shell_sort_t3 = Timer('shell_sort(t3)', 'from __main__ import shell_sort, t3, random')

python_sort_t1 = Timer('python_sort(t1)', 'from __main__ import python_sort, t1, random')
python_sort_t2 = Timer('python_sort(t2)', 'from __main__ import python_sort, t2, random')
python_sort_t3 = Timer('python_sort(t3)', 'from __main__ import python_sort, t3, random')


def insertion_sort_timer(a_list, timer_function):
  return 'Insertion Sort of took %10.7f seconds to run, on average' % (timer_function.timeit(number=100))

def shell_sort_timer(a_list, timer_function):
  return 'Shell Sort of took %10.7f seconds to run, on average' % (timer_function.timeit(number=100))

def python_sort_timer(a_list, timer_function):
  return 'Python Sort of took %10.7f seconds to run, on average' % (timer_function.timeit(number=100))


def main():
  print(insertion_sort_timer(t1, insertion_sort_t1))
  print(insertion_sort_timer(t2, insertion_sort_t2))
  print(insertion_sort_timer(t3, insertion_sort_t3)) 
  print(shell_sort_timer(t1, shell_sort_t1)) 
  print(shell_sort_timer(t2, shell_sort_t2)) 
  print(shell_sort_timer(t3, shell_sort_t3)) 
  print(python_sort_timer(t1, python_sort_t1)) 
  print(python_sort_timer(t2, python_sort_t2)) 
  print(python_sort_timer(t3, python_sort_t3))


if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main()








