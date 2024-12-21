# Secret Santa with Forbidden Pairs 🎅🎁

### Background

This script is useful for organizing a Secret Santa campaign where each participant is assigned a Santa and a Child to gift a book to. The script ensures the following conditions:

1. **No participant is assigned to themselves.**
2. **No mutual Santa-Child assignments.** (two individuals are not each others Santa-Child respectively)
3. **No forbidden pairs** (some participants should never be assigned to each other).

> 💡 **Tip**: Forbidden pairs can be useful in scenarios where certain participants should not be assigned to each other, such as spouses, family members, or close friends. This ensures that the Secret Santa game remains fun and engaging, as both the Santa and the recipient are strangers to each other, adding an element of surprise and excitement.

4. **Ensures a single loop among participants.** (Each participant is part of a single continuous loop, ensuring everyone is both a Santa and a Child)

Additionally, all Santa-Child relationships are saved in `logs/santa_pairs_log.txt`, and the messages to be shared with Santas are stored in `secret_santa_messages.txt`.

---

## Features 🌟

- **Simple Setup**: Provide `participants.csv` with columns `Name`, `Address`, `Phone`, and `Preferences`.
- **Forbidden Pairs**: A second CSV (`forbidden_pairs.csv`) lists pairs that should never be matched.
- **One-Ring Constraint**: Ensures each participant has exactly one Santa and one Child.
- **Personalized Messages**: A fun, casual template for WhatsApp messages, saved to a text file.

---
## Project Structure 📂

```plaintext
secret-santa/
├── LICENSE                 # Project license (MIT by default)
├── README.md               # Documentation and usage instructions
├── requirements.txt        # Dependencies for the project
├── .gitignore              # Files and folders ignored by Git
├── src/
│   └── main.py             # Main Python script
├── data/
│   ├── participants.csv    # Input: List of participants
│   └── forbidden_pairs.csv # Input: Forbidden Santa-Child pairs
└── logs/
    └── .gitkeep            # Placeholder for logs (e.g., santa_pairs_log.txt)
```

## Getting Started 🚀

### Prerequisites

- **Python 3.8+** recommended
- `pip` for installing dependencies

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/vibhuist/Secret-Santa.git
   cd Secret-Santa
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   > *Tip*: Consider a Python virtual environment, e.g., `python -m venv venv && source venv/bin/activate` (Linux/macOS) or `.\venv\Scripts\activate` (Windows).

3. **Prepare your data**:
   - **`data/participants.csv`**: Contains participant info  
   - **`data/forbidden_pairs.csv`**: Contains pairs who should **not** match

---

## Usage 🛠️

1. **Run the script**:
   ```bash
   python src/main.py
   ```
2. **What happens**:
   - The script reads `data/participants.csv` and `data/forbidden_pairs.csv`.
   - Validates participant and forbidden pair data.
   - Creates a valid Secret Santa ring respecting forbidden pairs.
   - Logs pairings to `logs/santa_pairs_log.txt`.
   - Generates a text file `secret_santa_messages.txt` with personalized WhatsApp messages.

3. **Open `secret_santa_messages.txt`**:
   - Copy messages and send to each Santa in your group.

---

## Configuration ⚙️

- **File paths**: Modify these paths in `src/main.py` if needed:
  ```python
  input_file = "data/participants.csv"
  forbidden_file = "data/forbidden_pairs.csv"
  output_file = "secret_santa_messages.txt"
  pairs_log_file = "logs/santa_pairs_log.txt"
  ```
- **Max Retries**: The script tries up to 1000 shuffles to form a valid ring. You can adjust this in `create_secret_santa_ring()` if needed.

---

## Example 📄

### Participants (`data/participants.csv`)

```csv
Name,Address,Phone,Preferences
Alice,123 Candy Lane,5551234567,Fantasy Books
Bob,456 Broadway Ave,5559876543,Sci-Fi
Charlie,789 Maple St,5555555555,Horror
Diana,987 Pine St,5551112222,Romance
```

### Forbidden Pairs (`data/forbidden_pairs.csv`)

```csv
Name_A,Name_B
Alice,Bob
```

---
## Sample Pair Output 📄

After running the script, a sample output in `logs/santa_pairs_log.txt` might look like this:

```plaintext
Santa,Child
Alice,Charlie
Bob,Diana
Charlie,Bob
Diana,Alice
```
## Sample Output Message 📬

After running the script, a sample message in `secret_santa_messages.txt` might look like this:

```plaintext
🎅🎁 Hey hey, Santa *Alice*! You've got a Child! 🎄

📚 *Your Child has described their book preference as*: Horror

Here’s everything you need to know about your Child:
👤 *Name*: Charlie
📞 *Phone*: 5555555555
🏠 *Address*: 789 Maple St

⏰ *Important*: Please send the book(s) by *22nd December*! 📦
📸 Once sent, share the speed post receipt and tracking number with *Vibhu*.
🤔 Not sure if you can do this? Let *Vibhu* know ASAP!

✨ *Some tips to make it awesome*:
1️⃣ Keep your name as Santa and address *Anonymous*! 😎
2️⃣ Don’t spill the beans about your Child to other Santas. 🤐
3️⃣ Don’t reach out to your Child before sending their gift. 📵
4️⃣ Wrap the book if you can—it’s always more fun to unwrap! 🎀
5️⃣ One book under ₹400 is perfect, but if you’re feeling generous, go for more! 💝

🎉 Have fun and make your Child’s day special! 🌟
Keep it magical! ✨ Merry Christmas and happy gifting! 🎅🎄
```

---

## License 📜

This project is licensed under the [MIT License](./LICENSE).

Enjoy organizing your Secret Santa event! 🎄✨
