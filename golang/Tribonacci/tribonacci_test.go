package Tribonacci

import (
	"reflect"
	"testing"
)

func TestTribonacci(t *testing.T) {
	tables := []struct {
		seed     [3]int
		n        int
		expected []int
	}{
		{[3]int{1, 1, 1}, 5, []int{1, 1, 1, 3, 5}},
		{[3]int{1, 2, 3}, 5, []int{1, 2, 3, 6, 11}},
		{[3]int{1, 2, 3}, 3, []int{1, 2, 3}},
		{[3]int{1, 2, 3}, 2, []int{1, 2}},
		{[3]int{1, 2, 3}, 1, []int{1}},
		{[3]int{1, 2, 3}, 0, []int{}},
	}
	for _, table := range tables {
		sequence := Tribonacci(table.seed, table.n)
		if !reflect.DeepEqual(sequence, table.expected) {
			t.Errorf("Tribonacci sequence was incorrrect, got %d, wanted %d", sequence, table.expected)
		}
	}
}
