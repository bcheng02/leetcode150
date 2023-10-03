/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    if (nums.length == 1) return true
    let goal = nums.length - 1
    
    for (let i = goal - 1;  i >= 0; i--) {
        if (nums[i] + i >= goal) goal = i
        if (goal == 0) return true
    }
    return false

};