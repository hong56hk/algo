import sys

def compare_files(file1, file2):
  with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
    pos = 0
    while True:
      b1 = f1.read(1)
      b2 = f2.read(1)

      if not b1 and not b2:
        break  # Both files reached EOF

      if b1 != b2:
        print(f"Difference at byte {pos:#x}: {b1.hex() if b1 else 'EOF'} != {b2.hex() if b2 else 'EOF'}")

      pos += 1

if __name__ == "__main__":
  file1 = "C:/Users/Hong/Downloads/Archive/brush-scatter-43.abr" #sys.argv[1]
  file2 = "C:/Users/Hong/Downloads/Archive/brush-scatter-47.abr" #sys.argv[1]

  compare_files(file1, file2)


43 47
2B 2F

33=51
37=55

45=69
47=71