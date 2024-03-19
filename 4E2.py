def reverse_range(list, start, end):
    rev=[]
    it = 0
    while it < start:
        rev.append(list[it])
        it += 1
    it = end
    while it >= start:
        rev.append(list[it])
        it -= 1
    it = end + 1
    while it < len(list):
        rev.append(list[it])
        it += 1
    return rev
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse_range(L,3,6))
