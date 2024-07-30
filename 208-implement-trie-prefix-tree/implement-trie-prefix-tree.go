type Trie struct {
    root *Node
}


func Constructor() Trie {
    return Trie{
        root: &Node{
            Char: '_',
            isWord: false,
            children: [26]*Node{},
        },
    }
}


func (this *Trie) Insert(word string)  {
    itr := this.root
    wordLength := len(word)
    for index, char := range word {
        char_as_val := getIndex(char)
        if itr.children[char_as_val] == nil { //insert newNode
            newNode := &Node{
                Char: char,
                isWord: (index==wordLength-1),
                children: [26]*Node{},
            }
            itr.children[char_as_val] = newNode
        }
        itr = itr.children[char_as_val] 
        if index == wordLength -1 {
            itr.isWord = true
        }
    }
}


func (this *Trie) Search(word string) bool {
    itr := this.root
    for _, char := range word {
        char_as_val := getIndex(char)
        if itr.children[char_as_val]== nil {
            return false
        }
        itr = itr.children[char_as_val]
    }
    return (itr.isWord)
}


func (this *Trie) StartsWith(prefix string) bool {
    itr := this.root
    for _, char := range prefix {
        char_as_val := getIndex(char)
        if itr.children[char_as_val]== nil {
            return false
        }
        itr = itr.children[char_as_val]
    }
    return true
}

type Node struct {
    Char rune
    isWord bool
    children [26] *Node
}

func getIndex(char rune) int {
    return int(char - 'a')
}



/**
 * Your Trie object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Insert(word);
 * param_2 := obj.Search(word);
 * param_3 := obj.StartsWith(prefix);
 */