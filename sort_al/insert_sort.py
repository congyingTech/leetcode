#-*- coding:utf-8 -*-
def insert_sort(lists):
    n = len(lists)
    for i in range(1, n):
        #暂存要更改的数
        key = lists[i]
        j = i - 1
        while j >= 0:
            print(j)
            if lists[j] > key:
                lists[j+1] = lists[j]
                lists[j] = key
            #要看j之前的那些是否也是排好了序
            j -= 1
    return lists

if __name__ == "__main__":
    lists=[2,3,4,5,1]
    print(insert_sort(lists))
                
        
