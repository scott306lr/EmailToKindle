# EmailToKindle
Directly sends an email from Gmail to Kindle.

### Updates

* 2020/8/5 Changed to sending one mail with multiple attachments instead of the other way around. 
 * haven't checked if there is any limit for gmail or kindle with total attachment size or so.

### Features

* Sends mails with an attachment of books inside the _**books**_ folder.
* Remembers the names of the book sent in the past, those with the same name won't be sent again. 
* For users who doesn't have python, I've added *.exe* version.

## How to use EmailToKindle

### Requirements

You'll have to enable ["less secure apps access"](https://myaccount.google.com/lesssecureapps) option in gmail for this app to work.\
I will find away to avoid this step in the future.

### Usage

Drag the books (or documents) you would like to send into the *books* folder, then execute _**send.py**_ or _**send.exe**_ .\
It's up to you whether to delete the books sent before or not; same books won't be sent twice.

### Getting Started

To get the program working, you will have to fill up the data inside _**info.json**_ which looks like this:
``` 
{
    "gmailAddress": "yourMail@gmail.com",
    "gmailPassword": "yourPassword",
    "kindleAddress": "yourMail@kindle.com"
}
```
Replace your email and password inside the brackets.\
\
Inside _**books**_ folder, there is a sample document *"BookToBeSent.txt"* which should better be deleted before executing.\
\
That's all, enjoy!









