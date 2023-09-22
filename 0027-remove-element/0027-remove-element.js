/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let filtered = nums.filter(x => x !== val)
    nums.forEach((_, i) => nums[i] = filtered[i])
    return filtered.length
};