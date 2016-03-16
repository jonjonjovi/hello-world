import math


def main():
    sum=0

    for x in range(1,1000):
        if(x%3==0):
            sum=sum+x
            print(x)

        elif(x%5==0):
             sum=sum+x
             print(x)

    print("Final answer =",sum)
if __name__ == "__main__":
  main()