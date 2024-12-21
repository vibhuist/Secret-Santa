import pandas as pd
import random
import sys

def read_csv(file_path):
    """
    Reads and validates the participants CSV.
    """
    data = pd.read_csv(file_path)
    required_columns = {'Name', 'Address', 'Phone', 'Preferences'}
    if not required_columns.issubset(data.columns):
        raise ValueError(
            f"CSV must contain columns: {required_columns}. "
            f"Found: {data.columns.tolist()}"
        )

    if data.isnull().any().any():
        raise ValueError("Some participants have incomplete information. Check the CSV.")

    if data['Name'].duplicated().any():
        raise ValueError("Duplicate names found. Ensure all participant names are unique.")

    if (data['Address'].str.len() < 10).any():
        raise ValueError("Some addresses appear incomplete. Please verify addresses.")

    if len(data) < 2:
        raise ValueError("At least two participants are required.")

    return data

def read_forbidden_pairs(file_path):
    """
    Reads forbidden pairs from a CSV file (e.g., Name_A, Name_B columns).
    Returns a set of tuples (santa, child) that are disallowed.
    If the CSV is empty, returns an empty set.
    """
    forbidden_df = pd.read_csv(file_path)
    
    # If the file is empty or has no rows, return an empty set
    if forbidden_df.empty:
        return set()

    required_columns = {'Name_A', 'Name_B'}
    if not required_columns.issubset(forbidden_df.columns):
        raise ValueError(
            f"Forbidden pairs CSV must contain columns: {required_columns}. "
            f"Found: {forbidden_df.columns.tolist()}"
        )

    forbidden_pairs = set()
    for _, row in forbidden_df.iterrows():
        name_a, name_b = row['Name_A'], row['Name_B']
        # Store both directions
        forbidden_pairs.add((name_a, name_b))
        forbidden_pairs.add((name_b, name_a))

    return forbidden_pairs

def create_secret_santa_ring(participants, forbidden_pairs, max_retries=1000):
    """
    Creates a Secret Santa ring that respects forbidden pair constraints.
    No one is their own Santa, no 2-person loops, and no forbidden pairs.
    """
    names = participants['Name'].tolist()

    for _ in range(max_retries):
        shuffled = names[:]
        random.shuffle(shuffled)
        
        if all(
            shuffled[i] != names[i] and
            shuffled[i] != names[(i + 1) % len(names)] and
            (names[i], shuffled[i]) not in forbidden_pairs
            for i in range(len(names))
        ):
            return [(names[i], shuffled[i]) for i in range(len(names))]

    raise ValueError("Unable to create a valid Secret Santa ring after multiple attempts.")

def log_pairs(santa_pairs, output_file="logs/santa_pairs_log.txt"):
    """
    Logs the final (Santa, Child) pairs for reference.
    """
    with open(output_file, 'w') as log_file:
        for santa, child in santa_pairs:
            log_file.write(f"Santa: {santa}, Child: {child}\n")
    print(f"Santa pairs logged in {output_file}")

def generate_message(santa, child_details):
    """
    Generates a casual, friendly Secret Santa message.
    """
    return (
        f"🎅🎁 Hey hey, Santa *{santa['Name']}*! You've got a Child! 🎄\n\n"
        f"📚 *Your Child’s book preference*: {child_details['Preferences']}\n\n"
        f"Here’s everything you need to know about your Child:\n"
        f"👤 *Name*: {child_details['Name']}\n"
        f"📞 *Phone*: {child_details['Phone']}\n"
        f"🏠 *Address*: {child_details['Address']}\n\n"
        f"⏰ *Important*: Please send the book(s) by *22nd December*! 📦\n"
        f"📸 Once sent, share the speed post receipt and tracking number with *Vibhu*.\n"
        f"🤔 Not sure if you can do this? Let *Vibhu* know ASAP!\n\n"
        f"✨ *Some tips to make it awesome*:\n"
        f"1️⃣ Keep your name as Santa and address *Anonymous*! 😎\n"
        f"2️⃣ Don’t spill the beans about your Child to other Santas. 🤐\n"
        f"3️⃣ Don’t reach out to your Child before sending their gift. 📵\n"
        f"4️⃣ Wrap the book if you can—it’s always more fun to unwrap! 🎀\n"
        f"5️⃣ One book under ₹400 is perfect, but if you’re feeling generous, go for more! 💝\n\n"
        f"🎉 Have fun and make your Child’s day special! 🌟\n"
        f"Keep it magical! ✨ Merry Christmas and happy gifting! 🎅🎄"
    )

def save_messages(participants, santa_pairs, output_file="secret_santa_messages.txt"):
    """
    Saves all Santa messages into a text file for easy distribution.
    """
    messages = []
    for santa, child_name in santa_pairs:
        santa_details = participants[participants['Name'] == santa].iloc[0]
        child_details = participants[participants['Name'] == child_name].iloc[0]
        messages.append(generate_message(santa_details, child_details))
    with open(output_file, 'w', encoding='utf-8') as file:
        for message in messages:
            file.write(message + "\n\n")
    print(f"Messages saved to {output_file}")

def main():
    input_file = "data/participants.csv"
    forbidden_file = "data/forbidden_pairs.csv"
    output_file = "secret_santa_messages.txt"
    pairs_log_file = "logs/santa_pairs_log.txt"

    try:
        participants = read_csv(input_file)
        forbidden_pairs = read_forbidden_pairs(forbidden_file)
        santa_pairs = create_secret_santa_ring(participants, forbidden_pairs)
        log_pairs(santa_pairs, pairs_log_file)
        save_messages(participants, santa_pairs, output_file)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
