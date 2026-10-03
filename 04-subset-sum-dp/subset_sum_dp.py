def subset_sum_dp(nums, target, show=False):
    """Track which sums are reachable, instead of trying every subset."""
    reachable = {0}
    for x in nums:
        new_sums = set()
        for s in reachable:
            if s + x <= target:
                new_sums.add(s + x)
        reachable |= new_sums
        if show:
            print(f"after {x}: {sorted(reachable)}")
    return target in reachable


if __name__ == "__main__":
    print(subset_sum_dp([1, 2, 4], 7, show=True))
    print(subset_sum_dp(list(range(1, 31)), 100))
