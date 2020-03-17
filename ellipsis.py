class EllipsisFormatter:

    ELLIPSIS = "[...]"

    def __init__(self, max_len=32, min_len=1):
        self.max_len = max_len
        self.min_len = min_len

    def format(self, string):
        # If string is already sorter than maximum, do nothing.
        if len(string) <= self.max_len:
            return string

        # Split into words and cut on the maximum possible number of words.
        words = string.split(" ")
        accumulated_length = 0
        max_possible_idx = 0
        for word in words:
            accumulated_length += len(word)  # Sum word length.
            # If total length (taking elipsis space into account)
            # is greater than maximum, stop.
            if accumulated_length + len(self.ELLIPSIS) >= self.max_len:
                break
            max_possible_idx += 1  # Update index.
            accumulated_length += 1  # Sum <SPACE> length.
            
        result = " ".join(words[:max_possible_idx])

        # In case result is very short.
        if len(result) < self.min_len:
            if len(result) > 0:
                result += " " + words[max_possible_idx][:self.max_len - len(self.ELLIPSIS) - len(result) - 1]
            else:
                result = words[max_possible_idx][:self.max_len - len(self.ELLIPSIS)]
            return result + self.ELLIPSIS  # No space between word and ellipsis.

        # Add space between word and ellipsis.
        return result + " " + self.ELLIPSIS

