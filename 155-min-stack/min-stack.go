
func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

type MinValue struct{
    Value int
    MinValue int
}

type MinStack struct {
    Stack []MinValue
}


func Constructor() MinStack {
     return MinStack{
        Stack:make([]MinValue,0),
     }
}

func (this *MinStack) Push(val int)  {
    if len(this.Stack)==0{
        mv := MinValue{
            Value: val,
            MinValue: val,
        }
        this.Stack = append(this.Stack, mv)
        return
    }
    minvalue := min(this.Stack[len(this.Stack)-1].MinValue, val)
    mv := MinValue{
        Value: val,
        MinValue: min(minvalue, val),
    }
    this.Stack = append(this.Stack, mv)
}


func (this *MinStack) Pop()  {
    this.Stack = this.Stack[:len(this.Stack)-1]
}


func (this *MinStack) Top() int {
    prev := this.Stack[len(this.Stack)-1]
    return prev.Value
}


func (this *MinStack) GetMin() int {
    prev := this.Stack[len(this.Stack)-1]
    return prev.MinValue
    
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(val);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */