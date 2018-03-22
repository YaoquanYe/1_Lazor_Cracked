import itertools 
import copy
import sys

f = open('input.txt', 'r+')

data = f.read().split('\n')
# initialization of variables
# Now we specify that we have two lazers
#    x, y, v1x, v2y
# NOTE! because 0, 0 is the top left, our axis
# are as follows:
#
#      __________\ +x
#      |         /
#      |
#      |
#      |
#     \|/ +y
#      

# v1,v2: direction of start point x,y: coordinates of a point
v1 = 0 
v2 = 0
x = 0
y = 0
# Block_Type is the type of a block. 
Block_Type = 'o' 
Block_index = 0 
#destination_list contains all the destination points
destination_list = []
# start_list is a list of Point objects and contains all the information of the start points
start_list =[]
# the number of fixed block A, B, C and start points.
Num_fixedA = 0
Num_fixedB = 0
Num_fixedC = 0
Num_Start = 0
# the lists below are only used in read data.
Start= []
fixedblock_list = []
Startpointlist = []
Xlist = []
fixedAlist = []
fixedBlist = []
fixedClist = []
Despointlist = []
##############################################################################################################
class Block:
    
# (x,y) is the center of the block, and left, right... is the path coordinate of that block. Type shows the type of the block
  
  def __init__(self,x,y):
    self.x = x
    self.y = y
    self.Block_Type = Block_Type
    self.Block_index = ((x-1)+ (Num_Cols*(y-1)))/2
#############################################################################################################
class Point:
# Declare variable and initiazation via constructor    

  def __init__(self,x,y):
    self.x = x
    self.y = y
    # v1: direction of x, v2: direction of y
    self.v1 = v1
    self.v2 = v2
########################################################################################################## 

for s in data:
    # read data about the board dimensions
	if s.startswith('Num_Cols = '):
		Num_Cols = s.split()[-1]
		Num_Cols = int(Num_Cols)
	if s.startswith('Num_Rows = '):
		Num_Rows = s.split()[-1]
		Num_Rows = int(Num_Rows)
    # read data about removable blocks A,B,C
	if s.startswith('Num_A = '):
		Num_A = s.split()[-1]
		Num_A = int(Num_A)
		
	if s.startswith('Num_B = '):
		Num_B = s.split()[-1]
		Num_B = int(Num_B)

	if s.startswith('Num_C = '):
		Num_C = s.split()[-1]
		Num_C = int(Num_C)
    
    # read data about the points for which the user wants the laser light to intersect, and save them as an array in Despointlist
	if s.startswith('Num_Destination = '):
		Num_Destination = s.split()[-1]
		Num_Destination = int(Num_Destination)

	if s.startswith('Destination = '):
		Destination = s.split()[2:]
		Despointlist.append(Destination)

    # read data about the information of start point, and save them as an array in Startpointlist
	if s.startswith('Num_Start = '):
   		Num_Start = s.split()[-1]
   		Num_Start = int(Num_Start)
   		
	if  s.startswith('start = '):
		
   		Start = s.split()[2:]
   		Startpointlist.append(Start)

    # read data about the number of block X and its corresponding positions. Save them as an array in Xlist
   	if s.startswith('Num_X = '):
		Num_X = s.split()[-1]
		Num_X = int(Num_X)
   		
	if s.startswith('X = '):
		X = s.split()[2:]
		Xlist.append(X)

    # read data about the number of block FA (fixed block A) and its corresponding positions. Save them as an array in fixedAlist
	if s.startswith('Num_fixedA = '):
		Num_fixedA = s.split()[-1]
		Num_fixedA = int(Num_fixedA)
		
   		
	if s.startswith('FA = '):
		FA = s.split()[2:]
		fixedAlist.append(FA)

    # read data about the number of block FB (fixed block B) and its corresponding positions. Save them as an array in fixedBlist
	if s.startswith('Num_fixedB = '):
		Num_fixedB = s.split()[-1]
		Num_fixedB= int(Num_fixedB)
   		
	if s.startswith('FB = '):
		FB = s.split()[2:]
		fixedBlist.append(FB)
    
    # read data about the number of block FC (fixed block C) and its corresponding positions. Save them as an array in fixedClist

	if s.startswith('Num_fixedC = '):
		Num_fixedC = s.split()[-1]
		Num_fixedC= int(Num_fixedC)
   		
	if s.startswith('FC = '):
		FC = s.split()[2:]
		fixedClist.append(FC)

