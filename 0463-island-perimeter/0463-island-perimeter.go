func islandPerimeter(grid [][]int) int {
    var visit = make(map[string]bool)

    var dfs func(i, j int) int
    dfs = func(i, j int) int {
        // [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
        // (0,1)(0,2)(1,1)(1,2)(1,3)(2,2)(1,1)(0,2)(2,1)(2,2)(3,1)(3,2)(4,1)(3,0)(3,1)(4,0)(3,-1)(2,0)(2,1)(2,0)(1,1)(1,0)(1,1)(2,0)(1,-1)(0,0)(0,1)(0,0)(-1,1)  
        fmt.Printf("(%d,%d)", i,j);
        if i >= len(grid) || j >= len(grid[0]) || i < 0 || j < 0 || grid[i][j] == 0 {
            return 1
        }
        key := fmt.Sprintf("%d,%d", i, j)
        if visit[key] {
            return 0
        }

        visit[key] = true
        perim := dfs(i, j+1)
        perim += dfs(i+1, j)
        perim += dfs(i, j-1)
        perim += dfs(i-1, j)
        return perim
    }

    for i := range grid {
        for j := range grid[0] {
            if grid[i][j] == 1 {
                return dfs(i, j)
            }
        }
    }

    return 0
}