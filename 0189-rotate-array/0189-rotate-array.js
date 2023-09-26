/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {

    let spliceIndex
    let numLen = nums.length

 
    spliceIndex = numLen - k
    
    // splice works w/ negative numbers so long as arr[startIndex + arrSize] exists
    while (spliceIndex + numLen < 0) {
        spliceIndex += numLen
    }


    let chunk = nums.splice(spliceIndex, k)
    let newArr = chunk.concat(nums)
    
    newArr.forEach((_, i) => {
        nums[i] = newArr[i]
    })
    
    
    
    
    
    
    
    
    
    
    
    
    

    // UNSHIFT IS TOO SLOW
    // for (let i = 0; i < k; i++) {
    //     nums.unshift(nums.pop())
    // }
};