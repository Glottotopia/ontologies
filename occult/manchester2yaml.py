import sys
import pprint

manchesterfile = sys.argv[1]
d = {}
vs = []
k = None
for l in open(manchesterfile).readlines():
    if l.startswith("Class"):
	for v in vs:
	    try:
		d[v].append(k.strip())
	    except KeyError:
		d[v] = [k.strip()]
	k = l[7:]
	vs = []
    if l.startswith("        "):
	vs.append(l.strip())
	
	 

def printclass(k,level,numberstring):
    print level*' ', '%s_0'%numberstring, k, ':'
    for i, kk in enumerate(d[k]):
	try:
	    if numberstring == '':
		printclass(kk,level+1,'%s'%(i+1))
		
	    else:
		printclass(kk,level+1,'%s_%s'%(numberstring,i+1))
	except KeyError:
	    pass
	
print "%YAML 1.2"
print "---"
printclass('owl:Thing',0,'')
