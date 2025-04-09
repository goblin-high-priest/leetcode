/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
 int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    typedef struct hashTable {
        int key;
        int value;
        UT_hash_handle hh;
    } *hashTable;
    hashTable ht = NULL, item, tmpItem;

    for (int i = 0; i < numsSize; i++) {
        int diff = target - nums[i];
        HASH_FIND_INT(ht, &diff, item);
        if (item) {
            int* result = malloc(sizeof(int) * 2);
            result[0] = item->value;
            result[1] = i; 
            *returnSize = 2;
            HASH_ITER(hh, ht, item, tmpItem) {
                HASH_DEL(ht, item);
                free(item);
            }
            return result;
        }
        item = malloc(sizeof(struct hashTable));
        item->key = nums[i];
        item->value = i;
        HASH_ADD_INT(ht, key, item);
    }
    HASH_ITER(hh, ht, item, tmpItem) {
        HASH_DEL(ht, item);
        free(item);
    }
    *returnSize = 0;
    return malloc(sizeof(int) * 0);
}