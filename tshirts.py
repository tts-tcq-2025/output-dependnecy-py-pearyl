
def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42: # to fix bug, update cms > 38 to cms >= 38
        return 'M'
    else:
        return 'L'


assert(size(37) == 'S')
assert(size(38) == 'M')  # Added test to catch the bug
assert(size(40) == 'M')
assert(size(43) == 'L')
print("All is well (maybe!)")
