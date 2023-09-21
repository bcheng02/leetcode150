/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    // trim to right length
    let merged = nums1.slice(0, m).concat(nums2.slice(0, n))
                                  .sort((a, b) => a - b)

    // nums1.forEach((curr, i, arr) => curr = merged[i])

    for (let i = 0; i < m + n; i++) {
        nums1[i] = merged[i]
    }
};