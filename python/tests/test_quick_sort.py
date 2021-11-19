import pytest
from code_challenges.quick_sort.quick_sort import quickSort

def test_1():
  data1=[2,1,8,4,3]
  quickSort(data1)
  assert [1,2,3,4,8]==data1

  data2=[8,4,23,42,16,15]
  quickSort(data2)
  assert [4,8,15,16,23,42]==data2

  data3=[20,18,12,8,5,-2]
  quickSort(data3)
  assert [-2,5,8,12,18,20]==data3

  data4=[5,12,7,5,5,7]
  quickSort(data4)
  assert [5,5,5,7,7,12]==data4

  data5=[2,3,5,7,13,11]
  quickSort(data5)
  assert [2,3,5,7,11,13]==data5

  data6=[20,18,12,8,5,-2]
  quickSort(data6)
  assert [-2,5,8,12,18,20]==data6