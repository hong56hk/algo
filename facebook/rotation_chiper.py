import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(input, rotation_factor):
  output = ""
  for c in input:
    asii = ord(c)
    if ord("0") <= asii <= ord("9"):
      output += chr((asii - ord("0") + rotation_factor)%10 + ord("0"))
    elif ord("A") <= asii <= ord("Z"):
      output += chr((asii - ord("A") + rotation_factor)%26 + ord("A"))
    elif ord("a") <= asii <= ord("z"):
      output += chr((asii - ord("a") + rotation_factor)%26 + ord("a"))

    else:
      output += c
    
  
  return output



if __name__ == "__main__":
  testcases = [
    [("This is a world full of happiness.", 3), ("Wklv lv d zruog ixoo ri kdsslqhvv.")],
    [("You can do it!", 3), ("Brx fdq gr lw!")],
    [("You can do it!", 26), ("You can do it!")],
    [("One goes up, must comes down.", 6), ("Utk muky av, sayz iusky juct.")],
    [("Adsinv3gAh_+=357FH:;fha#tyaEFGa6AG", 13), ("Nqfvai6tNu_+=680SU:;sun#glnRSTn9NT")],
  ]
  count = 1
  for testcase in testcases:
    input = testcase[0]
    expected = testcase[1]
    result = rotationalCipher(input[0], input[1])
    

    if result == expected:
      print("Test #{} passed".format(count))
    else:
      print("Test #{} failed.".format(count))
      print(" input   : {}".format(input[0]))
      print(" expected: {}".format(expected))
      print(" returned: {}".format(result))
    
    count += 1
  