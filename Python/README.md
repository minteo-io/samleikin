# SAML Utils

## Decrypt SAML assertions
* Make sure that python is installed
* Save key in PEM format to `key.pem`
* Save SAML response XML (everything between  `<saml2p:Response` and `</saml2p:Response>`) to `saml.xml`

```sh
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

python saml_assertion_decrypt.py
```

The decrypted result will be in `saml_out.xml`
