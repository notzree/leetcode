class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        Stack<int[]> output = new Stack<>();
        output.add(intervals[0]);

        for (int i = 1; i <intervals.length; i++){
            int [] pair = intervals[i];
            int[] last_pair = output.peek();  
            int last_endpoint = last_pair[1];

            if (pair[0]<=last_endpoint){
                //merge them
                output.pop();
                last_pair[1] = Math.max(last_endpoint,pair[1]);
                output.push(last_pair);
            }
            else {
                output.push(pair);
            }
        }
        int[][] array = new int[output.size()][2];
        for (int i = output.size()-1; i >=0; i--) {
            int[] array1 = output.pop();
            array[i] = array1.clone(); // Creates a deep copy of each array
        }
        return array;
        
    }
}
