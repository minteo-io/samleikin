# SAML Utils

## Decrypt SAML Assertions

### Prerequisites
1. Ensure Python is installed on your system.
2. Save your key in PEM format as `key.pem`.
3. Save the SAML response XML (everything between `<saml2p:Response` and `</saml2p:Response>`) as `saml.xml`.

### Steps to Decrypt
1. Create a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

2. Install required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Execute the decryption script:
    ```sh
    python saml_assertion_decrypt.py
    ```

### Output
The decrypted SAML assertion will be saved in `saml_out.xml`.
