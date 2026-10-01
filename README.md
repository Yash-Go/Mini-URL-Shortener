# 🔗 Mini URL Shortener

A simple **Command-Line Interface (CLI) URL Shortener** built using Python.

This project allows users to create short codes for long URLs, retrieve the original URLs using those codes, view all saved URLs, track the number of times a short code is resolved, and delete saved short links.

The project uses a **JSON file for data persistence**, so saved URLs remain available even after the program is closed.

---

## 📌 Features

- 🔗 Shorten long URLs
- 🎲 Automatically generate a random 6-character short code
- ✏️ Create a custom alias for a URL
- 🔍 Resolve a short code back to the original URL
- 📊 Track the number of times each short code is resolved
- 📋 Display all saved URLs and their click counts
- 🗑️ Delete a saved short code
- 💾 Store data permanently using a JSON file
- ⚠️ Handle invalid URLs and invalid aliases
- 🆘 Built-in command-line help using `argparse`

---

## 🛠️ Technologies Used

- **Python 3**
- **JSON** — for storing URL data
- **argparse** — for handling command-line arguments
- **random** — for generating random short codes
- **string** — for providing letters and digits

No external APIs or third-party libraries are required.

---

## 📁 Project Structure

```text
Mini-URL-Shortener/
│
├── main.py
├── data.json
└── README.md
```

### `main.py`

Contains the complete Python program and all URL-shortening functionality.

### `data.json`

Stores all shortened URLs, their short codes, and click counts.

This file is automatically created when the first URL is saved.

### `README.md`

Contains the documentation and instructions for using the project.

---

# 🚀 Getting Started

## 1. Requirements

Make sure Python 3 is installed on your computer.

Check your Python version using:

```bash
python --version
```

or:

```bash
python3 --version
```

---

## 2. Open the Project

Open a terminal in the project folder.

For example:

```bash
cd Mini-URL-Shortener
```

---

## 3. Run the Program

The program is run using:

```bash
python main.py
```

The available commands are:

```bash
python main.py shorten <url>
python main.py resolve <code>
python main.py list
python main.py delete <code>
```

---

# 📖 Usage

## 1. Shorten a URL

To shorten a URL, use:

```bash
python main.py shorten https://google.com
```

The program will generate a random 6-character code.

Example:

```text
Done! your short code is: aB72xK
```

---

## 2. Use a Custom Alias

You can choose your own short code instead of using a randomly generated one.

Use the `--alias` option:

```bash
python main.py shorten https://google.com --alias google
```

Output:

```text
Done! your short code is: google
```

The custom alias:

- Must not be empty
- Must contain 30 characters or fewer
- Can contain letters
- Can contain numbers
- Can contain hyphens (`-`)
- Must not already exist

### Example of a valid alias

```text
google-123
```

### Examples of invalid aliases

```text
google.com
google_123
google@123
```

---

# 🔍 Resolve a Short Code

To retrieve the original URL, use:

```bash
python main.py resolve aB72xK
```

Example output:

```text
Original url: https://google.com
This code was clicked 1 times
```

Every time a code is successfully resolved, its click count increases by `1`.

The updated click count is saved in `data.json`.

---

# 📋 List All Saved URLs

To view all saved URLs, use:

```bash
python main.py list
```

Example output:

```text
CODE       CLICKS   URL
----------------------------------------
aB72xK     3        https://google.com
yt82Lp     1        https://youtube.com
github1    5        https://github.com
```

The list displays:

- Short code
- Number of clicks
- Original URL

---

# 🗑️ Delete a Short Code

To delete a saved URL, use:

```bash
python main.py delete aB72xK
```

Example output:

```text
code deleted: aB72xK
```

The URL is removed from `data.json`.

If the code does not exist:

```text
Error: code not found
```

---

# 🆘 Command-Line Help

The project uses Python's `argparse` module to provide command-line help.

To see all available commands:

```bash
python main.py -h
```

You can also get help for a specific command:

```bash
python main.py shorten -h
python main.py resolve -h
python main.py delete -h
```

---

# 💾 Data Storage

The project stores all information in:

```text
data.json
```

An example of the stored data is:

```json
{
    "aB72xK": {
        "url": "https://google.com",
        "clicks": 3
    },
    "yt82Lp": {
        "url": "https://youtube.com",
        "clicks": 1
    }
}
```

The short code is used as the **key** in the JSON data.

Each short code stores:

```text
URL
Click count
```

For example:

```text
aB72xK
   │
   ├── url → https://google.com
   │
   └── clicks → 3
```

---

# 🔄 How Data Persistence Works

The project uses two main functions.

### `load_data()`

Reads the existing information from `data.json`.

```text
data.json
    ↓
json.load()
    ↓
Python dictionary
```

### `save_data(data)`

Saves the Python dictionary back into `data.json`.

