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
    console.log("current Value: ", button.value);
    let newState = 1 - currentValue;

    // Remove existing classes
    button.classList.remove("notfound", "completed");

    // Add the appropriate class based on the new state
    if (newState == 0) {
        console.log("Leaving Button == 0, ", currentValue);
        button.textContent = "Not Found";
        button.classList.add("notfound");
    } else if (newState == 1) {
        console.log("Leaving Button == 1, ", currentValue);
        button.textContent = "Found";
        button.classList.add("completed");
    }

    // Update the button value after updating the text and class
    button.value = newState;

    let buttonID = button.id;
    let buttonDone = newState;
    console.log("Leaving cycleValues");
    updateType(buttonID, buttonDone);
}

function updateType(buttonID, buttonDone) {
  console.log("ButtonID ->", buttonID);
  console.log("ButtonDone ->", buttonDone);

  const data = {
  tear_id: parseInt(buttonID),
  tear_done: parseInt(buttonDone),
  };
  console.log("DATA ->", data)
  
  fetch('/update_tear', {
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

function updateSort(sortBy) {
  
  const data = {
  tear_sort: sortBy,
  };
  console.log("DATA ->", data)
  
  fetch('/sort_tear_region', {
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