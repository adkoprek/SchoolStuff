def subset_sum(set, sum):
    generation_table = [False] * (sum + 1)
    generation_table[0] = True

    for number in set:
        for i in reversed(range(sum + 1)):
            if generation_table[i] and number + i < sum:
                generation_table[number + i] = True 

    return generation_table[sum]

set = [3, 24, 4, 12, 5, 2]
print(subset_sum(set, 9))
