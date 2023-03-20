from random_list import make_random_list

sample_list = make_random_list(20, 0, 100)

def find_sum_pair(lst, target):
    sorted_list = sorted(lst)
    left = 0
    right = len(sorted_list) - 1
    print(f"Finding pairs that equal to {target} from {sorted_list}")

    while left < right:
        if sorted_list [left] + sorted_list [right] == target:
            return (sorted_list [left], sorted_list [right])
        
        if sorted_list [left] + sorted_list [right] < target:
            left = left + 1
        else:
            right = right - 1

    print("No pairs sum to the target")

print(sample_list)
print(find_sum_pair(sample_list, 115))

# Write your solution for algorithm 5 below
"""
def find_pair(lst, target):
    sorted_list = sorted(lst)
    left = 0
    right = len(sorted_list)-1

    while left < right:
        if sorted_list[left] + sorted_list[right] == target:
            return(sorted_list[left], sorted_list[right])
        
        if sorted_list[left] + sorted_list[right] < target:
            left = left + 1
        else: 
            right = right - 1
    
    return('no pairs sum to the target')

sample_list = [ 3, 7, 6, 8]
print(find_pair(sample_list, 9))
"""