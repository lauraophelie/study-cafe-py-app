# Study café

Study cafe is a game-styled study app, made in Python, that simulates the look of a 'study cafe' where student can go order food and drink while also having a cozy, peaceful place to study with other people. The app contains various features such as a timer, some lofi music (for the music enjoyers), and a to-do list features to stay organized, a chat system. 

**Project Status → 90% done** 

## 📂 Technologies & tools used
- **Programming language :** python
- **Tools use :** Figma for protyping, Aseprite for the pixel art
- **Library used (in python):** fernet, json, socket, pygame, cryptography, tkinter, pyglet (to load fonts), pillow (for images)
- **Others :** Lospec (https://lospec.com/) for the color palette

## 📂 Key concepts used
- **Socket programming :** using socket to establish the connection between the server and the clients 
- **Hybrid cryptography :** asymetric & symetric cryptography both used to ensure a secure communication on a public channel using the Diffie-Hellman exchange keys
- **Game development :** displaying the sprite on the window, handling collisions and movements, adding objetcs onto the background

## 📂 Key features

- **Starting a study session :** the user open the app and start a study session by providing his username and the duration of the session (measured in hour); after providing those informations the user is then added inside an empty room
- **Joining a study session :** the user (a 'friend') can join an on-going study session by providing and username and an encrypted link from the host (the 'server'); once it's done and everything is in-check, the user is then added in the same study room as the host 

## 📂 Process
The base idea was to make an app with a pixel-art styled UI where you could join your friends in the same "room" and you could study "together" or just study solo in a pretty room. 

To make it work, I then had the idea to split it into two (02) key features : 
- one where the student could create / open a new study room (and later, they could invite their friend if wanted or just stay solo)
- and another where the student could just join another student by simply providing a link and an unique username.

The project started by simply writing down everything needed for the project : from the basic elements to the details of the two (02) core features of the app but also a basic sketch of the screens. It is an important part for me to write everything down first to give you more structure and more clarity on the idea before diving into the coding aspect. 

Additional researchs were also made : inspirations pictures for the UI part, color palette, simple code such as implementing socket communication in python, how to use pygame, etc.

For the UI part : a good amount of time were spent looking at inspirations pictures then drawing the assets in Aseprite following the chosen color palette but also following some tutorial found on the internet as it was my very first time doing pixel art.

Then, obviously, the rest of the time was dedicated to the coding part, running various tests and debugging. 

## 📂 Installation

To run the project, you'll need to install the following elements : 
- Python 3.10 (https://www.python.org/)
- PIP (https://pip.pypa.io/en/stable/installation/)

Once those two are installed and working properly, install the following packages by running the command : 

```
pip install ...
```


## 📂 Contact

If you have any questions or any feedback to give about this project, feel free to reach out : 
- Author : [Laura Ophélie](https://github.com/lauraophelie)
- Email : lauraophelie1@gmail.com

---

*Thank you for using **Study Café**! If you find this project helpful, please consider giving it a star ⭐.*


