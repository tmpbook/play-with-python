# coding:utf8
def quick_sort(the_list):
    if not isinstance(the_list, list):
        return
    if len(the_list) < 2:
        # 基线条件
        return the_list
    else:
        # 递归条件：这里为了简单选择第一个元素作为基准值
        pivot = the_list[0]

        # 所有大于基准值的元素组成的子数组
        greater = [i for i in the_list[1:] if i > pivot]

        # 所有小于等于基准值的元素组成的子数组
        less = [i for i in the_list[1:] if i <= pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == "__main__":
    print(quick_sort([11, 3, 2, 1, 5, 10]))

# output:
# [1, 2, 3, 5, 10, 11]
