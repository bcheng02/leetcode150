/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let uniqueArr = [...new Set(nums)]
    let uniqueLen = uniqueArr.length
    let numsLen = nums.length
    
    // this should be a faster way to copy diff lengthed arrays...
    for (let i = 0; i < numsLen ;i++) {
        nums[i] = uniqueArr[i]
    }
    nums.splice(uniqueLen,numsLen-uniqueLen)
    
    return uniqueLen;
    
    // OLD RELIABLE
    // let uniqueArr = [...new Set(nums)]
    // nums.forEach((_, i) => {
    //     nums[i] = uniqueArr[i]
    // })
    // return uniqueArr.length
};  