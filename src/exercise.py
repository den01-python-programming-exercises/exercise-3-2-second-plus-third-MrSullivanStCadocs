def main():
    #write your code below this line
    myList = []
    while True:
      userNumber = int(input(" "))
      myList.append(userNumber)
      if(userNumber == 0):
        break
    
    sum = myList[1] + myList[2]
    print(str(myList[0]))
    print(str(sum))




if __name__ == '__main__':
    main()
