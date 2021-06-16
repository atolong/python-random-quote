def main():
   #print("Keep it logically awesome.")
   
  #f = open("quotes.txt")
  #quotes = f.readlines()
  #f.close()
  
  f = open("quotes.txt")
quotes = f.readlines()

import random
last=13
rnd=random.randint(o,last)
last=len(quotes)-1

print(quotes[rnd])
f.close()
  print(quotes)

if __name__== "__main__":
  main()
