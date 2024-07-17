type RandomizedSet struct {
    random_map map[int]int // k-> integer value v -> index in random array
    random_array []int
}


func Constructor() RandomizedSet {
    return RandomizedSet{
        random_map: make(map[int]int),
        random_array: make([]int,0),
    }
}


func (this *RandomizedSet) Insert(val int) bool {
    if _,ok := this.random_map[val]; ok {
        return false
    } 
    this.random_array = append(this.random_array, val) //Adds value to the end of the array
    this.random_map[val] = len(this.random_array)-1 //assign the index of the value to the value in the map
    return true
}


func (this *RandomizedSet) Remove(val int) bool {
    index, ok := this.random_map[val]
    if !ok {
        return false
    }

    lastElement := this.random_array[len(this.random_array)-1] //store last element
    this.random_array[index] = lastElement //replace element[index] with last element
    this.random_map[lastElement] = index //update the map for replaced element (reassign index from end -> index)

    this.random_array = this.random_array[:len(this.random_array)-1] //Remove the last element
    delete(this.random_map, val) //Delete from map

    return true
}


func (this *RandomizedSet) GetRandom() int {
    random := rand.IntN(len(this.random_array))
    return this.random_array[random]
}


/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */