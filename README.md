# Password Strength Checker

## Task

* Analyzes a password entered by the user.
* Classifies the password into one of three categories:

  * **Strong**
  * **Medium**
  * **Weak**
* Explains the requirements for creating a **Strong** password.

## Technology Used

* Python
* Regular Expressions (`re` module)

## Code Details

* The password must be at least **12 characters long**. If it is shorter, the user is prompted to enter a new password.

### Strong Password Requirements

A password is classified as **Strong** if it contains:

* At least one lowercase letter
* At least one uppercase letter
* At least one digit
* At least one special character

### Medium Password Requirements

A password is classified as **Medium** if it contains:

* At least one lowercase letter
* At least one uppercase letter
* At least one digit

### Weak Password

A password is classified as **Weak** if it contains only one type of character, such as:

* Only lowercase letters
* Only uppercase letters
* Only digits
