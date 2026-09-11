/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
// 167. Two Sum II - Input Array Is Sorted (Medium)
var twoSum = function (numbers, target) {
  let i = 0;
  let j = numbers.length - 1;

  while (i < j) {
    const sum = numbers[i] + numbers[j];
    if (sum === target) {
      return [i + 1, j + 1]; // 1-indexed
    }
    if (sum < target) {
      i++;
    } else {
      j--;
    }
  }

  return [];
};
