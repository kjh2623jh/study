a = [[1,2],[3,4],[5,6]]

# 방법 1. sum()
# 시스템 리소스를 많이 사용해 프로덕션 시스템에서는 권하지 않음.
print(1, sum(a, []))

# 방법 2. itertools, unpacking
import itertools
print(2, list(itertools.chain(*a)))

# 방법 3. itertools.chain
import itertools
print(3, list(itertools.chain.from_iterable(a)))

# 방법 4. list comprehension
print(4, [element for arr in a for element in arr])

# 방법 5. reduce
from functools import reduce
print(5, list(reduce(lambda x, y: x+y, a))) 

# 방법 6. reduce 2
from functools import reduce
import operator
print(6, list(reduce(operator.add, a)))

# 방법 7. numpy.flatten
import numpy
print(7, numpy.array(a).flatten().tolist())