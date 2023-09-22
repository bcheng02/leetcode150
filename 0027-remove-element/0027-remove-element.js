/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
// var removeElement = function(nums, val) {
//     let filtered = nums.filter(x => x !== val)
//     nums.forEach((_, i) => nums[i] = filtered[i])
//     return filtered.length
// };

var removeElement = function(nums, val) {
    let index = 0;

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            nums[index] = nums[i];
            index++;
        }
    }

    return index;
};
