from itertools import combinations


def solve(nums, target):
    """Try every subset until one adds up to target."""
    for size in range(len(nums) + 1):
        for indices in combinations(range(len(nums)), size):
            if sum(nums[i] for i in indices) == target:
                return list(indices)
    return None


def verify(nums, target, indices):
    """Check a proposed answer in one pass."""
    return sum(nums[i] for i in indices) == target


if __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2]
    answer = solve(nums, target=9)
    print(answer)
    print(verify(nums, 9, answer))
