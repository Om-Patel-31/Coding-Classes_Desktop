'use strict';
function testStrictMode() {
    undeclaredVariable = 10; // This will cause an error in strict mode
    console.log(undeclaredVariable);
}
export { testStrictMode };