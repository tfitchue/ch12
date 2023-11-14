# Taner Fitchue
# CH12
#11/10/23


class NumberSorter:
    def __init__(self):
        self.numbers = []

    def get_user_input(self):
        count = 0
        while count < 15:
            num = int(input(f"Enter a number (or -1 to stop, {15 - count} remaining): "))
            if num == -1:
                break
            self.numbers.append(num)
            count += 1

    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quicksort(left) + middle + self.quicksort(right)

    def bucket_sort(self, arr):
        if not arr:
            return arr

        max_num = max(arr)
        min_num = min(arr)
        bucket_range = max(1, (max_num - min_num) / 10)  # Ensure bucket_range is at least 1

        buckets = [[] for _ in range(11)]  # Increase the range by 1 to include the maximum value
        for num in arr:
            index = min(10, int((num - min_num) // bucket_range))  # Ensure the index is within bounds
            buckets[index].append(num)

        sorted_buckets = [sorted(bucket) for bucket in buckets]
        return [num for bucket in sorted_buckets for num in bucket]

    def print_results(self):
        print("Unsorted array:", self.numbers)

        # Quicksort
        sorted_quick = self.quicksort(self.numbers.copy())
        print("Quicksort:", sorted_quick)

        # Bucket Sort
        sorted_bucket = self.bucket_sort(self.numbers.copy())
        print("Bucket Sort:", sorted_bucket)

if __name__ == "__main__":
    sorter = NumberSorter()
    sorter.get_user_input()
    sorter.print_results()

