# https://www.acmicpc.net/problem/2448

# 3, 6, 12, 24, 48, ...

def star_min():
    return ["  *  ", " * * ", "*****"]

def combine_stars(tri):
    len_tri = len(tri)
    def top_space():
        return list(map(lambda line: " " * len_tri + line + " " * len_tri, tri))
    def add_space():
        return list(map(lambda line: line + " " + line, tri))
    return [*top_space(), *add_space()]

def print_star(number):
    cache = {3: star_min()}
    if number in cache:
        return cache[number]
    else:
        cache[number] = combine_stars(print_star(number // 2))
        return cache[number]

number = int(input())
result = print_star(number)
print('\n'.join(result))