import sys
fout = open("sample.out", "w") 
def solve(a, b):
  
  m = (a + b) / 2
  fout.write(str(m) + "\n")
  print m
  sys.stdout.flush()
  s = raw_input()
  if s == "CORRECT":
    return
  elif s == "TOO_SMALL":
    a = m + 1
  else:
    b = m - 1
  solve(a, b)

T = input()
for _ in xrange(T):
  a, b = map(int, raw_input().split())
  _ = input()
  solve(a + 1, b)

fout.close()