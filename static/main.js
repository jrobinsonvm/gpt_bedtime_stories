document.getElementById("storyForm").addEventListener("submit", function(event){
    event.preventDefault()

    console.log('Form submission detected.');

    let name = document.getElementById("name").value
    let age = document.getElementById("age").value
    let mood = document.getElementById("mood").value
    let todaysEvent = document.getElementById("event").value  // Changed variable name from 'event' to 'todaysEvent'
    let model = document.getElementById("model").value

    let data = {name: name, age: age, mood: mood, event: todaysEvent, model: model}  // Changed 'event' to 'todaysEvent'

    console.log('Form data:', data);

    fetch('http://192.168.1.37:5001/api/v1/resources/gpt4all', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        document.getElementById("story").innerText = data
    })
    .catch((error) => {
        console.error('Fetch error:', error);
    });
})
