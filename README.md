# Samleikin

This guide will help you get up and running with `Samleikin`.

## Preconditions
- Signed agreement with [Talgildu Føroyar](https://www.samleikin.fo)
- Received PKCS#12 bundle from [Elektron](https://elektron.fo)
- [Keycloak 24](https://www.keycloak.org) up and running and accessible from the internet

## Tools
[Keystore Explorer](https://keystore-explorer.org)

## Setup
You should start by extracting the private key and certificate(s) from the PKCS#12 to separate files. This can be done using `Keystore Explorer`.

## Keycloak 24 configuration

### Realm settings

1. Realm settings -> General -> Unmanaged Attributes: `Enabled`
2. Realm settings -> Keys -> Add providers -> Delete all providers of provider type: `rsa-generated`, `rsa-enc-generated`, `rsa` and `rsa-enc` if they exist
3. Realm settings -> Keys -> Add providers -> Add provider -> `rsa` -> Drag your private key file to `Private RSA Key` and the certificates file to `X509 Certificate` -> Save
4. Realm settings -> Keys -> Add providers -> Add provider -> `rsa-enc` -> Drag your private key file to `Private RSA Key` and the certificates file to `X509 Certificate` -> Save
5. Realm settings -> User profile -> `email` -> Required field: `Off`
6. Realm settings -> User profile -> `firstName` -> Required field: `Off`
7. Realm settings -> User profile -> `lastName` -> Required field: `Off`

### Identity providers

1. Identity providers -> Add provider -> SAML v2.0
2. Alias: `samleikin`
3. Display name: `Samleikin`
4. Service provider entity ID: `https://[KEYCLOAK_URL]/realms/samleikin`
5. Identity provider entity ID: `https://innrita.staging.samleiki.fo/idp/shibboleth`
6. Single Sign-On service URL: `https://innrita.staging.samleiki.fo/idp/profile/SAML2/Redirect/SSO`
7. Single logout service URL: `https://innrita.staging.samleiki.fo/idp/profile/SAML2/Redirect/SLO`
8. Backchannel logout: `Off`
9. Send 'id_token_hint' in logout requests: `On`
10. Send 'client_id' in logout requests: `Off`
11. NameID policy format: `Persistent`
12. Principal type: `Subject NameID`
13. Allow create: `On`
14. HTTP-POST binding response: `On`
15. HTTP-POST binding for AuthnRequest: `Off`
16. HTTP-POST binding logout: `Off`
17. Want AuthnRequests signed: `On`
18. Signature algorithm: `RSA_SHA256`
19. SAML signature key name: `KEY_ID`
20. Want Assertions signed: `On`
21. Want Assertions encrypted: `On`
22. Encryption Algorithm: `RSA-OAEP`
23. Force authentication: `Off`
24. Validate Signatures: `On`
25. Use metadata descriptor URL: `Off`
26. Use metadata descriptor URL: `[SAMLEIKIN_SIGNING_CERT]`

### Staging environment


### Production environment

