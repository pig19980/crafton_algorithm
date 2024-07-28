def build_suffix_array(s):
    """Build suffix array for string s"""
    suffixes = [(s[i:], i) for i in range(len(s))]
    suffixes.sort()
    return [suffix[1] for suffix in suffixes]


def build_lcp_array(s, suffix_array):
    """Build LCP (Longest Common Prefix) array for string s and its suffix array"""
    n = len(s)
    rank = [0] * n
    lcp = [0] * n

    # Assign ranks based on suffix array
    for i, suffix in enumerate(suffix_array):
        rank[suffix] = i

    h = 0  # Initial depth for LCP calculation

    for i in range(n):
        if rank[i] > 0:
            j = suffix_array[rank[i] - 1]
            while i + h < n and j + h < n and s[i + h] == s[j + h]:
                h += 1
            lcp[rank[i]] = h
            if h > 0:
                h -= 1

    return lcp


def longest_common_substring(s1, s2):
    """Find longest common substring of s1 and s2"""
    combined_string = s1 + "#" + s2 + "$"
    suffix_array = build_suffix_array(combined_string)
    lcp_array = build_lcp_array(combined_string, suffix_array)

    max_length = 0
    starting_index = 0

    for i in range(1, len(combined_string)):
        if (suffix_array[i] < len(s1) and suffix_array[i - 1] > len(s1)) or (
            suffix_array[i] > len(s1) and suffix_array[i - 1] < len(s1)
        ):
            if lcp_array[i] > max_length:
                max_length = lcp_array[i]
                starting_index = suffix_array[i]

    return combined_string[starting_index : starting_index + max_length]


# Example usage:
s1 = "yeshowmuchiloveyoumydearmotherreallyicannotbelieveit"
s2 = "yeaphowmuchiloveyoumydearmother"
lcs = longest_common_substring(s1, s2)
print("Longest Common Substring:", lcs)
