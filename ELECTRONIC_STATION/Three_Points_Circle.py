'''
//定义两个点，分别表示两个中点  
    Point2f midpt1, midpt2;  
    //求出点1和点2的中点  
    midpt1.x = (pt2.x + pt1.x) / 2;  
    midpt1.y = (pt2.y + pt1.y) / 2;  
    //求出点3和点1的中点  
    midpt2.x = (pt3.x + pt1.x) / 2;  
    midpt2.y = (pt3.y + pt1.y) / 2;  
    //求出分别与直线pt1pt2，pt1pt3垂直的直线的斜率  
    float k1 = -(pt2.x - pt1.x) / (pt2.y - pt1.y);  
    float k2 = -(pt3.x - pt1.x) / (pt3.y - pt1.y);  
    //然后求出过中点midpt1，斜率为k1的直线方程（既pt1pt2的中垂线）：y - midPt1.y = k1( x - midPt1.x)  
    //以及过中点midpt2，斜率为k2的直线方程（既pt1pt3的中垂线）：y - midPt2.y = k2( x - midPt2.x)  
    //定义一个圆的数据的结构体对象CD  
    CircleData CD;  
    //连立两条中垂线方程求解交点得到：  
    CD.center.x = (midpt2.y - midpt1.y - k2* midpt2.x + k1*midpt1.x) / (k1 - k2);  
    CD.center.y = midpt1.y + k1*(midpt2.y - midpt1.y - k2*midpt2.x + k2*midpt1.x) / (k1 - k2);  
    //用圆心和其中一个点求距离得到半径：  
    CD.radius = sqrtf((CD.center.x - pt1.x)*(CD.center.x - pt1.x) + (CD.center.y - pt1.y)*(CD.center.y - pt1.y));  
    return CD;  
'''

def checkIO(data):
    point1 = {'x':0,'y':0}
    point2 = {'x':0,'y':0}
    point3 = {'x':0,'y':0}
    points = data.replace('(','').replace(')','').split(',')
    point1['x'] = points[0]
    point1['y'] = points[1]
    point2['x'] = points[2]
    point2['y'] = points[3]
    point3['x'] = points[4]
    point3['y'] = points[5]
    print(point1['x'])

if __name__ == '__main__':
    checkIO("(2,2),(6,2),(2,6)")
    
