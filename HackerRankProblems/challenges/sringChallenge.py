def StringChallenge(strParam):

  # code goes here
  a = ""
  for x in strParam:
    if x .isalnum():
      a += x
  return a

# keep this function call here 
print(StringChallenge(input()))