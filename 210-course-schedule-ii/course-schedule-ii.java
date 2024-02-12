import java.util.*;
class Solution {
    ArrayList<Integer> output = new ArrayList<>();
    HashSet<Integer> visited = new HashSet<>();
    HashSet<Integer> cycle = new HashSet<>(); //help us detect cycles\
    HashMap<Integer, ArrayList<Integer>> adj = new HashMap<>();
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        //build adj list
        for (int i=0; i <prerequisites.length; i++){
            int course = prerequisites[i][0];
            int preq = prerequisites[i][1];
            if (!adj.containsKey(course)){
                adj.put(course,new ArrayList<>());
            }
            adj.get(course).add(preq);
        }
        //course has 3 states: 
        //visited (added to output), 
        //unvisited(not added to either), 
        //visiting (course not added to output but added to cycle)

        // Try to visit each course
        for (int i = 0; i < numCourses; i++) {
            if (!visited.contains(i)) {
                if (!dfs(i)) {
                    return new int[0]; // Return an empty array if a cycle is detected
                }
            }
        }

        int[] array = new int[output.size()];
        for (int i = 0; i < output.size(); i++) {
            array[i] = output.get(i); 
        }
        return array;
    }

    public boolean dfs(int course){
        if (cycle.contains(course)){
            return false; //cycle detected
        }
        if (visited.contains(course)){
            return true;
        }
        cycle.add(course);
         for (Integer preq : adj.getOrDefault(course, new ArrayList<>())) {
            if (!dfs(preq)){
                return false;
            }
        }
        //we keep dfs-ing, if we made it here it means that all of the preqs are satisfied and we have finished searching down this branch. 
        //We can remove the cur course from the cycle as we have completed 1 branch of traversal. We can also add it into the output as we have added all of its pre-reqs recursively.
        cycle.remove(course);
        visited.add(course);
        output.add(course);
        return true;
        


    }


}