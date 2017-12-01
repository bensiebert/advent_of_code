def solve(nums):
    nums = str(nums)
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return int(nums[0])

    matching_nums = []
    for idx, curr_num in enumerate(nums):
        try:
            next_num = nums[idx+1]
        except IndexError:
            next_num = nums[0]

        if curr_num == next_num:
            matching_nums.append(int(curr_num))

    return sum(matching_nums)

if __name__ == "__main__":
    import sys
    numbers = sys.stdin.read().strip()
    solution = solve(numbers)
    print(solution)
