func canPlaceFlowers(flowerbed []int, n int) bool {
    // Add padding (0 at the beginning and end)
	f := append([]int{0}, flowerbed...)
	f = append(f, 0)

	// Iterate through the flowerbed, skipping first and last index
	for i := 1; i < len(f)-1; i++ {
		// Check if the current position is empty and both neighbors are empty
		if f[i-1] == 0 && f[i] == 0 && f[i+1] == 0 {
			f[i] = 1  // Plant a flower
			n--        // Decrease the count of flowers to plant
		}
	}

	// If there are no flowers left to plant, return true
	return n <= 0
}