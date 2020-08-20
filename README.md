# Flask Backend Template implementing Authentication
This is a flask application that implements authentication with sqlite database
This is functional to PoC, and should not be used in production
## Implementation
- Using the `flask_login` module implemented security with login, signup, logout API calls.
- Using `sqlite` database for storing the user information
- hashing the password before saving them into the database

## Warning
- The password is communicated from client-to-server in unencrypted manner, please implement SSL/TLS for improved security
- The API calls do not have DoS protection, neither they have, any validation mechanism, please implement this before using them
- There is in-code comment documentation for understanding the code, please read it carefully before using this template

## Try it out
If you want to check it out, follow the instructions given below
> This was built on a linux machine thus the automation that is provided in the documentation will not work on windows
1. First check if make is installed, if not install `make` from your package manager

2. Run the command `make build` > (For windows user read the contents of the makefile's build section to get the list of commands)

    > Please check out how to use virtualenv on windows for understand the commands

3. For deploying the application locally, try running `make run` > (Same as above read the run section of the makefile to find the commands and their windows counterpart)

## Credits
Check the websits below for the detailed documentation reference
- **Flask** : [Visit Here!](https://flask.palletsprojects.com/en/1.1.x/)
- **halfmoon** : [Visit Here!](https://gethalfmoon.com/)
