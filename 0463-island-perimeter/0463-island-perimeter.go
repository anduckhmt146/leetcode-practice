func islandPerimeter(grid [][]int) int {
    var visit = make(map[string]bool)

    var dfs func(i, j int) int
    dfs = func(i, j int) int {
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