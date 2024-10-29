# Part 2
input = open("./2018/day_2/input.txt")
example = open("./2018/day_2/example.txt")


workingData = input.readlines()  # change to try example
# workingData = example.readlines()  # change to try example


def findBox(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums), 1):
            fst, snd = nums[i], nums[j]
            diff = []
            for k in range(len(fst)):
                if fst[k] != snd[k]:
                    diff.append(k)

            if len(diff) == 1:
                return fst[:diff[0]] + fst[diff[0] + 1:]
            
print(findBox(workingData))