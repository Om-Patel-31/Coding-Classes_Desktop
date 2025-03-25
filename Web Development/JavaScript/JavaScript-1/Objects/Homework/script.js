// #1
let car = {};

car.make = "sports car(S)";
car.model = "Koenigsegg Jesko Absolut Street Legal";
car.year = "2020";
console.log(car.make);
console.log(car.model);
console.log(car.year);

// #2
car.year = "2021";
console.log(car.year);

// Remove a specified property (e.g., director) from the movie object
let movie = {
    title: "Inception",
    director: "Christopher Nolan",
    year: 2010
};

console.log("Before deletion:", movie);
delete movie.director;
console.log("After deletion:", movie);

// Apply Object.keys() to the car object and log the resulting array of property names
console.log(Object.keys(car));

// Use Object.values() on the movie object, then log the obtained array containing property values
console.log(Object.values(movie));

// Utilize Object.entries() on the car object and log the array of [key, value] pairs representing the object's properties
console.log(Object.entries(car));

// Create a JavaScript object named "song" representing details about a fictional song
let song = {
    title: "Fictional Song",
    artist: "Imaginary Artist",
    duration: "3:45"
};

// Use JSON.stringify() on the song object, save the result in a variable called "stringifiedSong," and log it
let stringifiedSong = JSON.stringify(song);
console.log(stringifiedSong);

// In your HTML file, create a div element with the ID "songDetails" to serve as a dedicated container for displaying information about a song
// <div id="songDetails"></div>

// Use JSON.parse() on "stringifiedSong" and store the result in a variable called "parsedSong."
let parsedSong = JSON.parse(stringifiedSong);

// Utilize innerHTML to display specific details, such as the song's title and artist, within the "songDetails" div
document.getElementById("songDetails").innerHTML = `Title: ${parsedSong.title}, Artist: ${parsedSong.artist}`;