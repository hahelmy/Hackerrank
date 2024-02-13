def jumpingOnClouds(c):
    path1 =set()
    indx = 0
    
    while indx < len(c)-1:
        if c[indx] == 0:
            path1.add(indx)
            if (indx+2 <= len(c) -1 ) and (c[indx+2] == 0):
                path1.add(indx+2)
                indx += 2
            elif (indx+1 <= len(c) -1 ) and (c[indx+1] == 0):
                path1.add(indx+1) 
                indx += 1
                
    print (len(path1))
    
c=[0,0,0,1,0,0]  
jumpingOnClouds(c)