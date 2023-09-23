/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let uniqueArr = [...new Set(nums)]
    nums.forEach((_, i) => {
        nums[i] = uniqueArr[i]
    })
    return uniqueArr.length
};  