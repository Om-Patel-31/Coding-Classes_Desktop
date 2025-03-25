function loadCode(filePath, elementId) {
    fetch(filePath)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.text();
        })
        .then(data => {
            const lines = data.split("\n");
            let formattedCode = lines.map(line => `<span>${line}</span>`).join("\n");
            document.getElementById(elementId).innerHTML = formattedCode;
        })
        .catch(error => {
            console.error('Error loading the file:', error);
            document.getElementById(elementId).textContent = "Failed to load the code.";
        });
}

loadCode("../../Python/Dictionaries/script.py", 'codeDisplay1');
loadCode("../../Python/Dictionaries/usingdictionaries.py", 'codeDisplay2');
loadCode("../../Python/Dictionaries/codechallenge.py", 'codeDisplay3');
loadCode("../../Python/Dictionaries/scrabble.py", 'codeDisplay4');
loadCode("../../Python/Dictionaries/quiz.py", 'codeDisplay5');