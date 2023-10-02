/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let array_s = JSON.stringify([...s].sort())
    let array_t = JSON.stringify([...t].sort())
    return array_s == array_t
};