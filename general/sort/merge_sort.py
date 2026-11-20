class MergeSort:
    def merge(self, arr1, arr2):
        combined = []

        i = 0
        j = 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                combined.append(arr1[i])
                i += 1
            else:
                combined.append(arr2[j])
                j += 1

        while i < len(arr1):
            combined.append(arr1[i])
            i += 1

        while j < len(arr2):
            combined.append(arr2[j])
            j += 1

        return combined

    def merge_sort(self, arr):
        if len(arr) == 1:
            return arr
        mid_index = int(len(arr) / 2)
        left = self.merge_sort(arr[:mid_index])
        right = self.merge_sort(arr[mid_index:])
        return self.merge(left, right)


m = MergeSort()
res = m.merge_sort([1, 3, 5, 4, 2, 6, 9, 8])
print(res)
