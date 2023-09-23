/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let uniqueArr = [...new Set(nums)]
    let i = 0
    for (i; i < nums.length ;i++) {
        nums[i] = uniqueArr[i]
    }
    nums.splice(uniqueArr.length,Number.MAX_SAFE_INTEGER)
    
    return i+1;
};  