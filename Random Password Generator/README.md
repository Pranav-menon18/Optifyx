# Python Random Password Generator

This repository contains two versions of random password generator implemented in Python: a CONSOLE version and a GUI version. Both applications are designed to generate secure random passwords while providing a user-friendly experience.

## Features

- **Password Generation:** Generates random passwords based on user-defined criteria.
- **Error Handling:** Both versions include robust error handling to guide users.
- **User-Friendly:** Each version is designed to be intuitive and easy to use.
- **Customization Options:** Users can choose to include uppercase letters, lowercase letters, digits, and special characters.
- **Copy Functionality:** Easily copy generated passwords to your clipboard.

## Error Handling

Both applications handle the following errors:

- **Invalid Length:** Prompts the user to enter a valid password length.
- **Invalid Numbers:** Ensures that numeric inputs are valid where required.
- **General Exceptions:** Catches unexpected errors and provides helpful feedback to the user.

## Installation

1. To get started, clone this repository to your local machine:
    
    ```bash
    git clone https://github.com/Mohamed-ait-alla/Python-Random-Password-Generator.git
2. Navigate to the project directory
    
    ```bash
    cd Python-Random-Password-Generator

## Requirements

- Make sure you have Python 3.x installed on your Windows operating system. You may need to install additional modules that do not come with pip.

- For the console version, install the following modules:

    ```bash
    pip install termcolor pyfiglet pyperclip
    
- For the GUI version, install:

    ```bash
    pip install tkinter pyperclip

## Usage

1. To run the console version:

    ```bash
    python random_password_generator_console_version.py  
2. To run the GUI version:

    ```bash
    python random_password_generator_gui_version.py
## Example Interaction

### Console version

<p style="align: center">
   <img src="demo/console-example-interaction.gif">
</p>

### Gui version

<p style="align: center">
   <img src="demo/gui-example-interaction.gif">
</p>

## Contributing

Contributions are welcome! If you have suggestions or improvements, feel free to open an issue or submit a pull request.
