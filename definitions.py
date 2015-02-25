# Determina si realmente es aleatorio el algoritmo del profe

def get_digits(num, base=10):
    while True:
        res = num%base
        yield res
        num = num//base
        if num==0:
            break

def digit_reduce(num):
    while num>=10:
        num = sum(get_digits(num))
    return num

if __name__ == '__main__':
    # get_digits assertions
    assert tuple(get_digits(0))   == (0,)
    assert tuple(get_digits(9))   == (9,)
    assert tuple(get_digits(11))  == (1,1)
    assert tuple(get_digits(111)) == (1, 1, 1)
    assert tuple(get_digits(123)) == (3, 2, 1)
    assert tuple(get_digits(90, 60))   == (30, 1)
    assert tuple(get_digits(120, 60))  == (0, 2)
    assert tuple(get_digits(141, 60))  == (21, 2)
    assert tuple(get_digits(0, 60))    == (0,)
    assert tuple(get_digits(1, 60))    == (1,)
    assert tuple(get_digits(3600, 60)) == (0, 0, 1)
    assert tuple(get_digits(3666, 60)) == (6, 1, 1)

    # digit_reduce assertions
    assert digit_reduce(0) == 0
    assert digit_reduce(1) == 1
    assert digit_reduce(2) == 2
    assert digit_reduce(3) == 3
    assert digit_reduce(4) == 4
    assert digit_reduce(5) == 5
    assert digit_reduce(6) == 6
    assert digit_reduce(7) == 7
    assert digit_reduce(8) == 8
    assert digit_reduce(9) == 9
    assert digit_reduce(21) == 3
    assert digit_reduce(211) == 4
    assert digit_reduce(99) == 9
    assert digit_reduce(999) == 9
    assert digit_reduce(23998249249249427942987429428742987429842794274297429) == 1

