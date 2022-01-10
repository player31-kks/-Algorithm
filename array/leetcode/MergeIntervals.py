from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    result = [intervals[0]]
    for interval in intervals[1:]:
        incoming_start, incoming_end = interval
        current_start, current_end = result[-1]
        if incoming_start <= current_end:
            result.pop()
            result.append([min(current_start, incoming_start), max(current_end, incoming_end)])
        else:
            result.append(interval)
    return result


if __name__ == '__main__':
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(merge([[1,4],[4,5]]))
