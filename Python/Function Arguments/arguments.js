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

loadCode("../../Python/Function Arguments/main.py", 'codeDisplay1');
loadCode("../../Python/Function Arguments/nile.py", 'codeDisplay2');
loadCode("../../Python/Function Arguments/project.py", 'codeDisplay3');
loadCode("../../Python/Function Arguments/test.py", 'codeDisplay4');