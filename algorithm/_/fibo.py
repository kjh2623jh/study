number = 100


def fibo(n):
    A = [[1, 1], [1, 0]]
    def matrix_mult(A, B):
        temp = [[0] * 2 for _ in range(2)]
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    temp[i][j] += (A[i][k] * B[k][j])
        return temp

    def matrix_pow(n, M):
        if n == 1:
            return M
        if n % 2 == 0:
            temp = matrix_pow(n//2, M)
            return matrix_mult(temp, temp)
        else:
            temp = matrix_pow(n-1, M)
            return matrix_mult(temp, M)

    return matrix_pow(n, A)[1][0]
print(fibo(number))


def fibo1(n):
    SIZE = 2
    ZERO = [[1,0],[0,1]]
    BASE = [[1,1],[1,0]]

    def square_matrix_mul(a, b, size=SIZE):
        new = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                for k in range(size):
                    new[i][j] += a[i][k] * b[k][j]
        
        return new
    
    def get_nth(n):
        matrix = ZERO.copy()
        k = 0
        tmp = BASE.copy()

        while 2 ** k <= n:
            if n & (1 << k) != 0:
                matrix = square_matrix_mul(matrix, tmp)
            k += 1
            tmp = square_matrix_mul(tmp, tmp)
        
        return matrix
    
    return get_nth(n)[1][0]
print(fibo1(number))


def fibo2(n):
    sqrt5 = 5**(1/2)
    return int((1/sqrt5)*(((1 + sqrt5) / 2) ** n - ((1 - sqrt5) / 2) ** n))
print(fibo2(number))


def fibo3(n):
    def matrix_s(m):            # 행렬 곱, 입력에는 초기 행렬이나, 현재 결과 행렬만 들어온다.
        a, b = result_arr[0]    # 결과행렬이 들어오는 경우는 제곱, 아니면 곱이다.
        c, d = result_arr[1]
        e, f = m[0]
        g, h = m[1]
        result_arr[0][0] = (a * e + b * g) % 1_000_000_007
        result_arr[0][1] = (a * f + b * h) % 1_000_000_007
        result_arr[1][0] = (c * e + d * g) % 1_000_000_007
        result_arr[1][1] = (c * f + d * h) % 1_000_000_007

    def recur(n):   # 거듭제곱 분할정복
        if n == 1:
            return

        if n // 2:
            recur(n // 2)
            matrix_s(result_arr)   # 제곱 연산

        if n % 2:
            matrix_s(first_arr) # 그냥 곱 연산

    first_arr = [[1, 1], [1, 0]]       # 초기 행렬
    result_arr = [[1, 1], [1, 0]]      # 결과 행렬
    recur(n - 1)
    return result_arr[0][0] % 1_000_000_007
print(fibo3(number))


def fibo4(n):
    if n < 2:
        return n
    cache = [0 for _ in range(n+1)]
    cache[1] = 1
    
    for i in range(2, 100+1):
        cache[i] = cache[i-1] + cache[i-2]

    return cache[n]
print(fibo4(number))


def fibo5(n, __cache={0: 0, 1: 1}):
    """Get nth fibonacci number"""
    if n in __cache:
        return __cache[n]

    __cache[n] = fibo5(n-1) + fibo5(n-2)
    return __cache[n]
fibo5(number)
