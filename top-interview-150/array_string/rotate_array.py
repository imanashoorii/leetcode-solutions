class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # Reversal Algorithm

        n = len(nums)

        if n == 0:
            return None

        k %= n

        self._reverse_right(nums, n, k)

    def __reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def _reverse_right(self, arr, n, k):
        self.__reverse(arr, 0, n - k - 1)
        self.__reverse(arr, n - k, n - 1)
        self.__reverse(arr, 0, n - 1)

    def _reverse_left(self, arr, n, k):
        self.__reverse(arr, 0, k - 1)
        self.__reverse(arr, k, n - 1)
        self.__reverse(arr, 0, n - 1)
