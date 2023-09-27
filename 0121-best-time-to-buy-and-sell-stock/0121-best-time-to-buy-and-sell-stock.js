/**
 * @param {number[]} prices
 * @return {number}
 */
// [7,1,5,3,6,4]
var maxProfit = function(prices) {
    /* V1
    // NESTED FOR LOOPS, O(n^2) TOO SLOW
    let profit = 0
    let curr
    let diff 
    
    for (let i = 0; i < prices.length - 1; i++) {
        curr = prices[i]
        for (let j = i+1; j < prices.length; j++) {
            diff = prices[j] - curr
            if (diff > profit) profit = diff
        }
    }
    
    
//     nested for loops proof of concept
//     let myArr = [1,3,5,7]

//     for (let i = 0; i < myArr.length - 1; i++) {
//         console.log(myArr[i])
//         for (let j = i + 1; j < myArr.length; j++) {
//             console.log(myArr[j])
//         }
//     }
//     1 3 5 7 3 5 7 5 7
    
    
    return profit
    */
    
    
    let currMin = prices[0]
    let profit = 0
    
    for (let i = 1; i < prices.length; i++) {
        let curr = prices[i]
        if (curr < currMin) {
            currMin = curr
        } else {
            profit = Math.max(profit, curr - currMin)
        }
    }
    return profit
   
};