# convert Despointlist into an int list, destination_list. 
for ii in range(Num_Destination):
	a =[]
	x = Despointlist[ii][0]
  	x=int(x)
  	y = Despointlist[ii][1]
	y=int(y)
  	a.append(x)
  	a.append(y)
  	destination_list.append(a)
  	
    # Check the validity of Destination points
	if (x > 2*Num_Cols or y > 2*Num_Rows  or (x+y)%2 == 0):
		print ("Sorry, destination points are not valid please try again!")
   		break

# convert Startpointlist into an array of object Point--> start_list. 
for ii in range(Num_Start):
	q = Startpointlist[ii][0]
	q = int(q)
	m = Startpointlist[ii][1]
	m = int(m)
	a = Point(q,m)
	e = Startpointlist[ii][2]
	e = int(e)
	t = Startpointlist[ii][3]
	t = int(t)
	a.v1 = e
	a.v2 = t
	start_list.append(a)
    # Check the validity of start points
	if (q > 2*Num_Cols or m> 2*Num_Rows  or (q+m)%2 == 0):
		print ("Sorry, start points are not valid please try again!")
   		break

# fixedblock_list is a list of unremovable block with their block type
# append fixedblock_list with information in Xlist
for ii in range(Num_X):
	x= Xlist[ii][1]
	x=int(x)
	
	y = Xlist[ii][0]
	y =int(y)
    
     # Check the validity of user input 
	if ( x > Num_Cols or y > Num_Rows or x <= 0 or y <= 0):
		print ("Sorry, Block X is not valid please try again!")
   		break
   	x = 2*x-1
   	y = 2*y-1
	c = Block(x,y)
	pos_X = c.Block_index
  	fixedblock_list.append([pos_X,'X'])

# append fixedblock_list with information in fixedAlist
for ii in range(Num_fixedA):
	# x, y are column number and row number
	x= fixedAlist[ii][1]
	x=int(x)
	y = fixedAlist[ii][0]
	y =int(y)
     # Check the validity of user input 
	if ( x > Num_Cols or y > Num_Rows or x <= 0 or y <= 0):
		print ("Sorry, Block Fixed A is not valid please try again!")
   		break
   	# now x, y are center coordinates
   	x = 2*x-1
   	y = 2*y-1
	c = Block(x,y)
	pos_FA = c.Block_index
  	fixedblock_list.append([pos_FA,'FA'])

# append fixedblock_list with information in fixedBlist
for ii in range(Num_fixedB):
	# x, y are column number and row number
	x= fixedBlist[ii][1]
	x=int(x)
	y = fixedBlist[ii][0]
	y =int(y)
     # Check the validity of user input 
	if ( x > Num_Cols or y > Num_Rows or x <= 0 or y <= 0):
		print ("Sorry, Block Fixed B is not valid please restart it again!")
   		break
   	# now x, y are center coordinates
   	x = 2*x-1
   	y = 2*y-1
	c = Block(x,y)
	pos_FB = c.Block_index
  	fixedblock_list.append([pos_FB,'FB'])

# append fixedblock_list with information in fixedClist
for ii in range(Num_fixedC):
	# x, y are column number and row number
	x = fixedClist[ii][1]
	x = int(x)
	y = fixedClist[ii][0]
	y = int(y)
     # Check the validity of user input 
	if ( x > Num_Cols or y > Num_Rows or x <= 0 or y <= 0):
		print ("Sorry, Block Fixed C is not valid please restart it again!")
   		break
   	# now x, y are center coordinates
   	x = 2*x-1
   	y = 2*y-1
	c = Block(x,y)
	pos_FC = c.Block_index
  	fixedblock_list.append([pos_FC,'FC'])


