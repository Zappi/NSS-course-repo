def print_one_to_twenty():
    numbers = []
    for i in range(1, 21):
        numbers.append(i)
    return numbers


def reverse_array(number_array):
    number_array.reverse()
    return number_array


def write_file(textArr):
    f = open('demo.txt', 'w')
    for text in textArr:
        f.write(str(text) + "\n")
    f.close()

    f = open('demo.txt', 'r')


def read_file(fileName):
    sum = 0
    f = open(fileName, 'r')
    for value in f:
        sum += int(value)

    return sum


def main():
    print(print_one_to_twenty())
    print(reverse_array(print_one_to_twenty()))
    write_file([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    sum = read_file('demo.txt')
    print(sum)


if __name__ == '__main__':
    main()
