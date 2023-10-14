/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    let len = nums.length
    
    let pre = [nums[0]]
    for (let i = 1; i < len; i++) {
        pre[i] = pre[i - 1] * nums[i]
    }
    console.log(pre)
    
    
    
    let post = []
    post[len - 1] = nums[len - 1]
    for (let i = len - 2; i >= 0; i--) {
        post[i] = post[i + 1] * nums[i]
    }
    console.log(post)
    
    
    let ans = []
    for (let i = 0; i < len; i++) {
        let prePart = (pre[i - 1] !== undefined) ? pre[i - 1] : 1    // be careful since 0 is considered falsy
        console.log(`pre: ${prePart}`)
        let postPart = (post[i + 1] !== undefined) ? post[i + 1] : 1 // be careful since 0 is considered falsy
        console.log(`post: ${postPart}`)

        ans[i] = prePart * postPart
    }
    console.log(ans)
    return ans
};