# make a copy of start_list and record all the start points
start_test = copy.deepcopy(start_list) 	

# make a copy of destination_list and record all the destination points
des_test = copy.deepcopy(destination_list)

total_numblock = Num_A + Num_B + Num_C 

# Total number of fixed blocks
total_fixedblock = Num_X + Num_fixedA + Num_fixedB + Num_fixedC

# Sort the fixedblock_list by the index number in ascending order 
fixedblock_list = sorted(fixedblock_list, key = lambda x : x[0])

############################################################################################################################

# Start generating boards

# Generate a list containing all types of blocks (A,B,C)
sample_comblock = []
for i in range(Num_A):
    sample_comblock.append('A')
for j in range(Num_B):
    sample_comblock.append('B')
for k in range(Num_C):
    sample_comblock.append('C')

# all_comblock includes all combinations of blocks A, B, and C (redundancy may occur if has multiple blocks with same types)
all_comblock = []

# unique_comblock includes all unique combinations of blocks A, B, and C (no redundancy)
unique_comblock = []
for l in itertools.permutations(sample_comblock):
    all_comblock.append(l)

for i in all_comblock:
    if i not in unique_comblock:
        unique_comblock.append(i)


def partitions(n, k):
    for c in itertools.combinations(range(n+k-1), k-1):
        yield [b-a-1 for a, b in zip((-1,)+c, c+(n+k-1,))]

# all_posiboard includes partition function output (1 denotes either a A/B/C block is placed here, 0 denotes empty block, X dentoes no block allowed)
all_posiboard = []

# actual_board includes all unqiue boards with types A, B, C, fixed A, fixed B, fixed C and X 
actual_comboard = []
for p in partitions(total_numblock, Num_Cols*Num_Rows-total_fixedblock):
    if max(p) == 1:
        if len(fixedblock_list) != 0:
            for j in range(len(fixedblock_list)):
          # append fixed block to list p if its index exceeds the length of current list
                if (fixedblock_list[j][0]>len(p)-1):
                    p.append(fixedblock_list[j][1])
                else:
                    p.insert(fixedblock_list[j][0],fixedblock_list[j][1])
            all_posiboard.append(p)
        else:
          all_posiboard.append(p)
        
#for w in all_posiboard:
  #print w

               
for m in all_posiboard:
    for g in unique_comblock:
        k = 0
        # Make local copys of boards to replace "1" in all_posiboard with A/B/C from unique_comblock 
        copy_board = copy.deepcopy(m)
        for n in range(len(copy_board)):
            if copy_board[n] == 1 :
                copy_board[n] = g[k]
                k += 1
        actual_comboard.append(copy_board)

for i in actual_comboard:
    for q in range(len(i)):
        if i[q] == 0:
            i[q] = 'o'

#for i in actual_comboard:
   #print i

##########################################################################################################################

x_coord = []
y_coord = []
xycoord_comboard = copy.deepcopy(actual_comboard)

#print actual_comboard
for w in range(1,Num_Cols*2):
    if w % 2 == 1:
        x_coord.append(w)

for e in range(1,Num_Rows*2):
    if e % 2 == 1:
        y_coord.append(e)

for z in range(len(actual_comboard)):
  for x in x_coord:
    for y in y_coord:
            a = Block(x,y)
            # xycoord_comboard is an array containing the block objects(x,y coordinates of the center point, and block type).
            # it contains all combinations of the board
            a.Block_type = actual_comboard[z][((x-1)+(Num_Cols*(y-1)))/2]
            xycoord_comboard[z][((x-1)+(Num_Cols*(y-1)))/2] = a

#####################################################################################

