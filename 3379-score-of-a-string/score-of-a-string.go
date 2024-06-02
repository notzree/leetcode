func scoreOfString(s string) int {
    sum :=0
    for c :=0; c < len(s)-1; c++ {
        diff := int(s[c]) - int(s[c+1])
        current_sum := int(math.Abs(float64(diff)))
        sum +=current_sum
    }
    return sum
}