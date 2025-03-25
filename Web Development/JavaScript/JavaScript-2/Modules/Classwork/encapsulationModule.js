const encapsulationModule = (function() {
    let privateVar = "This is a private variable";

    function getPrivateVar() {
        return privateVar;
    }

    return {
        getPrivateVar: getPrivateVar
    };
})();

export const getPrivateVar = encapsulationModule.getPrivateVar;
export default encapsulationModule;