"""
https://www.codewars.com/kata/59cf0ba5d751dffef300001f/train/python

Task

You are given a string s. Your task is to count the number of each letter
(A-Z), and make a vertical histogram as result. Look at the following
examples to understand the rules.
Example

For s = "XXY YY ZZZ123ZZZ AAA BB C", the output should be:

          *
          *
          *
*       * *
* *   * * *
* * * * * *
A B C X Y Z

Rules

You just need to count the uppercase letters. Any other character will be
 ignored.
Using * to represent the number of characters.
The order of output is form A to Z. Characters that do not appear in the string
 are ignored.
To beautify the histogram, there is a space between every pair of columns.
There are no extra spaces at the end of each row. Also, use "\n" to separate
 rows.
Happy Coding ^_^

    ## Loop method instead of dict comprehension
    # store_loop = {}
    # for c in chars:
    #     if c in ascii_uppercase:
    #         store_loop[c] = s.count(c)

"""


def vertical_histogram_of_orig(s):
    chars = set(s)
    hist = {c: s.count(c) for c in chars if c.isupper()}

    # Default arg accounts for empty string input
    height = max(hist.values(), default=0)
    keys_ord = sorted(hist.keys())

    output = []
    for h in range(height, 0, -1):
        line = ""
        for k in keys_ord:
            if h <= hist[k]:
                line += "*"
            else:
                line += " "
        output.append(" ".join(line.rstrip()))
    output.append(" ".join(keys_ord))

    return "\n".join(output)


def vertical_histogram_of(s):
    def build_line(h):
        return " ".join(["*" if h <= hist[k] else " " for k in keys_ord])

    hist = {c: s.count(c) for c in set(s) if c.isupper()}

    height = max(hist.values(), default=0)
    keys_ord = sorted(hist.keys())

    lines = [build_line(h).rstrip() for h in range(height, 0, -1)]

    return "\n".join(lines + [" ".join(keys_ord)])


def vertical_histogram_of2(s):
    """
    Recursive version
    """

    def recline(h, k, st):
        if len(k) == 0:
            return ""
        if h > st[k[0]]:
            return recline(h, k[1:], st)
        return "*" + recline(h, k[1:], st)

    chars = set(s)
    hist = {c: s.count(c) for c in chars if c.isupper()}

    # Default accounts for empty string input
    height = max(hist.values(), default=0)
    keys_ord = sorted(hist.keys())

    output = []
    for h in range(height, 0, -1):
        line = recline(h, keys_ord, hist)
        output.append(" ".join(line))
    output.append(" ".join(keys_ord))

    return "\n".join(output)
    # return output


TEST = "XXY YY ZZZ123ZZZ AAA BB C"
if __name__ == "__main__":
    vertical_histogram_of(TEST)
vertical_histogram_of(TEST)
# vertical_histogram_of2("AAABBC")
# vertical_histogram_of("abc123")
print('hello world')
