def minimun(array1, array2):
    array1.sort()
    array2.sort()
    largest = abs(max(array1) + max(array2))
    x = 0
    y = 0
    ans = []
    while x < len(array1) and y < len(array2):
        firstnum = array1[x]
        secondnum = array2[y]
        if firstnum < secondnum:
            least = secondnum - firstnum
            x += 1
        elif secondnum < firstnum:
            least = firstnum - secondnum
            y += 1
        else:
            return [array1[x], array2[y]]
        if least < largest:
            largest = least
            ans = [firstnum, secondnum]
    return ans


a = [-1, 5, 10, 20, 28, 3, 12]
b = [26, 134, 135, 15, 17, 12]
print(minimun(a, b))
