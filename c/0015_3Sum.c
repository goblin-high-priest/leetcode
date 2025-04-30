/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
 int compare(const void* a, const void* b) {return (*(int*)a - *(int*)b);}
 void twoSum(int* nums, int numsSize, int i, int** result, int* returnSize, int* returnColumnSizes) {
     int left = i + 1;
     int right = numsSize - 1;
     while (left < right) {
         int sum = nums[i] + nums[left] + nums[right];
         if (sum < 0) {
             left++;
         } else if (sum > 0) {
             right--;
         } else {
             result[*returnSize] = (int*)malloc(sizeof(int) * 3);
             result[*returnSize][0] = nums[i];
             result[*returnSize][1] = nums[left++];
             result[*returnSize][2] = nums[right--];
             returnColumnSizes[*returnSize] = 3;
             (*returnSize)++;
             while(left < right && nums[left] == nums[left-1]) left++;
             while(left < right && nums[right] == nums[right+1]) right--;
         }
     }
 }
 int** threeSum(int* nums, int numsSize, int* returnSize, int** returnColumnSizes) {
     qsort(nums, numsSize, sizeof(int), compare);
     *returnSize = 0;
     int** res = (int**)malloc(sizeof(int*) * numsSize * numsSize);
     *returnColumnSizes = (int*)malloc(sizeof(int) * numsSize * numsSize);
     for (int i = 0; i < numsSize; i++) {
         if (nums[numsSize-1] < 0) break;
         if (i != 0 && nums[i] == nums[i-1]) continue;
         if (nums[i] > 0) break;
         twoSum(nums, numsSize, i, res, returnSize, *returnColumnSizes);
     }
     return res;
 }