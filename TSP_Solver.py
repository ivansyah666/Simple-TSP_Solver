#!/usr/bin/env python
# coding: utf-8

# In[4]:


from itertools import permutations
def Total_dist(x,loc):
    dist=[]
    for i in range(len(loc)-1):
        dist.append(x[loc[i]][loc[i+1]])
    return sum(dist)
def Greed_Algorithm(x,start=0):
    loc=[start]
    dist=[]
    for i in range(len(x)):
        if len(loc)==len(x):
            loc.append(start)
        else:
            loc1=[h for h in range(len(x)) if h not in loc]
            y=[x[loc[i]][k] for k in loc1]
            for j in loc1:
                if x[loc[i]][j]==min(y):
                    loc.append(j)
                    break
            del(loc1)
            del(y)
    return loc,Total_dist(x,loc)
def Brute_Algorithm(x):
    loc=list(permutations([y for y in range(len(x))]))
    dist=[]
    res=[]
    for i in range(len(loc)):
        q=list(loc[i])
        q.append(q[0])
        dist.append(Total_dist(x,q))
        del q
    for i in range(len(loc)):
        if dist[i]==min(dist):
            q=list(loc[i])
            q.append(q[0])
            res.append(q)
    return res[0],min(dist)

