/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function(citations) {
    const n = citations.length;
    let left = 1;
    let right = n + 1;

    while (left < right) {
        let mid = (left + right) >> 1;

        if (citations[n - mid] >= mid) {
            left += 1;
        } else {
            right = mid;
        }
        
    }

    return left - 1;
};