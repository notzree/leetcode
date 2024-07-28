type Node struct {
    Val int
    Next *Node
}

type MyLinkedList struct {
    Head *Node
    Tail *Node
}


func Constructor() MyLinkedList {
    return MyLinkedList{}
}


func (this *MyLinkedList) Get(index int) int {
    node := this.Head
    for i:=0; i< index; i++ {
        if node == nil {
            return -1
        }
        node = node.Next
    }
    if node == nil {
        return -1
    }

    return node.Val
}


func (this *MyLinkedList) AddAtHead(val int)  {
    newNode := &Node{
        Val: val,
        Next: this.Head,
    }
    this.Head = newNode
    if this.Tail == nil {
        this.Tail = newNode
    }
}


func (this *MyLinkedList) AddAtTail(val int)  {
    newNode := &Node{
            Val: val,
            Next: nil,
        }
    //if tail is non-empty, add it to the end of the list
    if this.Tail != nil {
        this.Tail.Next = newNode
    }
    // if tail is empty, assign tail to the newNode
    this.Tail = newNode
    //if the head is empty, assign the head to the newNode
    if this.Head == nil {
        this.Head = newNode
    }
}


func (this *MyLinkedList) AddAtIndex(index int, val int) {
    if index == 0 {
        this.AddAtHead(val)
        return
    }

    node := this.Head
    for i := 0; i < index-1; i++ {
        if node == nil {
            // Index is greater than the length of the linked list
            return
        }
        node = node.Next
    }
    if node == nil {
        // Index is greater than the length of the linked list
        return
    }

    newNode := &Node{
        Val:  val,
        Next: node.Next,
    }
    node.Next = newNode
    if newNode.Next == nil {
        this.Tail = newNode
    }
}


func (this *MyLinkedList) DeleteAtIndex(index int)  {
    if index == 0 { //deleting head
        if this.Head != nil { //head exists
            this.Head = this.Head.Next //delete head
            if this.Head == nil { //case where head is also tail
                this.Tail = nil
            }
        }
        return
    }
    node := this.Head
    for i:=0; i< index-1; i++ {
        if node == nil {
            // Index was greater than length of the LL
            return 
        }
        node = node.Next
    }
    if node == nil {
        return
    }

    if node.Next !=nil { //node to be deleted exists, reminder node points to 1 before node[index]
        node.Next = node.Next.Next // delete node.next 
        if node.Next == nil { //if node.next.next was nil, node.next was the tail, we just deleted the tail
            this.Tail = node
        }
    }

}


/**
 * Your MyLinkedList object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Get(index);
 * obj.AddAtHead(val);
 * obj.AddAtTail(val);
 * obj.AddAtIndex(index,val);
 * obj.DeleteAtIndex(index);
 */