def binary_search(intervals, query):
    left, right = 0, len(intervals) - 1

    while left <= right:
        mid = (left + right) // 2
        if intervals[mid] <= query:
            left = mid + 1
        else:
            right = mid - 1

    return left

def count_intervals(intervals, query_points):
    start_intervals = sorted([interval[0] for interval in intervals])
    end_intervals = sorted([interval[1] for interval in intervals])

    results = []

    for q in query_points:
        start_count = binary_search(start_intervals, q)
        end_count = binary_search(end_intervals, q)
        count = start_count - end_count
        results.append(count)

    return results

n = int(input())
intervals = [list(map(float, input().split())) for _ in range(n)]
query_points = [float(input()) for _ in range(n)]

counter = count_intervals(intervals, query_points)

for x in counter:
    print(x)