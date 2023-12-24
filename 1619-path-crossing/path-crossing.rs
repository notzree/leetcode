use std::collections::HashSet;
impl Solution {
    pub fn is_path_crossing(path: String) -> bool {
        let mut map:HashSet<Vec<i32>> = HashSet::new();
        let mut curr: Vec<i32> = vec![0,0];
        map.insert(curr.clone());
        for c in path.chars(){
            println!("{},{}", curr[0], curr[1]);
            if c == 'N'{
                curr[0] = curr[0]+1
            }
            else if c == 'S'{
                curr [0] = curr[0]-1
            }
            else if c == 'E'{
                curr[1] = curr[1]+1
            }
            else if c == 'W'{
                curr[1] = curr[1]-1
            }
            
            if map.contains(&curr){
                return true
            } else{
                 map.insert(curr.clone());
            }
            

        
        }
        return false
    }
}