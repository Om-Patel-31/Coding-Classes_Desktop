"use strict";

function validate() {
    undeclaredVariable = "This will cause an error in strict mode";
}

export { validate };