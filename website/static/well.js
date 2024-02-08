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
  let newState = 1 - currentValue;
  
  // Update the button text or perform any other actions based on the value
  if (currentValue == 0) {
      button.textContent = "Not Found";
      button.value = newState
      button.className = 'item-button well_radio';
      button.classList.add("notfound")
  }
  else if (currentValue == 1) {
      button.textContent = "Found";
      button.value = newState
      button.className = 'item-button well_radio';
      button.classList.add("completed")
  }
  else {
      button.textContent = `Value: ${currentValue}`;
  }
  let buttonID = button.id;
  let buttonDone = currentValue;
  updateType(buttonID, buttonDone)

  // You can use the 'currentValue' variable in other parts of your script as needed
  console.log('Current Value:', currentValue);
}

function updateType(buttonID, buttonDone) {
  console.log("ButtonID ->", buttonID);
  console.log("ButtonDone ->", buttonDone);

  const data = {
  well_id: parseInt(buttonID),
  well_done: parseInt(buttonDone),
  };
  console.log("DATA ->", data)
  
  fetch('/update_well', {
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
  well_sort: sortBy,
  };
  console.log("DATA ->", data)
  
  fetch('/sort_well_region', {
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