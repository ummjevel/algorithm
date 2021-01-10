def password(cnt):
    
    print("chekcing : ", ans)
    # if cnt > N : # 조건에 안 맞을 때
    #     return
    
    if cnt == N : # 길이는 맞는데 모음 1개이상, 자음 2개 이상일 때,
        print(*ans)
        return
        # check_str = [0, 0]
        # for char in ans :
        #     if (check_str[0] > 1 and check_str[1] >= 2) : break 
        #     if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        #         check_str[0] += 1
        #     else : check_str[1] += 1
        
        # if(check_str[0]):
        #     if(check_str[1] >= 2):
        #         print(*ans)
        #         return

    for i in range(0, C) : 
        if (check[i]) : 
            continue

        check[i] = True
        ans.append(arr[i])
        password(cnt+1)
        ans.pop()
        for j in range(i+1, N):
            check[j] = False    
        
N, C = map(int, input().split())
arr = list(input().split())
arr.sort()
print(arr)
check = [False for i in range(C)]
ans = []

password(0)
