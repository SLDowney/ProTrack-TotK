window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  document.addEventListener('submit', function(event) {
    event.preventDefault(); 
    const selectedItem = itemForm.elements.item_name.options[itemForm.elements.item_name.selectedIndex];
  console.log("SortBy ->", selectedItem);
  })
});

function cycleValues(button) {
  let currentValue = button.value;
  console.log("Button Value: ", button.value)
  // Increment the value and loop back to 0 if it exceeds 2
  currentValue = (currentValue + 1) % 3;
  
  // Update the button text or perform any other actions based on the value
  if (currentValue == 0) {
      button.textContent = "Not Found";
      button.value = 0
      button.className = 'item-button shrine_radio';
      button.classList.add("notfound")
  }
  else if (currentValue == 1) {
      button.textContent = "Tapped";
      button.value = 1
      button.className = 'item-button shrine_radio';
      button.classList.add("started")
  }
  else if (currentValue == 2) {
      button.textContent = "Completed";
      button.value = 2
      button.className = 'item-button shrine_radio';
      button.classList.add("completed")
  }
  else {
      button.textContent = `Value: ${currentValue}`;
  }
  let buttonID = button.id;
  let buttonDone = currentValue;
  // updateInfo(button)
  updateType(buttonID, buttonDone)

  // You can use the 'currentValue' variable in other parts of your script as needed
  console.log('Current Value:', currentValue);
}

function cycleChests(button) {
  let currentValue = button.value;
    console.log("current Value: ", button.value);
    let buttonText = button.getAttribute('chest_item');
    let newState = 1 - currentValue;

    // Remove existing classes
    button.classList.remove("notfound", "completed");

    // Add the appropriate class based on the new state
    if (newState == 0) {
        console.log("Leaving Button == 0, ", currentValue); 
        button.textContent = "???"
        button.classList.add("notfound");
    } else if (newState == 1) {
        console.log("Leaving Button == 1, ", currentValue);
        button.textContent = buttonText;
        button.classList.add("completed");
    }

    // Update the button value after updating the text and class
    button.value = newState;

    let buttonID = button.id;
    let buttonDone = newState;
    let buttonChest = button.getAttribute('chest_id');
    console.log("Leaving cycleValues");
    updateChest(buttonID, buttonDone, buttonChest);
}

function updateType(buttonID, buttonDone) {
  console.log("ButtonID ->", buttonID);
  console.log("ButtonDone ->", buttonDone);

  const data = {
  shrine_id: parseInt(buttonID),
  shrine_done: parseInt(buttonDone),
  };
  console.log("DATA ->", data)
  
  fetch('/update_shrine', {
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

function updateChest(buttonID, buttonDone, buttonChest) {
  console.log("ButtonID ->", buttonID);
  console.log("ButtonDone ->", buttonDone);
  console.log("buttonChest ->", buttonChest);

  const data = {
  shrine_id: parseInt(buttonID),
  chest_id: parseInt(buttonChest),
  chest_done: parseInt(buttonDone),
  };
  console.log("DATA ->", data)
  
  fetch('/update_shrine_chest', {
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

function addshrine() {
  // Get values from the form
  const shrineDone = document.getElementById('shrine_done').value;
  const shrineName = document.getElementById('shrine_name').value;
  // Get other values similarly

  // Construct the JSON payload
  const payload = {
      shrine_done: shrineDone,
      shrine_name: shrineName,
      // Add other fields to the payload
  };

  // Make a POST request to the add_shrine route
  fetch('/add_shrine', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          // Handle success, e.g., show a success message
          console.log('shrine added successfully');
      } else {
          // Handle failure, e.g., show an error message
          console.error('Error adding shrine:', data.error);
      }
  })
  .catch(error => {
      console.error('Fetch error:', error);
  });
}

function updateSort(sortBy) {
  
  const data = {
  shrine_sort: sortBy,
  };
  console.log("DATA ->", data)
  
  fetch('/sort_shrine_region', {
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