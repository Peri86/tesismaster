#!/usr/bin/env python
import igraph

def generate_mcl_matrix(G):
    mcifile = ""
    mclheader = (
        ("\n(mclheader\n"),
        ("mcltype matrix\n"),
        ( "dimensions %sx%s\n)\n" % (G.vcount(), G.vcount()) ),
        ("(mclmatrix\n"),
        ("begin\n")
    )
    for mhline in mclheader:
        mcifile += mhline
    for v in G.vs:
        mcifile += str(v.index) + " "
        for n in G.neighbors(v.index):
            mcifile += str(n) + " "
        mcifile += " $\n"
    mcifile += ")\n"
    return mcifile
 
def create_graph_image(mcl_line, base_name, G):
    from subprocess import Popen
    nodes = mcl_line.split()
    nodes = nodes[1:-1]     
    subG = G.subgraph([int(node) for node in nodes])
    subG.write_dot(base_name+".dot")
    cmd = "dot -T png -o " + base_name + ".png " + base_name + ".dot"
    Popen(cmd, shell=True)
 
def run_mcl_cluster(G):
    from subprocess import Popen, PIPE
    mcistr = generate_mcl_matrix(G)
    print mcistr + "\n"
    cmd = "mcl - -scheme 6 -I 1.6 -o -"
    p = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE, shell=True)
    sout,serr = p.communicate(mcistr)
    p.wait()
    lll = int()
    print "return code: %i\n" % p.returncode
    llistaa = [] # 
    if p.returncode==0 and len(sout)>0:
        lines = sout.splitlines()
        idx_begin = lines.index("begin")+1
        idx_end = lines[idx_begin:].index(")")+idx_begin
        num = 0
        cont = 0
        #llistaa = []
        for line in lines[idx_begin:idx_end]:
            lnou = line.split(' ')
            #print lnou #######
            for l in lnou:
                #print cont #######
                if cont>0:
                    if cmp(l,"$")!=0:
                        if cmp(l,"")!=0:
                            lll = int(l)
                            llistaa.insert(lll,num)
                cont+=1
            cont=0
        #create_graph_image(line, "mcl-ex-"+str(num), G)
            num+=1

    #print llistaa #######
    return llistaa