#Write a Python program to print the first 6 terms of a geometric sequence starting with 2
#and having a common ratio of 3.
def geometric_sequence(start, ratio, terms):
    sequence = []
    for i in range(terms):
        sequence.append(start * (ratio ** i))
    return sequence
start = 2
ratio = 3
terms = 6
sequence = geometric_sequence(start, ratio, terms)
print("The first 6 terms of the geometric sequence are:", sequence)
