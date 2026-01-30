#!/bin/bash
# Generate a keystore and output it base64-encoded for GitHub Secrets
# Usage: ./make_keystore.sh myalias

ALIAS=${1:-mykey}
KEYSTORE_FILE=taj_keystore.jks

keytool -genkeypair -v -keystore "$KEYSTORE_FILE" -storetype JKS \
  -keyalg RSA -keysize 2048 -validity 10000 \
  -alias "$ALIAS" -storepass changeit -keypass changeit \
  -dname "CN=TAJ, OU=Dev, O=MyOrg, L=City, ST=State, C=SA"

echo
echo "Keystore created: $KEYSTORE_FILE"
echo "Base64 (copy this into GitHub secret ANDROID_KEYSTORE):"
base64 "$KEYSTORE_FILE" | tr -d '\n'

echo
echo "Alias: $ALIAS"
echo "Password: changeit"
