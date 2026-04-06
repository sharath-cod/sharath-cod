capacity=(10,7,3)
x=capicity[0]
y=capacity[1]
z=capacity[2]

memory={}
ans=[]

def getallstate(state):
  a=state[0]
  b=state[1]
  c=state[2]

if(a==5 and b==5):
  ans.append(state)
  return True
if (a,b,c) in memory :
  rteurn False
memory[(a,b,c])=1
if a>0
