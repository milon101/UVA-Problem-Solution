
def area(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1-y1*x2-y2*x3-y3*x1



def intersection(x1, y1, x2, y2, x3, y3, x4, y4):

    a1=area(x1,y1,x3,y3,x2,y2);
    a2=area(x1,y1,x4,y4,x2,y2);
    a3=area(x3,y3,x1,y1,x4,y4);
    a4=area(x3,y3,x2,y2,x4,y4);
    
    if(a1*a2<0 & a3*a4<0):
        return True
    if(a1==0 & (x3-x1)*(x3-x2)<=0 & (y3-y1)*(y3-y2)<=0):
        return True;
    if(a2==0 & (x4-x1)*(x4-x2)<=0 & (y4-y1)*(y4-y2)<=0):
        return True;
    if(a3==0 & (x1-x3)*(x1-x4)<=0 & (y1-y3)*(y1-y4)<=0):
        return True;
    if(a4==0 & (x2-x3)*(x2-x4)<=0 & (y2-y3)*(y2-y4)<=0):
        return True;
    
    return False;

def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b


n = input()


for i in range(int(n)):
    
    points = [int(x) for x in input().split()]
    intersect=False

    xstart = points[0]
    ystart = points[1]
    xend = points[2]
    yend = points[3]
    xleft = points[4]
    ytop = points[5]
    xright = points[6]
    ybottom = points[7]
            
    if(xleft>xright):
        swap(xleft,xright);
    if(ybottom>ytop):
        swap(ybottom,ytop);
            
    if(intersection(xstart,ystart,xend,yend,xleft,ytop,xright,ytop)):
        intersect=True
    elif(intersection(xstart,ystart,xend,yend,xleft,ybottom,xright,ybottom)):
        intersect=True
    elif(intersection(xstart,ystart,xend,yend,xleft,ytop,xleft,ybottom)):
        intersect=True
    elif(intersection(xstart,ystart,xend,yend,xright,ytop,xleft,ybottom)):
        intersect=True
    elif(xstart>=xleft & xstart<=xright & xend>=xleft & xend<=xright & ystart>=ybottom & ystart<=ytop & yend>=ybottom & yend<=ytop):
        intersect =True
            
    if(intersect==True):
        print("T");
    else:
        print("F");
