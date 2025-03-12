function getRecommendations() {
    let userText = document.getElementById("userText").value;

    fetch("/recommend", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: userText })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("sentiment").innerText = data.sentiment;
        
        let recList = document.getElementById("recommendations");
        recList.innerHTML = "";
        data.recommendations.forEach(song => {
            let li = document.createElement("li");
            li.innerText = `${song.Song_Name} - ${song.Artist} [${song.Genre}]`;
            recList.appendChild(li);
        });
    })
    .catch(error => console.error("Error:", error));
}
