# Secret Santa with Forbidden Pairs 🎅🎁

A Python script to organize a Secret Santa event among participants, ensuring:
1. **No participant is assigned to themselves.**
2. **No mutual Santa-Child assignments.**
3. **No forbidden pairs** (some participants should never be assigned to each other).

Additionally, the script generates personalized WhatsApp-ready messages with instructions and addresses.

---

## Features 🌟

- **Simple Setup**: Provide `participants.csv` with columns `Name`, `Address`, `Phone`, and `Preferences`.
- **Forbidden Pairs**: A second CSV (`forbidden_pairs.csv`) lists pairs that should never be matched.
- **One-Ring Constraint**: Ensures each participant has exactly one Santa and one Child.
- **Personalized Messages**: A fun, casual template for WhatsApp messages, saved to a text file.

---
## Project Structure 📂

```plaintext
secret-santa-forbidden/
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
   git clone https://github.com/<YourUsername>/secret-santa-forbidden.git
   cd secret-santa-forbidden
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

## Contributing 🤝

1. Fork the repository.
2. Create a new feature branch.
3. Commit and push changes to your branch.
4. Open a Pull Request with a detailed description.

---

## License 📜

This project is licensed under the [MIT License](./LICENSE).

Enjoy organizing your Secret Santa event! 🎄✨
