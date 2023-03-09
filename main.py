
def twoSum(nums, target):

    # print(nums)
    # print(target)
    
    length = len(nums)
    # print(length)
    
    start =0
    end =0
    
    for i in range(length):
        for j in range(i+1,length):
            if target == nums[i] + nums[j]:
                start = i
                end =j
    
    # print("answer is ",start,end)
    return [start,end]

# twoSum([2,7,11,15],9)

