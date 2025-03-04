---

# Caesar Cipher Encryption

This repository contains a simple Python implementation of the Caesar Cipher, a basic encryption technique where each letter in a given text is shifted by a fixed number of positions in the alphabet.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [License](#license)

## Introduction

The Caesar Cipher is a basic method of encryption where each letter in a message is moved forward or backward by a set number of places in the alphabet. This technique, named after Julius Caesar, was used to keep messages secret.

For example, if the shift is 3:

A → D

B → E

C → F

To decrypt the message, you simply shift the letters back by the same amount. The Caesar Cipher is a simple yet effective way to understand the basics of encryption and cryptography.



This Python script allows you to both encrypt and decrypt messages using the Caesar Cipher.

## Features

- **Encryption**: Convert plaintext to ciphertext by shifting letters by a specified number.
- **Decryption**: Revert ciphertext to plaintext by shifting letters back by the same number.
- **Custom Shift**: Choose any integer as the shift value.
- **Handles Upper and Lowercase Letters**: The cipher respects the case of the letters.
- **Ignores Non-alphabet Characters**: Numbers, spaces, and symbols are not altered.

## Installation

To use this project, clone the repository to your local machine:

```bash
git clone https://github.com/hf3cyber/PRODIGY_CS_01.git
cd PRODIGY_CS_01
```

Make sure you have Python installed. This script requires Python 3.

## Usage

To run the script, use the following command:

```bash
python CaesarCipher.py
```

### Encrypt a Message

To encrypt a message, you will be prompted to enter the text and the shift value.

### Decrypt a Message

Similarly, to decrypt a message, enter the encrypted text and use the same shift value used for encryption.

Here's a version that emphasizes readability with a focus on the outputs:

---

## Examples

### Example 1: Basic Encryption and Decryption

```python
text = "Hello, World!"
shift = 3
```

- **Encrypted Text**: `Khoor, Zruog!`
- **Decrypted Text**: `Hello, World!`

---


### Example 2: Handling Numbers and Symbols

```python
text = "This is 2025!"
shift = 5
```

- **Encrypted Text**: `Ymnx nx 2025!`
- **Decrypted Text**: `This is 2025!`

---

### Example 3: Negative Shift

```python
text = "Negative Shift"
shift = -4
```

- **Encrypted Text**: `Jwcwpreb Odepq`
- **Decrypted Text**: `Negative Shift`

---

---

These examples provide a clear and concise view of what the Caesar Cipher code does, making it easy for readers to understand the input and the corresponding output.
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
