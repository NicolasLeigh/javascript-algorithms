/**
 * @param {number} x
 * @return {boolean}
 */
// 9. Palindrome Number
function isPalindrome(x) {
  if (x < 0) {
    return false;
  }
  if (x < 10) {
    return true;
  }

  const s = x.toString();
  const len = s.length;

  for (let i = 0; i <= Math.floor(len / 2); i++) {
    if (s[i] !== s[len - 1 - i]) {
      return false;
    }
  }

  return true;
}

const answer = (x) => {
  if (x < 0) return false;
  if (x < 10) return true;
  const s = x.toString();
  const len = s.length;
  for (let i = 0; i <= Math.floor(len / 2); i++) {
    if (s[i] !== s[len - i - 1]) return false;
  }
  return true;
};
