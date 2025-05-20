infile = open("C:\\Users\\Hong\\Desktop\\Hong\\git\\algo\\inprogress\\input.txt", "r")

def getfunc(s):
  i = s.find('(')
  return s[:i]

try:
  for line in infile:
      line = line.strip()
      if len(line) > 0:
        if line.startswith("async"):
          word_arr = line.split(" ")
          func = getfunc(word_arr[2])
          print(f"{func}: {func},")
        elif line.startswith("function"):
          word_arr = line.split(" ")
          func = getfunc(word_arr[1])
          print(f"{func}: {func},")
except Exception as e:
  print(e)
  
infile.close()