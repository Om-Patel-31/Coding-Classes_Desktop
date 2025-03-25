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

loadCode("../../Python/Strings/Strings.py", 'codeDisplay1');
loadCode("../../Python/Strings/String_Methods.py", 'codeDisplay2');
loadCode("../../Python/Strings/Code_Challenge.py", 'codeDisplay3');
loadCode("../../Python/Strings/dailysales.py", 'codeDisplay4');