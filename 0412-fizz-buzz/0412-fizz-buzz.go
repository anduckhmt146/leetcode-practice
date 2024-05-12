func fizzBuzz(n int) []string {
	var numbers []string

	for index := 1; index <= n; index++ {
		if index%15 == 0 {
			numbers = append(numbers, "FizzBuzz")
		} else if index%3 == 0 {
			numbers = append(numbers, "Fizz")
		} else if index%5 == 0 {
			numbers = append(numbers, "Buzz")
		} else {
			numbers = append(numbers, strconv.Itoa(index))
		}
	}
	return numbers
}