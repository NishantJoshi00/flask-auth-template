# Flask Backend Template implementing Authentication
This is a flask application that implements authentication with sqlite database
This is functional to PoC, and should not be used in production
## Implementation
- Using the `flask_login` module implemented security with login, signup, logout API calls.
- Using `sqlite` database for storing the user information
- hashing the password before saving them into the database

## Warning
- The password is communicated from client-to-server in unencrypted manner, please implement SSL/TLS for improved security
- The API calls do not have DoS protection, neither they have, any validation mechanism, please implement they before using them
- There is in-code comment documentation for understanding the code, please read it carefully before using this template

## Credits
Check the websits below for the detailed documentation reference
- **Flask** : [Visit Here!](https://flask.palletsprojects.com/en/1.1.x/)
- **halfmoon** : [Visit Here!](https://gethalfmoon.com/)
