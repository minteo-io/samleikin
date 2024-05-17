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


### Staging environment


### Production environment

