bool containsDuplicate(int* nums, int numsSize) {
   
    int min = nums[0];
    int max = nums[0];

    for(int i = 0; i < numsSize; i++) {
        if(min > nums[i]) min = nums[i];
        if(max < nums[i]) max = nums[i];
    }

    printf("max: %d\n", max);
    printf("min: %d\n", min);

    int capacity = max - min + 1;

    printf("capacity %d\n", capacity);
    int *hashmap = calloc(capacity, sizeof(int));
    
    for(int i = 0; i < numsSize; i++){
        if(hashmap[nums[i]-min] >= 1) {
            free(hashmap);
            return true;
        }

        hashmap[nums[i]-min]++;
        
    }

    return false;

}