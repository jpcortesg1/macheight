# Required libraries
import json
from urllib.request import urlopen

# Search all cocoincidences
def searchCoincidences(data, sum):
    start = 0
    end = len(data) - 1
    into = False

    while start < end:
        if (int(data[start]["h_in"]) + int(data[end]["h_in"]) == sum):
            into = True
            print(data[start]["first_name"], data[start]["last_name"],  data[end]["first_name"], data[end]["last_name"])

        if (int(data[start]["h_in"]) + int(data[end]["h_in"]) < sum):
            start += 1
        else:
            end -= 1
    if(into == False):
      print("No matches found")

    print()

# Read the info of the la url
def readInfo():
    url = "https://mach-eight.uc.r.appspot.com"
    response = urlopen(url)

    dataJson = json.loads(response.read())
    return dataJson["values"]

# Run Program
def run(data):
  print("Insert any number for search the pair of players that when adding their height is equal to the number, or write 'exit' to stop the program: ")
  number = input()
  if(number == "exit"): 
    return

  isDigit = number.isnumeric()
  if(isDigit):
    number = int(number)
    searchCoincidences(data, number)
  else:
    print("Value must be numeric")
  
  run(data)


# Run file
def main():
  arrayData = readInfo()
  sortData = sorted(arrayData, key=lambda k: int(k['h_in']))
  run(sortData)


# Run main function
if __name__ == "__main__":
    main()