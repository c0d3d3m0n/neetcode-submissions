class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # frequency map
        left = 0
        max_freq = 0
        max_length = 0

        for right in range(len(s)):
            # Add current character
            count[s[right]] = count.get(s[right], 0) + 1

            # Update max frequency
            max_freq = max(max_freq, count[s[right]])

            # Check if window is invalid
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1

            # Update answer
            max_length = max(max_length, right - left + 1)

        return max_length