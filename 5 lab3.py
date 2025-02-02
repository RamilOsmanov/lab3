import itertools
def prperm():
    str = input()
    perm= itertools.permutations(str)
    for pr in perm :
        print(''.join(pr))

prperm()