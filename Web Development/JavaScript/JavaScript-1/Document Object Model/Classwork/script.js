// #1
document.getElementById('myPara').innerText = 'My Paragraph';

// #2
document.querySelector("#container img").src = "dog.jpg";

// #3
var newParagraph = document.createElement('p');
newParagraph.innerText = "New Element";
document.getElementById('container').appendChild(newParagraph);

// #4
document.getElementById('myPara').style.color = 'blue';

// #5
document.getElementById('myButton').addEventListener('click', function(){
    alert('Button clicked!');
});

// #6
document.querySelector("input").addEventListener("change", function() {
    document.getElementById("myPara").innerText = document.querySelector('input').value;
});