class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        ans = -1

        while low <= high:
            mid = (low + high) // 2

            current_load = 0
            required_days = 1

            for weight in weights:
                if current_load + weight <= mid:
                    current_load += weight
                else:
                    required_days += 1
                    current_load = weight
            if required_days <= days:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans


        