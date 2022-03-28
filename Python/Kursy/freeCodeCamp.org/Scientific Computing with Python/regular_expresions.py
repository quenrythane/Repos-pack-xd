import re

expression = "[a-z]"
input = "abc"
# [] mean 1 character, but this character could be anything from a to z
print(re.findall(expression, input))  # ['a', 'b', 'c']
print(re.findall("[0-9]]", input))  # [] <- there is no digits so empty list
print()

# RE: find all letter that are beetwen a-b
print(re.findall("[ab]", input))  # ['a', 'b']
# RE: find all combine letters ab
print(re.findall("[ab]+", input))  # ['ab']
print()


# RE: find all numbers
print(re.findall("[0-9]+", "I am 10 yo, and my brother is 6"))  # ['10', '6']
print()

# RE: start with a, than any array of lower letters but without spaces
print(re.findall("a[a-z]+", "I am 10 yo, and my brother is 6"))  # ['am', 'and']
print()

# RE: sentence star with I than contains small letter (a-z) nad whitespaces allow
print(re.findall("^I[a-z\s]+", "I am 10 yo, and my brother is 6"))  # ['I am ']
# it stops at 10 because i was searching small letters and whitespaces and 10 is number, so cut here
print(re.findall("[a-z\s]+", "I am 10 yo, and my brother is 6"))  # ['I am ']
print()
