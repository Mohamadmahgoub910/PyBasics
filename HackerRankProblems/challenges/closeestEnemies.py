def ArrayChallenge(strArr):
  e = []
  for i , r in enumerate(strArr):
    for j,c in enumerate(list(r)):
      if c == '1' :
        px, py= (i,j)
      if c == '2':
        e.append((i,j))
  m = []
  for a,b in e :
    nw = abs(px-a) + abs(py-b)
    cw, rw = abs(px-a) + abs(py- (b-len(strArr))), abs(px- (a-len(strArr))) + abs(py-b)
    m.append(min(nw,cw,rw))
  return min(m) if m else 0

# keep this function call here 
print(ArrayChallenge(input()))