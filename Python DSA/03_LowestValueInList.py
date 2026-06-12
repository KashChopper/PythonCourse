my_Array = [2,4,5,3,8,9,3]

minValue = my_Array[0]

for i in my_Array:
    if i < minValue:
        minValue = i

print(minValue)


"""
| i value | Condition `i < lowest_value` | lowest_value |
| ------- | ---------------------------- | ------------ |
| 3       | 3 < 3 → False                | 3            |
| 4       | 4 < 3 → False                | 3            |
| 2       | 2 < 3 → True                 | 2            |
| 4       | 4 < 2 → False                | 2            |
| 7       | 7 < 2 → False                | 2            |
| 8       | 8 < 2 → False                | 2            |
| 6       | 6 < 2 → False                | 2            |
| 7       | 7 < 2 → False                | 2            |

"""