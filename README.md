
# Homomorphic Encryption using TenSEAL

This project demonstrates how to utilize homomorphic encryption with the TenSEAL library. It includes functionalities to encrypt, process, and decrypt sensitive data while maintaining privacy and security.

## Features

- **Encryption**: Encrypt sensitive data, such as salaries and bonuses, using the CKKS encryption scheme provided by TenSEAL.
- **Data Processing**: Perform operations on encrypted data, such as adding bonuses to salaries, without revealing the underlying plaintext values.
- **Decryption**: Decrypt the processed data to obtain the final results while preserving privacy.
- **File Handling**: Read data from JSON files, process it, and write the results back to JSON files.

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies:
  'pip install -r requirments.txt'

3. Ensure you have the necessary keys for encryption and decryption. Generate the keys using the appropriate scripts provided in the `keys` directory.

## Usage
1. **Create Dataset**:
- Run `Dataset.py` Create a random dataset for test.
- Output: `employee_dataset.json` (Test Dataset)

2. **Create Private and Public keys**:
- Run `Generate_Key.py` to encrypt salary data and add bonuses to the encrypted values.
- Output: /keys (private and public keys)

3. **Encrypt Data**:
- Run `encrypt_data.py` to encrypt salary data and add bonuses to the encrypted values.
- Input: `employee_dataset.json` (containing employee data)
- Output: `updated_encrypted_json.json` (encrypted data with bonuses)

3. **Addition on Encrypt Data**:
- Run `Add_Bonus.py` to encrypt salary data and add bonuses to the encrypted values.
- Input: `updated_encrypted_json.json` (encrypted data with bonuses)
- Output: `updated_encrypted_json_final.json` (encripted data with final salaries)

3. **Decrypt Data**:
- Run `Decript_Dataset.py` to decrypt the processed data and obtain the final salary values.
- Input: `updated_encrypted_json_final.json` (encripted data with final salaries)
- Output: `output_json.json` (decrypted data with final salaries)





## Dependencies

- [TenSEAL](https://github.com/OpenMined/TenSEAL): A library for doing homomorphic encryption operations.


