# importing the stuff i need
import argparse
import json
import random
import string

# this is the file where all the urls will be saved
FILE_NAME = "data.json"


def load_data():
    # this function opens the json file and gets the data
    # if file is not there yet then we just return empty dict
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error: data.json is damaged or not valid")
        return {}


def save_data(data):
    # this saves whatever dictionary we give it into the json file
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)


def check_url(url):
    # basic check, url should start with http or https
    if url.startswith("http://") or url.startswith("https://"):
        # check that something is written after http:// or https://
        if len(url.split("://", 1)[1].strip()) > 0:
            return True

    return False


def check_alias(alias):
    # checking if the custom alias is simple and valid
    if len(alias) == 0 or len(alias) > 30:
        return False

    for character in alias:
        if not (character.isalnum() or character == "-"):
            return False

    return True


def make_code(data):
    # this makes a random code of 6 letters/numbers
    letters = string.ascii_letters + string.digits

    while True:
        code = ""

        for i in range(6):
            code = code + random.choice(letters)

        # check if this code is already used
        if code not in data:
            return code


def shorten(url, alias):
    if not check_url(url):
        print("Error: url is not valid, it should start with http:// or https://")
        return

    data = load_data()

    # check if this url already has a code
    if alias is None:
        for code in data:
            if data[code]["url"] == url:
                print("This url is already shortened, code is:", code)
                return

    if alias is not None:
        # check if the alias is valid
        if not check_alias(alias):
            print("Error: alias can only contain letters, numbers and hyphens")
            return

        # user wants their own code
        if alias in data:
            print("Error: this alias is already used, try a different one")
            return

        code = alias

    else:
        code = make_code(data)

    # saving the new entry, clicks starts from 0
    data[code] = {"url": url, "clicks": 0}
    save_data(data)

    print("Done! your short code is:", code)


def resolve(code):
    data = load_data()

    if code not in data:
        print("Error: code not found")
        return

    # adding 1 to the click count every time someone resolves it
    data[code]["clicks"] = data[code]["clicks"] + 1
    save_data(data)

    print("Original url:", data[code]["url"])
    print("This code was clicked", data[code]["clicks"], "times")


def show_list():
    data = load_data()

    if not data:
        print("No urls saved yet")
        return

    print("CODE       CLICKS   URL")
    print("----------------------------------------")

    for code in data:
        print(f"{code:<10} {data[code]['clicks']:<8} {data[code]['url']}")


def delete_code(code):
    data = load_data()

    if code not in data:
        print("Error: code not found")
        return

    del data[code]
    save_data(data)

    print("code deleted:", code)


# setting up argparse so we can run commands from terminal
# added help text everywhere so "python main.py -h" tells you what to do
parser = argparse.ArgumentParser(
    description="A simple CLI url shortener. Use -h after any command to see more info."
)

subparsers = parser.add_subparsers(dest="command", help="available commands")


# shorten command
shorten_cmd = subparsers.add_parser(
    "shorten", help="shorten a long url and get a short code back"
)

shorten_cmd.add_argument(
    "url", help="the long url you want to shorten, must start with http:// or https://"
)

shorten_cmd.add_argument(
    "--alias", default=None, help="use your own custom code instead of a random one"
)


# resolve command
resolve_cmd = subparsers.add_parser(
    "resolve", help="get the original url back from a short code"
)

resolve_cmd.add_argument("code", help="the short code you want to look up")


# delete command
delete_cmd = subparsers.add_parser("delete", help="delete a short code from storage")

delete_cmd.add_argument("code", help="the short code you want to delete")


# list command
list_cmd = subparsers.add_parser(
    "list", help="show all the urls saved so far with their click count"
)


args = parser.parse_args()


# checking which command was typed and calling the right function
if args.command == "shorten":
    shorten(args.url, args.alias)

elif args.command == "resolve":
    resolve(args.code)

elif args.command == "list":
    show_list()

elif args.command == "delete":
    delete_code(args.code)

else:
    # if no command given, just show a short list of what can be used
    print("Please enter a valid command. Available commands are:")
    print("  shorten <url>      - shorten a long url")
    print("  resolve <code>     - get the original url from a code")
    print("  list                - show all saved urls")
    print("  delete <code>      - delete a saved code")
    print("Run 'python main.py -h' to see more details")
