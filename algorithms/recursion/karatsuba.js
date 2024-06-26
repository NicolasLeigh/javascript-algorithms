// Create a lookup table of all single-digit multiplication products:
let MULT_TABLE = {};
for (let i = 0; i < 10; i++) {
  for (let j = 0; j < 10; j++) {
    MULT_TABLE[[i, j]] = i * j;
  }
}

function padZeros(numberString, numZeros, insertSide) {
  // Return a string padded with zeros on the left or right side.
  if (insertSide === 'left') {
    return '0'.repeat(numZeros) + numberString;
  } else if (insertSide === 'right') {
    return numberString + '0'.repeat(numZeros);
  }
}

function karatsuba(x, y) {
  // Multiply two integers with the Karatsuba algorithm. Note that
  // the * operator isn't used anywhere in this function.
  console.assert(Number.isInteger(x), 'x must be an integer');
  console.assert(Number.isInteger(y), 'y must be an integer');
  x = x.toString();
  y = y.toString();

  // At single digits, look up the products in the multiplication table:
  if (x.length === 1 && y.length === 1) {
    // BASE CASE
    console.log(
      `Lookup ${x} * ${y} = ${MULT_TABLE[[parseInt(x), parseInt(y)]]}`
    );
    return MULT_TABLE[[parseInt(x), parseInt(y)]];
  }

  // RECURSIVE CASE
  console.log(`Multiplying ${x} * ${y}`);

  // Pad with prepended zeros so that x and y are the same length:
  if (x.length < y.length) {
    // If x is shorter than y, pad x with zeros:
    // x = padZeros(x, y.length - x.length, 'left');
    x = x.padStart(y.length, '0');
  } else if (y.length < x.length) {
    // If y is shorter than x, pad y with zeros:
    // y = padZeros(y, x.length - y.length, 'left');
    y = y.padStart(x.length, '0');
  }
  // At this point, x and y have the same length.

  let halfOfDigits = Math.floor(x.length / 2);

  // Split x into halves a & b, split y into halves c & d:
  let a = parseInt(x.substring(0, halfOfDigits));
  let b = parseInt(x.substring(halfOfDigits));
  let c = parseInt(y.substring(0, halfOfDigits));
  let d = parseInt(y.substring(halfOfDigits));

  // Make the recursive calls with these halves:
  let step1Result = karatsuba(a, c); // Step 1: Multiply a & c.
  let step2Result = karatsuba(b, d); // Step 2: Multiply b & d.
  let step3Result = karatsuba(a + b, c + d); // Step 3: Multiply a + b & c + d.

  // Step 4: Calculate Step 3 - Step 2 - Step 1:
  let step4Result = step3Result - step2Result - step1Result;

  // Step 5: Pad these numbers, then add them for the return value:
  let step1Padding = (x.length - halfOfDigits) * 2;
  let step1PaddedNum = parseInt(
    padZeros(step1Result.toString(), step1Padding, 'right')
  );

  let step4Padding = x.length - halfOfDigits;
  let step4PaddedNum = parseInt(
    padZeros(step4Result.toString(), step4Padding, 'right')
  );

  console.log(
    `Solved ${x} + ${y} = ${step1PaddedNum + step2Result + step4PaddedNum}`
  );

  return step1PaddedNum + step2Result + step4PaddedNum;
}

// Example: 1357 x 2468 = 3349076
console.log('1357 * 2468 = ' + karatsuba(1357, 2468).toString());
