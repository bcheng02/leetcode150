/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    let objTally = nums.reduce((acc, curr) => {
        if (!acc[curr]) acc[curr] = 0
        acc[curr]++
        return acc
    }, {})
    
    let maxOccurence = 0
    let majItem
    for (let ele in objTally) {
        if (objTally[ele] > maxOccurence) {
            maxOccurence = objTally[ele]  
            majItem = ele
        } 
    }
    return majItem
};