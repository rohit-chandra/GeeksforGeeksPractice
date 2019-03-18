from collections import Counter

testcase = int(input())

for i in range(testcase):
    str_length = int(input())
    in_string = input()
    # build hash map :- character and how often it appears
    counter = Counter(in_string)

    k = -1 # keeping a count for in case we don't have non repeating values

    # compare given string with hasmap key. if key's value is 1 then print the key
    for j in in_string:
        if counter[j] == 1:
            print(j)
            k = k+1
            break

    if k == -1:
        print(-1)