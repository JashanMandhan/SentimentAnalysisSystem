function analyzeSentiment() {
    const text = document.getElementById("inputText").value;  // Get input text

    // Send POST request to backend
    fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text: text })  // Send text as JSON
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("result").innerText = "Sentiment: " + data.sentiment;
    })
    .catch(error => {
        console.error("Error:", error);
    });
}
