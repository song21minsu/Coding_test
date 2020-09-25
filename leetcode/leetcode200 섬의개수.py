def numIslands(matrix):

    def dfs(i,j):
        # 육지가 아니면 종료
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] != "1":
            return

        matrix[i][j]=0
        dfs(i+1,j)
        dfs(i-1,j)
        dfs(i,j+1)
        dfs(i,j-1)

    cnt=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]=="1":
                dfs(i,j)
                # 모든 육지를 탐색 후 카운트1증가
                cnt+=1
    return cnt

matrix = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],

  ["0","0","0","0","0"]
]

print(numIslands(matrix))