```text
Python dictionary
    ↓
json.dump()
    ↓
data.json
```

This allows the data to remain available even after the program is closed.

---

# 🧩 Main Functions

| Function | Purpose |
|---|---|
| `load_data()` | Loads saved URL data from `data.json` |
| `save_data(data)` | Saves URL data to `data.json` |
| `check_url(url)` | Performs basic URL validation |
| `check_alias(alias)` | Validates a custom alias |
| `make_code(data)` | Generates an unused random 6-character code |
| `shorten(url, alias)` | Creates a new shortened URL |
| `resolve(code)` | Retrieves the original URL and updates clicks |
| `show_list()` | Displays all saved URLs |
| `delete_code(code)` | Deletes a saved short code |

---

# 🧠 How the Program Works

The overall flow of the program is:

```text
                 User enters command
                         │
                         ▼
                    argparse
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
       shorten        resolve          list
          │              │
          │              │
          ▼              ▼
      load_data()    load_data()
          │              │
          ▼              ▼
      Validate       Find code
          │              │
          ▼              ▼
    Generate code   Increase clicks
          │              │
          ▼              ▼
      save_data()    save_data()
```

The `delete` command also loads the data, removes the selected code, and saves the updated dictionary.

---

# 🔐 URL Validation

The project performs a basic check to make sure the URL starts with:

```text
http://
```

or:

```text
https://
```

For example:

```text
https://google.com
```

is accepted.

While:

```text
google.com
```

is rejected.

This is a **basic validation**, not a complete check of whether a website actually exists.

---

# 🎲 Random Short Code Generation

When a custom alias is not provided, the program generates a random 6-character code.

The available characters are:

```text
a-z
A-Z
0-9
```

For example:

```text
aB72xK
P9kLm2
xT81Qa
```

Before accepting the generated code, the program checks whether it is already present in the stored data.

If the code already exists, another code is generated.

This prevents two stored URLs from having the same short code.

---

# ⚠️ Error Handling

The project handles several common errors.

### Missing `data.json`

If the file does not exist yet, the program starts with an empty dictionary:

```python
{}
```

### Invalid JSON

If `data.json` contains invalid JSON, the program displays:

```text
Error: data.json is damaged or not valid
```

### Invalid URL

For example:

```bash
python main.py shorten google.com
```

produces an error because the URL does not start with `http://` or `https://`.

### Invalid Alias

If an alias contains unsupported characters:

```bash
python main.py shorten https://google.com --alias google_123
```

the program rejects it.

### Code Not Found

Trying to resolve or delete a code that does not exist produces:

```text
Error: code not found
```

---

# 💻 Example Session

Here is an example of using the complete application.

### Step 1 — Shorten a URL

```bash
python main.py shorten https://google.com
```

Output:

```text
Done! your short code is: aB72xK
```

### Step 2 — Resolve the code

```bash
python main.py resolve aB72xK
```

Output:

```text
Original url: https://google.com
This code was clicked 1 times
```

### Step 3 — Resolve it again

```bash
python main.py resolve aB72xK
```

Output:

```text
Original url: https://google.com
This code was clicked 2 times
```

### Step 4 — View all URLs

```bash
python main.py list
```

Output:

```text
CODE       CLICKS   URL
----------------------------------------
aB72xK     2        https://google.com
```

### Step 5 — Delete the URL

```bash
python main.py delete aB72xK
```

Output:

```text
code deleted: aB72xK
```

---

# 📌 Design Decisions

## Why JSON?

JSON was chosen because:

- It is simple to understand
- Python has built-in JSON support
- It is easy to read manually
- It allows data to persist between program runs
- No database setup is required

## Why `argparse`?

`argparse` provides a clean way to create CLI commands and automatically generates useful help messages.

## Why random codes?

Random codes allow the program to automatically create short identifiers without requiring the user to choose one.

## Why check for duplicate URLs?

If a URL has already been shortened, the program returns the existing short code instead of creating another unnecessary entry.

---

# 📈 Possible Future Improvements

The current project provides the core URL-shortening functionality. Some possible improvements are:

- Add URL expiration dates
- Add a command to update an existing URL
- Add more detailed statistics
- Add timestamps for when URLs were created
- Improve URL validation
- Allow users to search stored URLs
- Add import/export functionality
- Replace JSON storage with SQLite or another database
- Create a web interface using Flask
- Add a REST API
- Add password-protected or private links

These can be added later as the project becomes more advanced.

---

# 🎯 Learning Outcomes

This project helped practice several important Python concepts:

- Functions
- Dictionaries
- Nested dictionaries
- Loops
- Conditional statements
- String operations
- File handling
- JSON
- Exception handling
- Command-line arguments
- Random value generation
- Data persistence
- Basic project structure

It also demonstrates how multiple Python concepts can be combined to create a complete working application.


