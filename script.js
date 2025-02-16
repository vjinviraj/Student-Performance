document.getElementById("predictForm").addEventListener("submit", async function (event) {
    event.preventDefault();

    let studyHours = document.getElementById("studyHours").value;
    let previousScore = document.getElementById("previousScore").value;
    let resultDiv = document.getElementById("result");

    try {
        let response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                study_hours: studyHours,
                previous_score: previousScore
            })
        });

        let data = await response.json();
        resultDiv.innerHTML = `Prediction: <span style="color: #ff007f">${data.prediction}</span>`;
    } catch (error) {
        resultDiv.innerHTML = "Error predicting!";
        console.error("Error:", error);
    }
});
