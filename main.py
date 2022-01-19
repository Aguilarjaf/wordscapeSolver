import enchant
from itertools import combinations, permutations

dictionary = enchant.Dict("en_US")

print("Welcome to the WordScape solver!\n")

while True:
    x = input("Please enter your given characters (Type \"Stop\" to Exit): ")

    if x == "Stop":
        break

    print("\nCalculating all combinations and permutations...\n")

    valid_words = []

    array = [''.join(l) for i in range(len(x)) for l in combinations(x, i+1)]

    for s in array:
        if len(s) >= 3:
            perms = [''.join(p) for p in permutations(s)]

            for x in perms:
                if dictionary.check(x):
                    if not valid_words.__contains__(x):
                        valid_words.append(x)

    print(f"All valid combinations/permutations include: \n\n{valid_words}\n");