/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let obj = nums.reduce((acc, curr)=>{
        if (!acc[curr]) acc[curr] = 0
        acc[curr]++
        return acc
    },{})
    
    let arr = []
    
    for (let prop in obj) {
        arr.push([prop, obj[prop]])
    }
    
    arr.sort((a, b) => a[1] > b[1] ? -1 : 1)
    
    let ans = []
    
    for(let i = 0; i < k; i++) {
        ans.push(arr[i][0])
    }
    
    return ans
    
};