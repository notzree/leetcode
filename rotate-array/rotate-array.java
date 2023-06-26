class Solution {
    public void rotate(int[] nums, int b) {
        int k = b % nums.length;
        reverse(nums,0,nums.length-1);
        reverse(nums,0,k-1);
        reverse(nums,k,nums.length-1);
    }
    public void reverse (int [] nums , int s, int e ){
        
        while (e>s){
          int  temp = nums[s];
            nums[s] = nums[e];
            nums[e] = temp;
            s++;
            e--;
        }
    }
}