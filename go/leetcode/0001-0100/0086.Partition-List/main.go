package main

import "github.com/NicolasLeigh/algorithms/structures"

type ListNode = structures.ListNode

func partition(head *ListNode, x int) *ListNode {
	beforeHead := &ListNode{Next: nil}
	before := beforeHead
	afterHead := &ListNode{Next: nil}
	after := afterHead

	for head != nil {
		if head.Val < x {
			before.Next = head
			before = before.Next
		} else {
			after.Next = head
			after = after.Next
		}
		head = head.Next
	}
	after.Next = nil
	before.Next = afterHead.Next
	return beforeHead.Next
}
