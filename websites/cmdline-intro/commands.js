// Initialize current step tracker for both Linux and Windows tabs
let currentStep = {
    linux: 0,
    windows: 0
};

// Commands for each step for Linux and Windows
let commands = {
    linux: [
        'mkdir my_folder',  // Step 1
        'cd my_folder',     // Step 2
        'touch file.txt',   // Step 3
        'rm file.txt'       // Step 4
    ],
    windows: [
        'mkdir my_folder',  // Step 1
        'cd my_folder',     // Step 2
        'echo. > file.txt', // Step 3
        'del file.txt'      // Step 4
    ]
};

// Track the currently active tab (default is 'linux')
let activeTab = 'linux';

// Store all card elements for both Linux and Windows
let linuxSteps = Array.from(document.querySelectorAll('#linux .card'));
let windowsSteps = Array.from(document.querySelectorAll('#windows .card'));

// Get the Next Step button
let nextButton = document.getElementById('next-step');

// Tree structure content for Linux and Windows
let treeStructure = {
    linux: [
        ["->Root/      "],                             // Initial state before any command
        ["->Root/      ", " └──my_folder/"],           // After mkdir
        ["Root/        ", " └──>my_folder/"],            // After mkdir + cd
        ["Root/        ", " └──>my_folder/", "    └──file.txt"], // After touch (file created)
        ["Root/        ", " └──>my_folder/"]             // After rm (file deleted)
    ],
    windows: [
        ["->C:\\        "],                            // Initial state before any command
        ["->C:\\        ", " └──my_folder\\"],            // After mkdir
        ["C:\\          ", " └──>my_folder\\"],            // After mkdir + cd
        ["C:\\          ", " └──>my_folder\\", "    └──file.txt"], // After echo (file created)
        ["C:\\          ", " └──>my_folder\\"]             // After del (file deleted)
    ]
};

// Check if the user typed the correct command
function checkCommand(tab) {
    let userInput = document.getElementById(`${tab}-input-${currentStep[tab] + 1}`).value.trim();
    let correctCommand = commands[tab][currentStep[tab]];

    // Show the Next Step button only if the command is correct
    if (userInput === correctCommand) {
        nextButton.style.display = 'inline-block'; // Show button
    } else {
        nextButton.style.display = 'none'; // Hide button if the command is incorrect
    }
}

// Show the next step when the "Next Step" button is clicked
function showNextStep() {
    let correctCommand = commands[activeTab][currentStep[activeTab]];

    // Only proceed if the command is correct
    let userInput = document.getElementById(`${activeTab}-input-${currentStep[activeTab] + 1}`).value.trim();
    if (userInput === correctCommand) {
        // Hide the current step's card
        let currentStepCard = (activeTab === 'linux') ? linuxSteps[currentStep[activeTab]] : windowsSteps[currentStep[activeTab]];
        currentStepCard.classList.add('hidden');

        // Increment the step
        currentStep[activeTab]++;

        // Show the next step if there are remaining steps
        if (currentStep[activeTab] < (activeTab === 'linux' ? linuxSteps.length : windowsSteps.length)) {
            let nextStepCard = (activeTab === 'linux') ? linuxSteps[currentStep[activeTab]] : windowsSteps[currentStep[activeTab]];
            nextStepCard.classList.remove('hidden');
        } else {
            nextButton.style.display = 'none'; // Hide the button after all steps are completed

            // Show "All Completed" message
            showCompletionMessage();
        }

        // Show tree structure for the current tab
        updateTreeStructure();
    }
}

// Show the "All Completed" message with confetti and a refresh button
function showCompletionMessage() {
    const completionMessage = document.createElement('div');
    completionMessage.textContent = "All Completed!";
    completionMessage.classList.add('completion-message');
    document.body.appendChild(completionMessage);

    // Create the refresh button
    const refreshButton = document.createElement('button');
    refreshButton.textContent = "Refresh Page";
    refreshButton.classList.add('refresh-button', 'next-step');
    refreshButton.onclick = function() {
        location.reload(); // Reload the page when clicked
    };
    document.body.appendChild(refreshButton);

    // Trigger confetti effect
    triggerConfetti();
}

// Trigger confetti on the page
function triggerConfetti() {
    // Include confetti library (this example uses a CDN for canvas-confetti)
    const script = document.createElement('script');
    script.src = "https://cdn.jsdelivr.net/npm/canvas-confetti@1.4.0/dist/confetti.browser.min.js";
    document.body.appendChild(script);

    script.onload = () => {
        // Trigger confetti once the script is loaded
        confetti({
            particleCount: 200,
            spread: 70,
            origin: { y: 0.6 }
        });
    };
}

// Update the tree structure to reflect the current state
function updateTreeStructure() {
    let treeOutput = treeStructure[activeTab][currentStep[activeTab]] || [];
    document.getElementById('tree-structure').textContent = treeOutput.join('\n');  // Join the tree structure array into a string
}

// Switch between tabs
function switchTab(tab) {
    activeTab = tab;

    // Update the visible tab and hide the other
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });

    document.getElementById(tab).classList.add('active');
    updateTreeStructure();  // Update the tree structure immediately for the selected tab
    currentStep[tab] = 0; // Reset to the first step for the selected tab

    // Hide the next step button
    nextButton.style.display = 'none';

    // Hide all steps initially
    linuxSteps.forEach(step => step.classList.add('hidden'));
    windowsSteps.forEach(step => step.classList.add('hidden'));

    // Show the first step for the selected tab
    let firstStep = (tab === 'linux') ? linuxSteps[0] : windowsSteps[0];
    firstStep.classList.remove('hidden');

    // Show the command input area for the selected tab
    displayCommands(tab);
}

// Display the commands for the selected OS inside the cards
function displayCommands(tab) {
    // Clear any previous command display outside of the cards
    linuxSteps.forEach((step, index) => {
        step.querySelector('.command-text').textContent = commands.linux[index] || '';
    });

    windowsSteps.forEach((step, index) => {
        step.querySelector('.command-text').textContent = commands.windows[index] || '';
    });
}

// Show the OS selection modal when the page loads
function showOSSelection() {
    const modal = document.querySelector('.modal');
    modal.style.display = 'flex'; // Display the modal
}

// Close the modal and initialize the selected OS
function closeOSModal(os) {
    const modal = document.querySelector('.modal');
    modal.style.display = 'none'; // Hide the modal

    // Set the theme based on user selection
    if (os === 'linux') {
        document.body.classList.add('linux-theme');
        document.body.classList.remove('windows-theme');
        activeTab = 'linux';
    } else if (os === 'windows') {
        document.body.classList.add('windows-theme');
        document.body.classList.remove('linux-theme');
        activeTab = 'windows';
    }

    // Show the correct tab and commands
    switchTab(activeTab);
}

// Initial prompt when the page loads
window.onload = function() {
    showOSSelection(); // Show the OS selection modal
};
