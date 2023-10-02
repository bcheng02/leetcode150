/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {

    let obj = {}
    
    for (let i = 0; i < nums.length; i++) {
        let curr = nums[i]
        let diff = target - curr
    
        if (obj[diff] >= 0) {           // make sure the key exists
            return [obj[diff], i]
        }
        obj[curr] = i

    }
};