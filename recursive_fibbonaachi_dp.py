import time

start_time = time.time()
def cal_fibb(n, dp=None):
    if dp is None:
        dp = [-1] * (n + 1)

    if n <= 2:
        return 1

    if dp[n] != -1:
        return dp[n]

    dp[n] = cal_fibb(n - 1, dp) + cal_fibb(n - 2, dp)
    return dp[n]

print(f'Answer is {cal_fibb(35)}')


end_time = time.time()
run_time = end_time - start_time

print(f"Execution time for code block 1: {run_time} seconds")

#dp[n] is the nth fibbonachi number




