# PowerShell script to create keystore and output base64
param(
  [string]$Alias = "mykey"
)

$keystore = "taj_keystore.jks"
$keytool = "keytool"

& $keytool -genkeypair -v -keystore $keystore -storetype JKS -keyalg RSA -keysize 2048 -validity 10000 -alias $Alias -storepass changeit -keypass changeit -dname "CN=TAJ, OU=Dev, O=MyOrg, L=City, ST=State, C=SA"

Write-Host "Keystore created: $keystore"
Write-Host "Base64 (copy this into GitHub secret ANDROID_KEYSTORE):"
[Convert]::ToBase64String([IO.File]::ReadAllBytes($keystore))
Write-Host "Alias: $Alias"
Write-Host "Password: changeit"
