// 4.
console.log('4.');
array1 = [1, 2, 3, 4, 5];
array2 = [...array1];
console.log(array2);

//5.
console.log('5.');
combArr1 = [1, 2, 3];
combArr2 = [4, 5, 6];
combArr3 = [...combArr1, ...combArr2];
console.log(combArr3);

//6.
console.log('6.');
const obj1 = {'name': 'John', 'age': 25};
const obj2 = {...obj1};
console.log(obj2);

//7.
console.log('7.');
combObj = {...obj1, ...obj2};
console.log(combObj);

//8.
console.log('8.');
numArr = [1, 2, 3, 4, 5];
newObj = {2: 'two', 3: 'three'};
combArr = [...numArr, ...newObj];
console.log(combArr);

//9.
console.log('9.');
function sum(...numbers) {
    return numbers.reduce((total, num) => total + num, 0);
}
console.log(sum(1, 2, 3, 4, 5));

//10.
console.log('10.');
function testRestParameter(...args) {
    console.log(args);
}
testRestParameter(1, 2, 3, 4, 5);

//11.
console.log('11.');
function mergeArrays(...array) {
    return array.reduce((total, arr) => total.concat(arr), []);
}

//12.
arr1 = [1, 2, 3];
arr2 = [4, 5, 6];
arr3 = [7, 8, 9];
console.log(mergeArrays(arr1, arr2, arr3));