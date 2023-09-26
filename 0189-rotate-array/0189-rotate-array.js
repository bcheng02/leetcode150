/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {

//     let spliceIndex
//     let numLen = nums.length

 
//     spliceIndex = numLen - k
    
//     // splice works w/ negative numbers so long as arr[startIndex + arrSize] exists
//     while (spliceIndex + numLen < 0) {
//         spliceIndex += numLen
//     }


//     let chunk = nums.splice(spliceIndex, k)
//     let newArr = chunk.concat(nums)
    
//     newArr.forEach((_, i) => {
//         nums[i] = newArr[i]
//     })
    
    
    
    
    
    
    
    // change each index
    let numLen = nums.length
    let maxIndex = numLen - 1
    let numsCopy = [...nums]
    
    for (let i = 0; i < numLen; i++) {
        let swapIndex = i - k
        while (swapIndex < 0) {
            swapIndex += numLen
        }
        nums[i] = numsCopy[swapIndex]
    }
    
    
    
    

    // UNSHIFT IS TOO SLOW
    // for (let i = 0; i < k; i++) {
    //     nums.unshift(nums.pop())
    // }
};