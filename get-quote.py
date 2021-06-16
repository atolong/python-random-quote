#第一次任务，输出字符
def main():
   print("Keep it logically awesome.")
   
   f = open("quotes.txt")#在第一次任务里没意义的三行代码
   quotes = f.readlines()
   f.close()

if __name__== "__main__":
  main()

#第二次任务，输出该文件某行句子
def main():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  print(quotes)
  print(quotes[0])
if __name__== "__main__":
  main()

#第三次任务，输出该文件随机行的句子
import random
last=13
rnd=random.randint(0,last)
def main():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last=len(quotes)-1
  print(quotes[rnd])
  
if __name__== "__main__":
  main()
