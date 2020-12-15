const fs = require("fs");

const processList = (list) => {
  list.forEach((e, i) => {
    list[i] = e.split(":");
    list[i][1] = list[i][1].trim();
    list[i][0] = list[i][0].split(" ");
    list[i][0][0] = list[i][0][0].replace("-", " ").split(" ");
    list[i] = list[i].flat(2);
  });
  return list;
};

const countCharacterOccurences = (string, char) => {
  let sum = 0;
  for (let ch of string) {
    if (ch === char) {
      sum += 1;
    }
  }
  return sum;
};

// solution one
const validSledRentalPasswords = (rulesAndPass) => {
  let valid = 0;

  rulesAndPass.forEach((pass) => {
    let count = countCharacterOccurences(pass[3], pass[2]);

    if (count >= Number(pass[0]) && count <= Number(pass[1])) {
      valid++;
    }
  });

  return valid;
};

// solution two
const validOfficialPasswords = (rulesAndPass) => {
  let valid = 0;

  rulesAndPass.forEach((pass) => {
    let word = pass[3];
    let char = pass[2];
    if (
      (word[Number(pass[0]) - 1] === char) ^
      (word[Number(pass[1]) - 1] === char)
    ) {
      valid += 1;
    }
  });

  return valid;
};

const accounts = processList(
  fs.readFileSync("input.txt", "utf-8").split("\r\n")
);

console.log(validSledRentalPasswords(accounts));
console.log(validOfficialPasswords(accounts));
