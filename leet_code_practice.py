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


