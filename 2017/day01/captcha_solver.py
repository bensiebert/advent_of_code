def solve(nums, look_ahead=1):
    nums = str(nums)
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return int(nums[0])

    matching_nums = []
    for idx, curr_num in enumerate(nums):
        compare_with_idx = (idx + look_ahead) % len(nums)
        compare_with_num = nums[compare_with_idx]

        if curr_num == compare_with_num:
            matching_nums.append(int(curr_num))

    return sum(matching_nums)

if __name__ == "__main__":
    import sys
    numbers = sys.stdin.read().strip()
    solution = solve(numbers)
    print('SOLUTION #1')
    print(solution)
    solution = solve(numbers, look_ahead = len(numbers) // 2)
    print('SOLUTION #2')
    print(solution)