# Start constructing path
limit = 4*(2*Num_Cols+1)*(2*Num_Rows+1)


def dfs (Board):
  destination_list = copy.deepcopy(des_test)
  start_list = copy.deepcopy(start_test)
  #print (Board[0].Block_type)
  #print (destination_list)
  #print (start_list[0])
  path_list = []
  while (len(start_list)!=0 and len(destination_list)!=0):
    
# pop up one element/ an Point object in start_list and store it in temp
    temp = start_list.pop()
    
# start_x,y,v1,v2 shows the attributes of temp and all the point that laser passed from the start point will be stored in the array path_list
    current_x = temp.x
    current_y = temp.y
    v1 = temp.v1
    v2 = temp.v2
    
    while True:

      a=[]
      a.append(str(current_x))
      a.append(str(current_y))
      
      # Break the loop if out of boundary
      if (current_x < 0 or current_x > 2*Num_Cols): 
        break
      if (current_y < 0 or current_y > 2*Num_Rows):
        break

      # Break the loop if encounters type C blocks
      if ( v1*v2 == 0):
        break

      # Break the loop if it is infinite loop 
      if ( len(path_list)>limit):  
        break
      else: path_list.append(a)
      

      # Check whether the current point is one element in destination list
      # If it is in the list, delete that element in the destination list.
      for i in range(len(destination_list)):
        
        if (current_x == destination_list[i-1][0]):
          if (current_y == destination_list[i-1][1]):
            destination_list.remove(destination_list[i-1])
            
      # If path pass all destination points, get out of loop
      if (len(destination_list)==0):
        break
      
     

 # predict the direction v1,v2 for the next step
      if (current_x % 2 == 0):
        B_index = ((current_x+v1-1) + (Num_Cols*(current_y-1)))/2
        if (B_index >= len(Board)):
          break
        target = Board[B_index]
        Block_type = target.Block_type
        
      
      if (current_y % 2 == 0):
        B_index = ((current_x-1)+ (Num_Cols*(current_y+v2-1)))/2
        if (B_index >= len(Board) or Block_index < 0):
          break
      
        target = Board[B_index]
        Block_type = target.Block_type
        
      # When it hits the boundary, the direction will not change
      if ((current_x == 0 and v1 < 0) or
          (current_x == 2 * Num_Cols and v1 > 0) or
          (current_y == 0 and v2 < 0) or
          (current_y == 2 * Num_Rows and v2 > 0)
          ):
        Block_type = 'o'    

      # when it encounters block A or fixed A
      if(Block_type =='A' or Block_type == 'FA'): # this is block A or fixed A: reflect
        if (current_x % 2 == 1):
          v1 = v1
          v2 = -v2
        else:
          v1 = -v1
          v2 = v2

      # when it encounters block B or fixed B
      if (Block_type == 'B' or Block_type == 'FB'): # this is block B or fixed B: absorb
        v1 = 0
        v2 = 0
    
      # when it encounters block C and fixed C
      if (Block_type == 'C' or Block_type == 'FC'): # this is block C or fixed C: reflect and pass
        
        m = v1
        n = v2
         # A new start point is created and added it into the start point
        
        if (current_x % 2 == 1):
          v1 = v1
          v2 = -v2
        else:
          v1 = -v1
          v2 = v2
        a = Point(current_x,current_y)
        a.v1 = v1
        a.v2 = v2
        start_list.append(a)
        v1 = m
        v2 = n

# Move to the next step and save the next step in the path_list
      current_x = current_x+v1
      current_y = current_y+v2
     
  return destination_list  


l = []


for i in range(len(xycoord_comboard)):
 
  l = dfs(xycoord_comboard[i])
 
  if (len(l) == 0):
    print "The Solution is:"
    for w in range(Num_Rows):
      printboard = []
      for r in range(Num_Cols):
        printboard.append(actual_comboard[i].pop(0))
      print printboard
    print "BRAVO"

    break

