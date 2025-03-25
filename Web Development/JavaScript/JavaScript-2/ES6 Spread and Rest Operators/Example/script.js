const arr1 = [1, 2, 3];
const arr1Copy = [...arr1];
console.log(arr1Copy);

const arr2 = [4, 5, 6];
const combinedArr = [...arr1, ...arr2];
console.log(combinedArr);

const obj1 = {foo: 'bar'};
const obj1Copy = {...obj1};
console.log(obj1Copy);

const obj2 = {baz: 'qux'};
const combinedObj = {...obj2, ...obj1};
console.log(combinedObj);

const combined = {...arr1, ...obj1};
console.log(combined);

function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}
console.log(sum(1, 2, 3));
console.log(sum(1, 2, 3, 4, 5));

function testRestParameter(...args){
    console.log(args);
}
function testArgumentsObject() {
    console.log(arguments);
}
testRestParameter(1, 2, 3);
testArgumentsObject(1, 2, 3);

function mergeArrays(...arrays) {
    let merged = [];
    for (let arr of arrays) {
        merged.push(...arr);
    }
    return merged;
}
console.log(mergeArrays(arr1, arr2));

