/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    // [..."apple"].sort().join('') = 'aelpp'
    
    let myObj = strs.reduce((acc, curr) => {
        let currSorted = [...curr].sort().join('')  // sorted string
        if (!acc[currSorted]) acc[currSorted] = []
        acc[currSorted].push(curr)
        return acc
    }, {})
    
    return Object.values(myObj) 
};