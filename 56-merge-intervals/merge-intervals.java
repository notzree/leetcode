class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        ArrayList<int[]> output = new ArrayList<>();
        output.add(intervals[0]);

        for (int i = 1; i <intervals.length; i++){
            int [] pair = intervals[i];
            int[] last_pair = output.get(output.size()-1);   
            int last_endpoint = last_pair[1];

            if (pair[0]<=last_endpoint){
                //merge them
                output.get(output.size()-1)[1] = Math.max(last_endpoint,pair[1]);
            }
            else {
                output.add(pair);
            }
        }
        int[][] array = new int[output.size()][2];
        for (int i = 0; i < output.size(); i++) {
            int[] array1 = output.get(i);
            array[i] = array1.clone(); // Creates a deep copy of each array
        }
        return array;
        
    }
}
