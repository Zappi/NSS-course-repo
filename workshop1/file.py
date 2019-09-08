def write_file(textArr):
    f = open('demo.txt', 'w')
    for text in textArr:
        f.write(str(text) + "\n")
    f.close()

    f = open('demo.txt', 'r')


write_file([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def read_file(fileName):
    sum = 0
    f = open(fileName, 'r')
    for value in f:
        sum += int(value)

    return sum


sum = read_file('demo.txt')
print(sum)
