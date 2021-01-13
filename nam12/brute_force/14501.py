def dfs(cnt, p) :
    
    if cnt > n :
        print("탈출 : ", cnt,p)
        return 
    print("추가 : ",cnt, p)
    ans.append(p)
    for i in range(n) :
        
        if(check_list[i]) :
            continue
        
        check_list[i] = True
        p += pay[cnt]
        print("dfs 진입", cnt+time[cnt], cnt, time[cnt], p)
        dfs(cnt + time[cnt], p)
        p -= pay[cnt]
        for j in range(i+1, n):
            check_list[j] = False 

n = int(input())
time, pay = [0 for i in range (n+10)], [0 for i in range (n+10)]
check_list = [False for i in range(n)]
ans = []

for i in range(n) :
    time[i] , pay[i] = map(int, input().split())

dfs(0,0)