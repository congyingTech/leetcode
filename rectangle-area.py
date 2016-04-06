#-*-coding:utf-8-*-
class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        #(A,B)第一个矩形的左下角，(C,D)第一个矩形的右上角
        #(E,F)第二个矩形的左下角，(G,H)第二个举行的右上角
        #查找两个直线矩形的二维平面覆盖的总面积。 如该图所示的每个矩形由其左下角和右上角限定。
        #覆盖面积=总面积 - 重叠面积
        #1）当两个矩形没有重叠的时候，覆盖面积就是两个矩形面积和
        #2）当有重叠的时候，要找到重叠部分的左下角和右上角，根据坐标计算出面积
        area = (D - B)*(C - A) + (H -F)*(G - E)
        #两个矩形不相交的情况
        if B >= H or E >= C or A >= G or F >= D:
            return area  
        #相交的情况下,求相交矩形的左下角和右上角
        leftbottomx = max(A, E)
        leftbottomy = max(B, F)
        righttopx = min(C, G)
        righttopy = min(D, H)
        
        return area - (righttopx - leftbottomx)*(righttopy - leftbottomy)
    
    
    
if __name__ =="__main__":
    print(Solution().computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
        
        
