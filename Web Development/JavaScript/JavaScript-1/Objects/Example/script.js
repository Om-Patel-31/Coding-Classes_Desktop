// Simulating fetching JSON data from a server
const jsonDataFromServer = '{"name": "John Doe", "age": 25, "city": "Exampleville", "isStudent": true, "courses": ["Javascript", "HTML", "CSS"]}';

// Parse the JSON data
const userObject = JSON.parse(jsonDataFromServer);

// Display user details in the HTML
const userDetailsElement = document.getElementById('userDetails');
userDetailsElement.innerHTML = `
    <p><strong>Name:</strong> ${userObject.name}</p>
    <p><strong>Age:</strong> ${userObject.age}</p>
    <p><strong>City:</strong> ${userObject.city}</p>
    <p><strong>Student:</strong> ${userObject.isStudent ? 'Yes' : 'No'}</p>
    <p><strong>Courses:</strong> ${userObject.courses.join(', ')}</p>
`;