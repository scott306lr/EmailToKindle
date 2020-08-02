# EmailToKindle
Directly sends an email from Gmail to Kindle.

### Features

* Sends mails with an attachment of books inside the *books* folder.
* Remembers the names of the book sent in the past, books with the same name won't be sent again. 
* For users who doesn't have python, I've added .exe version.

## How to use EmailToKindle

### Requirements

You'll have to [enable "less secure apps access"](https://myaccount.google.com/lesssecureapps) in order for this app to work./
I will find away to avoid this steo in the future.

### Usage

Drag the books(or documents) you would like to send into the *books* folder, then execute _**send.py**_ or _**send.exe**_ .\
It's up to you whether to delete the books sent before or not, same books won't be sent twice.

### Getting Started

To get the program working, you will have to fill up the data inside _**info.json**_ which looks like this:
``` 
{
    "gmailAddress": "yourMail@gmail.com",
    "gmailPassword": "yourPassword",
    "kindleAddress": "yourMail@kindle.com"
}
```
replace your email and password inside the brackets.\
Enjoy!









