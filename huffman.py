

		
class Leaf:
    def __init__(self, chars, weight):
        self.left = None
        self.right = None
        self.chars = chars
        self.weight = weight

        
class Fork:
    def __init__(self,chars, weight,left=None, right=None,):
        self.left = left
        self.right = right
        self.chars = chars
        self.weight = weight
    	self.right=right

def frequency(s):
	weight={}
	for char in s :
        	weight[char] = weight.get(char,0) + 1
	return weight
	
def sort_frq (weight) :
    symbols = weight.keys()
    tuples = []
    for e in symbols :
        tuples.append((weight[e],e))
    tuples.sort()
    return tuples

def createCodeTree(sample):
	nodes=sorted([Fork(k,v) for (k,v) in frequency(sample).items()],key=lambda x:x.weight)
	while len(nodes) > 1:
		nodes=sorted(([Fork(nodes[0].chars+nodes[1].chars,nodes[0].weight+nodes[1].weight,nodes[0],nodes[1])]+nodes[2:]),key=lambda x:x.weight)
	return(nodes[0])
		
def make_code_table(codeTree):	
	codList=basecodetable(codeTree)
	codList0={}
	for (k,v) in codList:
		codList0[k]=v
	return(codList0)
	
				
def encode(string,tree):
	return baseencode(string,tree,tree,"")
	
def baseencode(s,node,tree,rslt):
	if s=='':
		return rslt
	elif node.left==None:
		return baseencode(s[1:],tree,tree,rslt)
	elif s[0] in node.left.chars:
		return baseencode(s,node.left,tree,rslt+'0')
	else:
		return baseencode(s,node.right,tree,rslt+'1')

	
			
def decode(string,tree):
	return(basedecode(string,tree,tree,""))

def basedecode(s,node,tree,rslt):
	if s=="":
		return(rslt+node.chars)
	elif node.left==None:
		return(basedecode(s,tree,tree,rslt+node.chars))
	elif s[0]=='0':
		return(basedecode(s[1:],node.left,tree,rslt))
	else:	
		return(basedecode(s[1:],node.right,tree,rslt))

def basecodetable(tree):
	if tree.left == None :
		return [(tree.chars,'')]
	x=basecodetable(tree.right)
	y=basecodetable(tree.left)
	return [(i,'0'+j) for (i,j) in y]+[(i,'1'+j) for (i,j) in x]		
	
def quickEncode(string,codList):
	rslt=""
	for i in string:
		rslt=rslt+codList[i]
	return rslt
		
def test():
	tree=createCodeTree("qwertyuirsltasdfghjklzxcvbnm")
	table=make_code_table(tree)
	print "code table:" ,table
	print 'string: "hinithin"'
	print 'code: '
	print encode("hinithin",tree)
	print 'code: "111001" '
	print 'string: ', 
	print decode("111001",tree)
test()
	
