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
      button.className = 'item-button cave_radio';
      button.classList.add("notfound")
  }
  else if (currentValue == 1) {
      button.textContent = "Found";
      button.value = 1
      button.className = 'item-button cave_radio';
      button.classList.add("started")
  }
  else if (currentValue == 2) {
      button.textContent = "Completed";
      button.value = 2
      button.className = 'item-button cave_radio';
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

function cycleBfrog(button) {
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
    console.log("Leaving cycleValues");
    updateBfrog(buttonID, buttonDone);
}

function updateType(buttonID, buttonDone) {
  console.log("ButtonID ->", buttonID);
  console.log("ButtonDone ->", buttonDone);

  const data = {
  cave_id: parseInt(buttonID),
  cave_done: parseInt(buttonDone),
  };
  console.log("DATA ->", data)
  
  fetch('/update_cave', {
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

function updateBfrog(buttonID, buttonDone) {
  console.log("ButtonID ->", buttonID);
  console.log("ButtonDone ->", buttonDone);

  const data = {
  cave_id: parseInt(buttonID),
  bfrog_done: parseInt(buttonDone),
  };
  console.log("DATA ->", data)
  
  fetch('/update_cave_bfrog', {
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

function addcave() {
  // Get values from the form
  const caveDone = document.getElementById('cave_done').value;
  const caveName = document.getElementById('cave_name').value;
  // Get other values similarly

  // Construct the JSON payload
  const payload = {
      cave_done: caveDone,
      cave_name: caveName,
      // Add other fields to the payload
  };

  // Make a POST request to the add_cave route
  fetch('/add_cave', {
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
          console.log('cave added successfully');
      } else {
          // Handle failure, e.g., show an error message
          console.error('Error adding cave:', data.error);
      }
  })
  .catch(error => {
      console.error('Fetch error:', error);
  });
}

function updateSort(sortBy) {
  
  const data = {
  cave_sort: sortBy,
  };
  console.log("DATA ->", data)
  
  fetch('/sort_cave_region', {
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