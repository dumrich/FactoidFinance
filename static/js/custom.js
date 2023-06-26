count = 1;
function addTextBox() {
    event.preventDefault()
    // Clone the text box element
    var textBox = document.getElementById("addSource");
    var newTextBox = textBox.cloneNode(true);

    var field1 = newTextBox.querySelector('input[name="text_box_"]');
    field1.setAttribute('name', 'text_box_' + count);
    count += 1;

    // Add the new text box element to the page
    var container = document.getElementById("helluh");
    container.appendChild(newTextBox);
}


// Get reference to the input field and create a popup element
const inputField = document.getElementById('search-field');
const dropdownMenu = document.getElementById('dropdown-menu');

// Function to make API request and create the popup
function handleInput() {
  const query = inputField.value;

  // Make the API request
  fetch(`https://financialmodelingprep.com/api/v3/search?query=${query}&limit=5&apikey=5ca77484426a734fc5edcc3f08c06eb1`)
    .then(response => response.json())
    .then(data => {
        dropdownMenu.innerHTML = '';
        if (data.length > 0) {
            data.forEach(result => {
            const item = document.createElement('a');
            item.classList.add('dropdown-item');
            item.textContent = result.symbol;
            item.textContent = result.symbol;
            item.href = `/stocks/${result.symbol}`; 
            dropdownMenu.appendChild(item);
        });

        dropdownMenu.style.display = 'block';
      } else {
        dropdownMenu.style.display = 'none';
      }
        console.log(data);
    })
    .catch(error => {
      console.log('Error:', error);
    });
}

// Attach event listener to the input field
inputField.addEventListener('input', handleInput);
