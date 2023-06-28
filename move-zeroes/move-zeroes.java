class Solution {
    public void moveZeroes(int[] nums) {
        int s = 0;
        
        int temp;
        for (int i = 0 ; i<nums.length;i++){
            temp = nums[i];
            if (nums[i]!=0){
                temp = nums[i];
                nums[i] = 0;
                nums[s]= temp;
                
                
                s++;
            }
            
        }
    }
}