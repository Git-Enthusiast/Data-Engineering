# TASK: Use the debugger to find the bug.
# A mark equal to the pass mark IS a pass.
# Expected: 4 students passed.


def count_passes(marks, pass_mark):
    """Return how many marks are at or above the pass mark."""
    count = 0
    for mark in marks:
        if mark > pass_mark:
            count += 1
    return count


marks = [40, 55, 39, 70, 40]
print("Passes:", count_passes(marks, 40))
