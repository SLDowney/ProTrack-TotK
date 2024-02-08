window.addEventListener('DOMContentLoaded', function () {
  console.log("-----------------------------")
  document.addEventListener('submit', function(event) {
    //const selectedItem = itemForm.elements.item_name.options[itemForm.elements.item_name.selectedIndex];
  // console.log("SortBy ->", selectedItem);
  })
});

function cycleValues(button) { 
  let currentValue = button.value;
  console.log("Button: ", button)
  let newState = 1 - currentValue;
  
  // Update the button text or perform any other actions based on the value
  if (currentValue == 0) {
      button.textContent = "Not Found";
      button.value = 1 - currentValue
      button.className = 'item-button chest_radio';
      button.classList.add("notfound")
  }
  else if (currentValue == 1) {
      button.textContent = "Found";
      button.value = 1 - currentValue
      button.className = 'item-button chest_radio';
      button.classList.add("completed")
  }
  else {
      button.textContent = `Value: ${currentValue}`;
  }
  let buttonID = button.id;
  let buttonDone = currentValue;
  let chestItem = button.getAttribute('item');
  updateType(buttonID, buttonDone, chestItem)

  // You can use the 'currentValue' variable in other parts of your script as needed
  console.log('Current Value:', currentValue);
}

function updateType(buttonID, buttonDone, chestItem) {
  console.log("ButtonID ->", buttonID);
  console.log("ButtonDone ->", buttonDone);chestItem
  console.log("chestItem ->", chestItem);

  const data = {
  chest_id: parseInt(buttonID),
  chest_done: parseInt(buttonDone),
  chest_item: chestItem,
  };
  console.log("DATA ->", data)
  
  fetch('/update_chest', {
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
function addChest(form) {

    form = document.getElementById('addChest');
    let doneCheckbox = form.querySelector('#done');
    let doneValue = doneCheckbox.checked ? 1 : 0;
    let chestItem = form.querySelector('#chest_item').value;
    let chestType = form.querySelector('#chest_type').value;
    let chestCoord = form.querySelector('#chest_coord').value;
    let chestLocation = form.querySelector('#chest_location').value;
    let chestRegion = form.querySelector('#chest_region').value;
    let chestSideQ = form.querySelector('#chest_sideq').value;
    if (chestSideQ == "") {
      chestSideQ = null;
    }

    const data = {
        done: doneValue,
        chest_item: chestItem,
        chest_type: chestType,
        chest_coord: chestCoord,
        chest_region: chestRegion,
        chest_location: chestLocation,
        chest_sideq: chestSideQ
    };
    console.log("Data ->", data)
    fetch('/add_chest', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
      },
      body: JSON.stringify(data),
  })
  .then(response => {
      if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
      }
      return response.json();
  })
  .then(data => {
      if (data.success) {
          console.log('Chest added successfully:', data);
          // Handle success, e.g., show a success message to the user
      } else {
          console.error('Chest addition failed:', data);
          // Handle failure, e.g., show an error message to the user
      }
  })
  .catch(error => {
      console.error('Fetch error:', error);
})
}
      



function updateSort(sortBy) {
  
  const data = {
  chest_sort: sortBy,
  };
  console.log("DATA ->", data)
  
  fetch('/sort_chest_region', {
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