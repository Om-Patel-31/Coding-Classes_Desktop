// #1
document.getElementById("hwPara").innerText = "I am doing my HW";

// #2
document.querySelector("#hwBox video").src = "cat.mp4";

// #3
const newPara = document.createElement("p");
newPara.innerText = "Adding a new para";
document.getElementById("hwBox").appendChild(newPara);

// #4
document.getElementById("hwPara").style.color = "green";

// #5
document.getElementById("hwButton").addEventListener("click", function() {
    alert("Hello / Bonjour!");
});

// #6
document.querySelector("#hwInput").addEventListener("change", function() {
    const inputValue = this.value;
    document.getElementById("hwPara").innerText = inputValue;
});