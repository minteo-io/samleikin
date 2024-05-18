# Samleikin Setup Guide

This document provides technical instructions for the installation and configuration of `Samleikin`.

A repository containing relevant information from [Klintra](https://www.klintra.fo) is available at [https://bitbucket.org/klintra-ft/sp-demo/src/master/](https://bitbucket.org/klintra-ft/sp-demo/src/master/).

## Prerequisites
- A signed agreement with [Talgildu Føroyar](https://www.samleikin.fo).
- A PKCS#12 bundle obtained from [Elektron](https://elektron.fo).
- An operational and internet-accessible [Keycloak 24](https://www.keycloak.org) instance.

## Required Tools
- [Keystore Explorer](https://keystore-explorer.org)

## Setup Instructions
Extract the private key and certificate(s) from the PKCS#12 bundle into separate files using `Keystore Explorer`.

## Keycloak 24 configuration

### Realm settings

1. Realm settings -> General -> Unmanaged Attributes: `Enabled`
2. Realm settings -> Keys -> Add providers -> Delete all providers of provider type: `rsa-generated`, `rsa-enc-generated`, `rsa` and `rsa-enc` if they exist
3. Realm settings -> Keys -> Add providers -> Add provider -> `rsa` -> Drag your private key file to `Private RSA Key` and the certificates file to `X509 Certificate` -> Save
4. Realm settings -> Keys -> Add providers -> Add provider -> `rsa-enc` -> Drag your private key file to `Private RSA Key` and the certificates file to `X509 Certificate` -> Save
5. Realm settings -> User profile -> `email` -> Required field: `Off`
6. Realm settings -> User profile -> `firstName` -> Required field: `Off`
7. Realm settings -> User profile -> `lastName` -> Required field: `Off`

### Authentication

1. Authentication -> Flows -> Create flow
2. Name: `create user`
3. Flow type: `Basic flow`
4. Create
5. Add execution -> `Create user if unique` -> Add
6. `Create user if unique` -> Requirement: `Alternative`

### Identity providers

#### General settings
1. Identity providers -> Add provider -> SAML v2.0
2. Alias: `samleikin`
3. Display name: `Samleikin`
4. Service provider entity ID: `https://[KEYCLOAK_URL]/realms/samleikin`
#### SAML settings
##### Staging environment
> 5. Identity provider entity ID: `https://innrita.staging.samleiki.fo/idp/shibboleth`
> 6. Single Sign-On service URL: `https://innrita.staging.samleiki.fo/idp/profile/SAML2/Redirect/SSO`
> 7. Single logout service URL: `https://innrita.staging.samleiki.fo/idp/profile/SAML2/Redirect/SLO`
##### Production environment
> 5. Identity provider entity ID: `https://innrita.samleiki.fo/idp/shibboleth`
> 6. Single Sign-On service URL: `https://innrita.samleiki.fo/idp/profile/SAML2/Redirect/SSO`
> 7. Single logout service URL: `https://innrita.samleiki.fo/idp/profile/SAML2/Redirect/SLO`
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
26. Validating X509 certificates: `[SAMLEIKIN_SIGNING_CERT]`
27. Sign service provider metadata: `Off`
28. Pass subject: `Off`
29. Allowed clock skew: `180` 
30. Attribute Consuming Service Index: `0`
#### Requested AuthnContext Constraints
31. Comparison: `exact`
#### Advanced settings
32. Store tokens: `Off`
33. Stored tokens readable: `Off`
34. Trust Email: `Off`
35. Account linking only: `Off`
36. Hide on login page: `Off`
37. First login flow override: `create user` 
38. Post login flow: `None`
39. Sync mode: `Force
40. Add/Save

### Mappers

1. Identity providers -> Samleikin -> Mappers -> Add mapper
2. Name: `givenName`
3. Sync mode override: `Inherit`
4. Mapper type: `Attribute importer`
5. Attribute Name: `urn:oid:2.5.4.42`
6. Friendly Name: `givenName`
7. Name Format: `ATTRIBUTE_FORMAT_URI`
8. User Attribute Name: `firstName`

Repeat adding mappers for:

#### sn

    Name: sn
    Attribute Name: urn:oid:2.5.4.4
    Friendly Name: sn
    User Attribute Name: lastName

#### displayName

    Name: displayName
    Attribute Name: urn:oid:2.16.840.1.113730.3.1.241
    Friendly Name: displayName
    User Attribute Name: displayName (Custom Attribute...)

#### countryOfCitizenship

    Name: countryOfCitizenship
    Attribute Name: urn:oid:1.3.6.1.5.5.7.9.4
    Friendly Name: countryOfCitizenship
    User Attribute Name: countryOfCitizenship (Custom Attribute...)

#### dateOfBirth

    Name: dateOfBirth
    Attribute Name: urn:oid:1.3.6.1.5.5.7.9.1
    Friendly Name: dateOfBirth
    User Attribute Name: dateOfBirth (Custom Attribute...)

#### displayName

    Name: personalIdentityNumber
    Attribute Name: urn:oid:1.2.208.189.1.2.1
    Friendly Name: personalIdentityNumber
    User Attribute Name: personalIdentityNumber (Custom Attribute...)

## Metadata to Samleikin

You must provide a metadata XML file to Samleikin. 

Locate this file by navigating to: Identity providers -> Samleikin -> `SAML 2.0 Service Provider Metadata`
