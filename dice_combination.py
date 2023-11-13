def check_combo():
    MOD = 1000000007
    n = int(input())
    dp = [0 for i in range(n+1)]
    dp[0] = 1
    for i in range(1,n+1):
        for j in range(1, 7):
            if j<=i:
                dp[i] = (dp[i] + dp[i-j]) % MOD
    return dp[n]
print(check_combo())            
