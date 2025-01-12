# Eternal Encouragement
#### Video Demo: https://youtu.be/Ec2yQxWwp5A
### <ins>Description<ins>

Eternal Encouragement is a website made for the purpose of allowing users to easily access timeless advice from the Bible. We can't control every situation in our lives, but we can control how we act with the emotions that a situation may produce. The purpose of this site is to help with such circumstances.

At the bottom of the homepage, users can type out the emotion/emotions that they are experiencing or addictions that they are struggling with. Once the user is done typing, multiple bible verses are generated that relate to the emotions/temptations expressed in the text box. Next to the verse on the screen, an image of the person who authored the book is generated. Clicking on the image will produce a popup that gives important and interesting information about that author.



### __verses.db__
 The verses.db file contains a SQLite database of bible verses and its info that the app.py file uses for gathering information. The data is organized into four columns:

 - **emotion**: The emotion that the verse portrays
 - **verse**: The verse
 - **reference**: The reference of the verse (Example: "Psalms 23:1")
 - **id**: An autoincrementing unique id for each bible verse in the database

#### **Database Initialization Script**
- **Purpose**: This script(**'input_verses.py'**) is used to manually populate the 'verses.db' SQLite database with initial data
- **Usage**: To add new data, modify the "data" variable with new entries for 'emotion', 'verse', and 'reference'. This was repeated multiple times to fill the SQLite database.
- **Note**: This script is intended for initial database setup and occasional updates. The functionality of the website is not dependant on this file.


### __app.py__

The app.py file serves as the main entry point for our Flask application, facilitating various functionalities of the web interface. Below are the key features and configurations contained in this file:

- **Flask Configuration**: Initializes the Flask app and configures session management to use the filesystem instead of signed cookies, ensuring that session data is stored securely on the server.

- **Cache Settings**: Implements caching policies in the after_request function to ensure that the browser does not cache any responses. This ensures that users always receive the most current data from the server.

- **Routes**
    - **'/'**: The root route clears any existing session data and displays the homepage.
    - **'/verses'**: Manages the core functionality of the website. This route handles database interactions to retrieve verses based on emotional context from the user input, updates session state, and randomizes the order of the verses presented. It also prepares additional data for rendering, like images and author information associated with the verses.
    - **'/error'**: Displays an error page whenever the website encounters an issue.
    - **'/contact'**: Provides a contact form for users to reach out with questions or feedback.
- **Helpers: Utilizes helper functions from a seperate file (helpers.py)**
    - **'synonym_check'**: Analyzes the user input to connect the text to an emotion.
    - **'image_find'**: Fetches the image of the author related to the verse.
    - **'popup_info'**: Retrieves information about the author of the verse that is displayed.
- **Database Interaction**
    - Connects a SQLite Database('verses.db') to query verses based on the identified emotions. Handles database connections and queries based on the state of the user's session.

### __helpers.py__

The helpers.py file stores functions that aid app.py in grabbing specific information from the user input. Below are the functions in this file and their purpose:

- **'synonym_check'**
    - **Parameters**
        - 'text' (str): The user input's text that needs to be analyzed
    - **Returns**
        - If successful, a list containing the general words for the synonyms in the user text is returned.
        - If no word were matched and the 'matched_list' list is empty, "error" is returned.
    - **Functionality**
        1. **Preprocessing Text**
            - Removes punctuation from the input text using 'str.maketrans' and 'translate'.
            - Lowercases all the letters in the string.
        2. **Matching Synonym**
            - The function contains a predefined dictionary named 'synonyms'. Inside are keys that are general words for the the list of values that it pertains to.
            - It splits the preprocessed text and loops through each word to check if the word is in any of the list of values in the 'synonym' dictionary.
            - If the word is matched, the key that corresponds is appended to a list ('matched_list').
- **'image_find'**
    - **Parameters**
        - 'reference' (str): The reference of the verse. (Example: 'Psalms 23:1')
    - **Returns**
        - The name of the person who authored the book.
    - **Functionality**
        - The function contains a predefined dictionary named 'books_by_author'. The name of the author is the key and the the value is a list of books that the author wrote.
        - The reference is split and all of the contents of the reference are removed instead of the name of the book.
        - The function loops through each key and value pair in the dictionary until one of the book names in the dictionary match up with the reference that was given to the function.

- **'popup_info'**
    - **Parameters**
        - 'author' (str): The name of an author of a book in The Holy Bible.
    - **Returns**
        - A mini biography of the author
    - **Functionality**
        - The function contains a predefined dictionary named 'author_info'. The name of the author is the key and the value is string of text that contains important and interesting information of the author.
        - '.get' is used to find the key in the dictionary that matches the author inputted into the function and gets back its value.

### Templates Directory

The templates folder contains HTML files used by Flask to render the web pages for the application. The files are described below:
- **layout.html**: The base template for all the HTML files. Contains the navigation bar and links that are used in the other HTML files.
- **homepage.html**: The landing page of the application. Contains the text box that the user types in to.
- **verses.html**: The page that the user is directed to once the user submits its input from the homepage. Renders the verse related to the query and the author of the verse. It dynamically displays content based on user input and database interactions.
- **contact.html**: Contains a contact form for users to give feedback or ask questions.
- **error.html**: Displays an error page if the application encounters an error.

### Static Directory
The static folder contains images that are used by Flask to render on the web page when a query is made. It also contains a css folder ('styles.css') that the HTML files are formatted with.
