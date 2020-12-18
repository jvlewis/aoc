const fs = require("fs");

const year = 2020;
const accounts = fs.readFileSync("account.txt", "utf-8").split("\r\n");

const findProductOfTwo = (ledger) => {
  let pastValues = [];
  let firstVal, temp;

  for (i in ledger) {
    firstVal = Number(ledger[i]);
    temp = year - firstVal;

    if (pastValues.includes(temp)) return temp * firstVal;
    pastValues.push(firstVal);
  }
};

const findProductOfThree = (ledger) => {
  let pastValues = [];
  let firstVal, secondVal, temp;
  ledger = ledger;

  for (i in ledger) {
    firstVal = Number(ledger[i]);

    for (j in ledger) {
      secondVal = Number(ledger[j]);
      temp = year - secondVal - firstVal;

      if (pastValues.includes(temp)) {
        return temp * secondVal * firstVal;
      }
      pastValues.push(firstVal);
    }
  }
};

console.log(findProductOfTwo(accounts));
console.log(findProductOfThree(accounts));
