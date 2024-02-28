def temp(nums):
    sum = 0
    for i in nums:
        print(nums.count(i))
        print("_______",i)
        if nums.count(i) == 1:
            sum += i
    return sum


if __name__ == '__main__':
    nums = [1, 2, 3, 2]
    # print(temp(nums))
    temp(nums)
