import feedparser

contacts = {}


def read_rss_feed(url):
    feed = feedparser.parse(url)
    updates = []

    for entry in feed.entries:
        title = entry.title
        link = entry.link
        updates.append(f"Title: {title}\nLink: {link}")

    return updates


def input_error(func):
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError):
            return "Input error. Please try again."

    return handler


@input_error
def add_contact(command):
    _, name, phone = command.split()
    contacts[name] = phone
    return f"Contact '{name}' with phone number '{phone}' has been added."


@input_error
def change_phone(command):
    _, name, new_phone = command.split()
    if name in contacts:
        contacts[name] = new_phone
        return f"Phone number for contact '{name}' has been updated to '{new_phone}'."
    else:
        return f"Contact '{name}' not found."


@input_error
def show_phone(command):
    _, name = command.split()
    if name in contacts:
        return f"The phone number for '{name}' is '{contacts[name]}'."
    else:
        return f"Contact '{name}' not found."


def show_all_contacts():
    if contacts:
        result = "Contacts:\n"
        for name, phone in contacts.items():
            result += f"{name}: {phone}\n"
        return result.strip()
    else:
        return "No contacts found."


def main():
    print("Bot assistant. Type 'exit' to exit.")
    print("And a team for conals(read rss)")
    print("Bot assistant. Can read channels RSS")
    print(
        """Channel list.
http://feeds.bbci.co.uk/news/world/rss.xml
http://edition.cnn.com/services/rss/
https://www.reuters.com/tools/rss
http://feeds.feedburner.com/TechCrunch/
https://www.nationalgeographic.com/science/index.rss
https://www.reddit.com/r/worldnews/.rss"""
    )

    while True:
        command = input("Enter a command: ").lower()

        if command == "exit" or command == "good bye" or command == "close":
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command.startswith("add"):
            print(add_contact(command))
        elif command.startswith("change"):
            print(change_phone(command))
        elif command.startswith("phone"):
            print(show_phone(command))
        elif command == "show all":
            print(show_all_contacts())
        elif command == "read rss":
            rss_url = input("Enter the RSS feed URL: ")
            updates = read_rss_feed(rss_url)
            for update in updates:
                print(update)
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
