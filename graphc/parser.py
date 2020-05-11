from graphc import parserErrors
from colors import *
def isint(value):
  try:
    int(value)
    return True
  except ValueError:
    return False

def displayColor(inp,num):
  from termcolor import colored
  string = ""
  inp = inp.replace("c:","")
  inp = inp.lower()    
  if inp != "orange":
    for _ in range(num):
      string = string + colored(" ","white","on_"+inp)
  elif inp == "orange":
    for _ in range(num):
      string = string + color(" ",bg="orange")
  string = string + "\n"    
  return string   


def displayShape(shape,length):
  if length == 0:
    length = 5

  if shape == "tri":
    return "*\n* *\n*  *\n*   *\n******"

  elif shape == "hline":
    e = ""
    for _ in range(length):
      e = e + "*"
    return e

  elif shape == "vline":
    e = ""
    for _ in range(length):
      e = e + "*\n"
    return e

  elif shape == "square":
    return "**\n**"

  elif shape == "ctri":
    return "*\n***\n*****\n*******"    

def parse(graphcFile):
  from termcolor import colored
  commands = ["display"]
  colors = ["c:Red","c:Blue","c:Yellow","c:Green","c:Cyan","c:Magenta","c:Grey","c:Orange"]
  shapes = ["tri","hline","square","ctri","vline"]
  overString = ""
  code = open(graphcFile,"r").read()
  code = code.split("\n")

  if graphcFile.split(".")[1]!="graphc": 
    e = graphcFile.split(".")[1]
    #raises error if file ex. not .graphc
    raise parserErrors.IncorrectFile("file type not graphc(file type .{})".format(e))

  for x in code: #gets content of code
    line = x.split(" ")
    command = ""
    inp = ""
    num = 0
    for piece in line:
      if piece in commands:
        command = piece
      elif piece in colors or piece in shapes:  
        inp = piece
      if isint(piece):
        num = int(piece)
      else:
        continue
    if inp in colors:      
      overString = overString + displayColor(inp,num)
    elif inp in shapes:  
      overString = overString + displayShape(inp,num)
  return overString      
    