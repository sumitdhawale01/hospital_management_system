// Your JavaScript code for handling dynamic behavior goes here
// You can use AJAX to interact with a backend server for data processing

// Example:
const patientList = document.getElementById('patient-list');

function loadPatients() {
    fetch('/api/patients')
        .then(response => response.json())
        .then(data => {
            data.forEach(patient => {
                const listItem = document.createElement('li');
                listItem.textContent = patient.name;
                patientList.appendChild(listItem);
            });
        });
}

loadPatients();

// JavaScript for the homepage

// Function to display a welcome message
function displayWelcomeMessage() {
    const welcomeMessage = document.createElement('p');
    welcomeMessage.textContent = 'Welcome to our Hospital Management System!';
    const homeSection = document.getElementById('home');
    homeSection.appendChild(welcomeMessage);
}

// Function to handle a button click event
function handleButtonClick() {
    alert('Button clicked!');
}

// Add an event listener to the button element
const buttonElement = document.getElementById('myButton');
buttonElement.addEventListener('click', handleButtonClick);

// Call the displayWelcomeMessage function when the page loads
window.addEventListener('load', displayWelcomeMessage);

// JavaScript for the responsive navigation menu
const navbarToggle = document.querySelector('.navbar-toggle');
const navbarLinks = document.querySelector('.navbar-links');

navbarToggle.addEventListener('click', () => {
    navbarLinks.classList.toggle('active');
});


