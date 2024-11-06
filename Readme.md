# Grievance Management Data Processing Tool

This tool helps process and transform grievance management data between Excel and JSON formats, with various data validation and transformation capabilities.


## Project Structure

    ├── main.py # Core conversion utilities
    ├── process-json.py # Processing pipeline
    ├── simulator.py # Automation
    └── json/ # Storing JSOn files
        ├── input/ # Input JSON files
        └── output/ # Processed JSON files

## Prerequisites

- Python 3.12
- Chromium/Google chrome (latest)
- ChromeDriver (for automation, v132)

### Running chrome/chromium

For this automation, we need to run chrome/chromium in a way, where we can later access a logged in user's data. To achieve this, follow the below steps


 🔵 Press <kbd>Win</kbd> + <kbd>R</kbd> to open `Run`

 🔵 Enter the command below and press <kbd>Enter</kbd>

```bash
chrome --remote-debugging-port=9222 --user-data-dir="C:\chromium\profile"
```

🔵 This should open a new chrome/chromium window

If you inspect your `C:\` drive a new folder `chromium` is created for our use. 
During following this readme, or usage of this project, if any time the chrome/chromium crashes, you may delete the `C:\chromium\profile` folder from `C:\chromium`. 

> ⚠️ Note: To use this project's scripts, always run the chrome/chromium with the same command given above.

### Chromedriver
ChromeDriver is a standalone server that implements the W3C WebDriver protocol for Chromium/Chrome. It is required for automated testing with Selenium WebDriver, allowing the test scripts to programmatically control Chrome browser sessions.

> 💡Download Chrome Driver: [Click here](https://www.chromedriverdownload.com/)

> ⚠️Once you have downloaded the chrome driver zip file, extract it and place the contents in `C:\chromium\driver` folder. If you followed the previous step, the `C:\chromium` folder was aleady created during [Running chrome/chromium](#running-chromechromium)


> 📝Note: Make sure to get the latest version and install the latest verion of chrome

Key points about ChromeDriver:

- Acts as a bridge between your automation code and Chrome browser
- Enables browser automation for testing web applications
- Must match your Chrome browser version


For this project, ChromeDriver is used by the simulator.py script to automate testing of the grievance management system through the Chrome browser.


## Installation

### 1. Clone the repository

```bash
git clone https://github.com/shanujha/complaints-pmc-selenium
```

### 2. Create virtual env 
> ⚠️ Note: Required step. Also make sure all the [Preqrequisites](#prerequisites) are met

```bash
python -m venv .venv
```

### 3. Activate virtual env
> 💡Note: How to activate a virtual environment depends on the OS and shell being used.

Here are a list of ways to activate a .venv depending on OS and shell. Use the appropriate command in your appropriate shell. <b>You have to run this command in the project directory.</b>

| Operating System | Shell | Command |
|-----------------|--------|---------|
| Windows | Command Prompt | `.venv\Scripts\activate.bat` |
| Windows | PowerShell | `.venv\Scripts\Activate.ps1` |
| Linux/macOS | bash/zsh | `source .venv/bin/activate` |
| Linux/macOS | fish | `source .venv/bin/activate.fish` |
| Linux/macOS | csh/tcsh | `source .venv/bin/activate.csh` |

After activation, your shell prompt should change to indicate you're working in the virtual environment.




### 4. Install required dependencies:

```bash
python -m pip install -r requirements.txt
```

### 5. Features

- Convert Excel files to JSON format
- Convert JSON files to Excel format
- Process JSON data through multiple transformation stages
- Validate and update data fields

#### 5.1 Processing Stages

1. Key Updates
2. Peth Type Processing
3. Ward Value Updates
4. Number Formatting
5. Prabhag Value Updates
6. Application Type Addition






## Usage

#### `main.py`

Main script for Excel-JSON conversions and data processing.

> 💡 Tip: Run command `python main.py` in terminal to see the usage of this file

- Handles Excel-JSON conversions
- Manages data type consistency
- Handles NaN values


#### `process-json.py`
> 💡 Tip: Run command `python process-json.py` in terminal to see the usage of this file

- Orchestrates the complete processing pipeline
- Manages file dependencies
- Coordinates transformation stages

#### `simulator.py`
> 💡 Tip: Run command `python simulator.py` in terminal to see the usage of this file

- Provides automation testing capabilities
- Validates dropdown selections
- Verifies data integrity


## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
