package Tribonacci

import "math"

func Tribonacci(signature [3]int, n int) []int {
	var res []int

	for i:=0; float64(i) < math.Min(float64(n), float64(3)); i++ {
		res = append(res, signature[i])
	}

	for i:=2; i<n-1; i++ {
		res = append(res, res[i]+res[i-1]+res[i-2])
	}
	return res
}
