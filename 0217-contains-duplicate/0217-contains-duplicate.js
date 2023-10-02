/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let uniqueArr = [...new Set(nums)]
    return (uniqueArr.length !== nums.length)
};