/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let numsLen = nums.length
    let dupCount = 0
    let cleanArr = nums.reduce((acc, curr) => {
        if (!acc.includes(curr)) {
            acc.push(curr) 
            dupCount = 0
        } else if (dupCount == 0) {
            acc.push(curr)
            dupCount++
        }
        return acc
    }, [])
    
    let cleanLen = cleanArr.length
    

    for (let i = 0; i < numsLen ;i++) {
        nums[i] = cleanArr[i]
    }
    nums.splice(cleanLen,numsLen-cleanLen)
    return cleanLen
};