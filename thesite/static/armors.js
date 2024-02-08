window.addEventListener('DOMContentLoaded', function () {
    console.log("-----------------------------")
});

function cycleValues(button) {
    let currentValue = button.value;
    console.log("current Value: ", button.value);
    let newState = 1 - currentValue;

    // Remove existing classes
    button.classList.remove("notfound", "completed");

    // Add the appropriate class based on the new state
    if (newState == 0) {
        console.log("Leaving Button == 0, ", currentValue);
        button.classList.add("notfound");
    } else if (newState == 1) {
        console.log("Leaving Button == 1, ", currentValue);
        button.classList.add("completed");
    }

    // Update the button value after updating the text and class
    button.value = newState;

    let buttonID = button.id;
    let buttonDone = newState;
    let buttonItem = button.getAttribute('item');
    console.log("Leaving cycleValues");
    updateType(buttonID, buttonDone, buttonItem);
}

function updateType(buttonID, buttonDone, buttonItem) {
    console.log("ButtonID ->", buttonID); 
    console.log("ButtonDone ->", buttonDone);
  
    const data = {
    armor_id: parseInt(buttonID),
    armor_done: parseInt(buttonDone),
    armor_item: buttonItem,
    };
    console.log("DATA ->", data)
    
    fetch('/update_armor', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
      console.log('Response from server:', data);
    })
    .catch(error => {
      console.error('Error:', error);
    });
}