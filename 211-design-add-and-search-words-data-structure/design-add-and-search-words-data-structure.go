type WordDictionary struct {
    root *Node
}

type Node struct {
    isWord bool
    children [26] *Node
}



func Constructor() WordDictionary {
    dummyNode := &Node{
        isWord: false,
        children: [26] *Node{},
    }
    return WordDictionary{
        root: dummyNode,
    }
}


func (this *WordDictionary) AddWord(word string)  {
    itr := this.root
    for i,c :=range word {
        charIndex := getIndex(c)
        if itr.children[charIndex] == nil {
            newNode := &Node{
                isWord :(i==len(word)-1),
                children: [26]*Node{},
            }
            itr.children[charIndex] = newNode
        }
        itr = itr.children[charIndex]
        if i ==len(word)-1 {
            itr.isWord = true
        }
    }
}


func (this *WordDictionary) Search(word string) bool {
    itr := this.root
    runes := []rune(word)
    return dfs(itr, runes, 0)
}

func dfs(root *Node, word []rune, idx int) bool {
    if root == nil {
            return false
        }

    if idx == len(word){
        return root.isWord
    }
    char := word[idx]
    if char == '.' {
        for _, child :=range root.children{
            if child != nil {
                if dfs(child, word, idx+1) {
                    return true
                }
            }
        }
        return false
    }
    if root.children[getIndex(char)] == nil {
        return false
    }
    return dfs(root.children[getIndex(char)], word, idx+1)
}




func getIndex(char rune) int {
    return int(char-'a')
}





/**
 * Your WordDictionary object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddWord(word);
 * param_2 := obj.Search(word);
 */