#TODO
'''

permutation:
  return all the num permutation of the number

ie:
111 -> 12

'''

import math

def remove_char_index(text, index):
  return "{}{}".format(text[:index], text[index+1:])


def permutation(word)-> []:
  if len(word) == 1:
    return [word]
  else:
    result = []
    for i in range(len(word)):
      s = word[i]
      new_word = remove_char_index(word, i)
      new_word_arr = permutation(new_word)

      for ss in new_word_arr:
        result.append(s+ss)

    return result


if __name__ == '__main__':
  testcases = [
    "ab",
    "abc",
    "abcd",
  ]


  for i in range(len(testcases)):
    tc = testcases[i]
    all_combination = permutation(tc)

    if len(all_combination) != math.factorial(len(tc)):
      print("testcase [{}] failed".format(i))
    else:
      for h in range(len(all_combination)):
        s1 = all_combination[h]
        # check duplicate
        for k in range(len(all_combination)):
          s2 = all_combination[k]
          if s1 == s2 and h != k: # duplicated
            print("testcase [{}] failed".format(i))
            continue
      print("testcase [{}] passed".format(i))


