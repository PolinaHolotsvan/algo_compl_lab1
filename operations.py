from copy import copy, deepcopy

example1 = [
    "+ nun",
    "+ mom",
    "+ mom",
    "? mom",  # yes
    "- mom",
    "? mom",  # no
    "? dad",  # no
    "+ dog",
    "+ taco cat",
    "+ evil olive",
    "? evil olive",  # yes
    "& mom"  # invalid operation, pass
    "+ yo banana boy",
    "+ dad",
    "+ step on no pets",
    "- evil olive"
    "+ no lemon no melon",
    "+ do geese see god",
    "? dad",  # yes
    "+ geese do see god",
    "+ cool geese",
    "? evil olive"  # no
    "+ egad an adage",
    "#",  # further operations wouldn't be performed
    "? dd",
    "+ aaaa",
    "- aaaa"
]

example2 = ["+ mom", "- mom"] * ((10 ** 6) // 2)

example3 = deepcopy(example2)
example3.append("? mom")  # len = 10^6+1 elements
