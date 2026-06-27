class Solution {
    public void sortColors(int[] nums) {
        int z = 0, o = 0;
        for(int i = 0; i < nums.length; i++){
            int key = nums[i];
            int j;
            if (key == 0){
                for(j=i; j > z; j--){
                    nums[j] = nums[j-1];

                }
                nums[j] = key;
                o++;
                z++;
            }
            else if (key == 1){
                for(j=i; j > o; j--){
                    nums[j] = nums[j-1];

                }
                nums[j] = key;
                o++;
            }
        }
       
    }
}