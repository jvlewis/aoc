const fs = require("fs");

const rightThreeDownOne = (path) => {
  let right = 0;
  path.shift();

  return path.reduce((trees, cur) => {
    return (trees += cur[(right += 3) % cur.length] === "#" ? 1 : 0);
  }, 0);
};

const prodAllSlopes = (path) => {
  let R1D1 = (R3D1 = R5D1 = R7D1 = R1D2 = 0);
  let i1 = (i2 = i3 = i4 = i5 = 0);
  for (let i = 0; i < path.length; ++i) {
    R1D1 += path[i][(i1 += 1) % path[i].length] === "#" ? 1 : 0;
    R3D1 += path[i][(i2 += 3) % path[i].length] === "#" ? 1 : 0;
    R5D1 += path[i][(i3 += 5) % path[i].length] === "#" ? 1 : 0;
    R7D1 += path[i][(i4 += 7) % path[i].length] === "#" ? 1 : 0;
    if (i % 2 === 0 && i !== 0 && i < path.length - 1) {
      R1D2 += path[i][(i5 += 1) % path[i].length] === "#" ? 1 : 0;
    }
  }
  return R1D1 * R3D1 * R5D1 * R7D1 * R1D2;
};

const pathway = fs.readFileSync("input.txt", "utf-8").split("\r\n");

console.log(rightThreeDownOne(pathway));
console.log(prodAllSlopes(pathway));
