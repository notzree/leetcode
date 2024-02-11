import java.util.HashMap;

class Solution {
    public int countVowelSubstrings(String word) {
        int vowels = 0;
        int count = 0;
        // only vowels + minimum all vowels
        HashMap <Character, Integer> map = new HashMap<>();
        map.put('a',0);
        map.put('e',0);
        map.put('i',0);
        map.put('o',0);
        map.put('u',0);
        int start = 0;
        int end = 0;


        //window is maintained by start/end. these don't actually indicate the start or end of the window itself. 
        //the largest valid window is from start->i
        //the smallest valid window is from (end-1)->i
        //The start/end pointers maintain the range of extra characters that we can include or not include and still have a valid window
        //in other words, start-end == # of unique windows (substrings) at a given i.
        //When we have a valid minimum window (vowels ==5), we are going to try to compute the smallest valid window and assume the window we just
        //found is the largest valid window.
        for (int i = 0; i<word.length(); ++i){
            if (map.get(word.charAt(i)) != null){
                map.put(word.charAt(i), map.get(word.charAt(i))+1);
                if (map.get(word.charAt(i))==1){
                    ++vowels;
                }
                while (vowels == 5) {
                    // attempt to shrink window, these will all be vowels since if we encountered a constant we would adjust our start/end pointers
                    map.put(word.charAt(start), map.get(word.charAt(start))-1);
                    if (map.get(word.charAt(start))==0){ // shrinking the window would result in an invalid window
                        --vowels;
                    }
                    start++;
                }
                count = count + (start-end);
            }
             else {
                 //constant encountered, reset window 
                 map.forEach((k,v)->{
                     map.put(k,0);
                 }); 
                start = end = i+1; //move the start and end pointers to the next valid location 
                vowels =0;
             }
        }
        return count;
    }
}