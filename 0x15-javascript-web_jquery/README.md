# JavaScript - Web jQuery
* [What is JavaScript?](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_is_JavaScript)
* [Selector](https://jquery-tutorial.net/selectors/using-elements-ids-and-classes/)
* [Get and set content](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-content/)
* [Manipulate CSS classes](https://jquery-tutorial.net/dom-manipulation/getting-and-setting-css-classes/)
* [Manipulate DOM elements](https://jquery-tutorial.net/dom-manipulation/the-append-and-prepend-methods/)
* [API](https://oscarotero.com/jquery/)
* [Introduction](https://jquery-tutorial.net/ajax/introduction/)
* [GET & POST request](https://jquery-tutorial.net/ajax/the-get-and-post-methods/)
* [JQuery Ajax Tutorial #1 - Using AJAX & API’s](https://www.youtube.com/watch?v=fEYx8dQr_cQ)
* [What went wrong? Troubleshooting JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/What_went_wrong)
* [JQuery](https://jquery.com/)
* [JQuery API](https://api.jquery.com/)
* [JQuery Ajax](https://learn.jquery.com/ajax/)

## Tasks
### 0. No jQuery
A JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
* You must use `document.querySelector` to select the HTML tag
* You can’t use the JQuery API

File: [0-script.js](./0-script.js)

### 1. With jQuery
A JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API

File: [1-script.js](./1-script.js)

### 2. Click and turn red
A JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API

File: [2-script.js](./2-script.js)

### 3.Add `.red` class
A JavaScript script that adds the class `red` to the `<header>` element when the user clicks on the tag `DIV#red_header`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API

File: [3-script.js](./3-script.js)

### 4. Toggle classes
A JavaScript script that toggles the class of the `<header>` element when the user clicks on the tag `DIV#toggle_header`:
* The `<header>` element must always have one class: `red` or `green`, never both in the same time and never empty.
* If the current class is red, when the user click on `DIV#toggle_header`, the class must be updated to `green` ; and the reverse.
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API

File: [4-script.js](./4-script.js)

### 5. List of elements
A JavaScript script that adds a	`<li>` element to a list when the user clicks on the tag `DIV#add_item`:
* The new element must be: `<li>Item</li>`
* The new element must be added to `UL.my_list`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API

File: [5-script.js](./5-script.js)

### 6. Change the text
A JavaScript script that updates the text of the `<header>` element to `New Header!!!` when the user clicks on `DIV#update_header`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API

File: [6-script.js](./6-script.js)

### 7. Star wars character
A JavaScript script that fetches the character `name` from this URL: `https://swapi-api.alx-tools.com/api/people/5/?format=json`
* The name must be displayed in the HTML tag `DIV#character`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API

File: [7-script.js](./7-script.js)

### 8. Star Wars movies
A JavaScript script that fetches and lists the `title` for all movies by using this URL: `https://swapi-api.alx-tools.com/api/films/?format=json`
* All movie titles must be list in the HTML tag `UL#list_movies`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API

File: [8-script.js](./8-script.js)

### 9. Say Hello!
A JavaScript script that fetches from `https://fourtonfish.com/hellosalut/?lang=fr` and displays the value of `hello` from that fetch in the HTML tag `DIV#hello`.
* The translation of “hello” must be displayed in the HTML tag `DIV#hello`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API
* Your script must work when it is imported from the `<head>` tag

File: [9-script.js](./9-script.js)

### 10. No jQuery - document loaded
A JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`):
* You must use `document.querySelector` to select the HTML tag
* You can’t use the jQuery API
* Note: Your script must be imported from the `<head>` tag, not at the end of the HTML

File: [100-script.js](./100-script.js)

### 11. List, add, remove
A JavaScript script that adds, removes and clears `LI` elements from a list when the user clicks:
* The new element must be: `<li>Item</li>`
* The new element must be added to `UL.my_list`
* When the user clicks on `DIV#add_item`: a new element is added to the list
* When the user clicks on `DIV#remove_item`: the last element is removed from the list
* When the user clicks on `DIV#clear_list`: all elements of the list are removed
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API
* You script must work when it imported from the `HEAD` tag

File: [101-script.js](./101-script.js)

### 12. Say hello to everybody!
A JavaScript script that fetches and prints how to say “Hello” depending on the language
* You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
* The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
* The translation must be fetched when the user clicks on `INPUT#btn_translate`
* The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API
* You script must work when imported from the `<head>` tag

File: [102-script.js](./102-script.js)

### 13. And press ENTER
A JavaScript script that fetches and prints how to say “Hello” depending on the language
* You should use this API service: `https://www.fourtonfish.com/hellosalut/hello/`
* The language code will be the value entered in the tag `INPUT#language_code` (ex: `es`, `fr`, `en` etc.)
* The translation must be fetched when the user clicks on `INPUT#btn_translate` OR presses `ENTER` when the focus is on `INPUT#language_code`
* The translation of “Hello” must be displayed in the HTML tag `DIV#hello`
* You can’t use `document.querySelector` to select the HTML tag
* You must use the JQuery API
* You script must work when imported from the `<head>` tag

File: [103-script.js](./103-script.js)
