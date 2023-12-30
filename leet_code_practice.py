import re

word = "abbcc"
char_dict = {}
for char in word:
    if char not in char_dict:
        char_dict[char] = 1
    else:
        char_dict[char] += 1

result = False
for k in char_dict.keys():
    char_dict[k] -= 1
    char_set = set(char_dict.values())
    char_set.discard(0)
    print(char_set)
    if len(char_set) == 1:
        result = True
    print(result)
    char_dict[k] += 1
print(result)

import re

# Your input string
input_string = "Hello123 World456!"

# Replace all alphabets with spaces
result_string = re.sub(r'[a-zA-Z]', ' ', input_string)

print(f"Original string: {input_string}")
print(f"Result string:   {result_string}")

text = "  hello"
total_space_count = text.count(' ')
print(total_space_count)
all_words = [x for x in text.split(' ') if len(x) > 0]
print(all_words)
total_word_count = len(all_words)
print(total_word_count)
if total_space_count > 0 and total_word_count > 1:
    space_between_words = total_space_count // (total_word_count - 1)
    last_spaces = total_space_count % (total_word_count - 1)
    result = (' ' * space_between_words).join(all_words)
    if last_spaces > 0:
        result += ' ' * last_spaces
    print('r',result)
elif total_space_count == 0:
    print('t',text)
elif total_space_count > 0 and total_word_count == 1:
    print('e',''.join(all_words) + ' ' * total_space_count)

strs = ["flower","flower","flower"]
i = 0
result = ''
while True:
    try:
        chars = [x[i] for x in strs]
    except IndexError:
        break
    if len(set(chars)) == 1:
        result += ''.join(set(chars))
        print(result)
    else:
        break
    i += 1

print(result)

s = "Test1ng-Leet=code-Q!"
s_only_char_reverse = re.findall('[a-zA-Z]',s)
s_only_char_reverse.reverse()

for match in re.finditer('[^a-zA-Z]',s):
    s_only_char_reverse.insert(int(match.start()),match.group())

print(''.join(s_only_char_reverse))

licensePlate = "GrC8950"
words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]
import re
licensePlateChars = [s.lower() for s in re.findall(r'[a-z]',licensePlate,re.IGNORECASE)]
licensePlateCharsDict = {}
result = ''
for char in licensePlateChars:
    if char not in licensePlateCharsDict.keys():
        licensePlateCharsDict[char] = 1
    else:
        licensePlateCharsDict[char] += 1
print(licensePlateChars,licensePlateCharsDict)
for word in words:
    for key in licensePlateCharsDict.keys():
        if word.count(key) >= licensePlateCharsDict[key]:
            print('came here 1',key,word)
            continue
        else:
            print('came here 2',key,word)
            break
    else:
        print('came here 2')
        if len(word) < len(result) or result == '':
            result = word
print(result)

s = "aaabaaaa"
result = previous = s[0]
print(result)
char_count = 1
for char in s[1:]:
    if previous == char and char_count < 2:
        result += char
        char_count += 1
    elif previous != char:
        result += char
        char_count = 1
        previous = char
        print(result,char_count,'2')
print(result)

s = "code"
i, j = 0, 1
result = 0
while j <= len(s):
    while i < len(s):
        sub_str = s[i:i + j:1]
        if len(sub_str) == j:
            result += len(set(sub_str))
        i += 1
    j += 1
    i = 0
print(result)

mat = [[0,0],[1,1],[0,0]]
for index,elem in enumerate(mat):
    one_count = elem.count(1)
    print(one_count)
    print(index,elem)

nums = [0,1,0,3,12]
for i in range(len(nums)):
    if nums[i] == 0:
        nums.remove(0)
        nums.append(0)
print(nums)








