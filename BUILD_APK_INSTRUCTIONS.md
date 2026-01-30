Build APK — Local (WSL) and GitHub Actions

Overview
- This project is prepared to build an Android APK using Buildozer (python-for-android).
- CI workflow is added at `.github/workflows/build_apk.yml` to build on Ubuntu (GitHub Actions).

Option A — Build via GitHub Actions (recommended & fastest from Windows)
1. Push your branch (e.g., `main`) to GitHub. The workflow will run automatically for pushes to `main` or can be triggered manually.

2. (Optional) To produce a signed release APK, create these repository secrets (Settings → Secrets → Actions):
   - `ANDROID_KEYSTORE`: base64 of your JKS keystore file (use scripts/make_keystore.* to create)
   - `ANDROID_KEY_ALIAS`: alias used when creating the keystore
   - `ANDROID_KEY_PASSWORD`: keystore password (the script uses `changeit` by default)

3. After the workflow finishes, download the artifact `taj-al-itqan-apk` from the workflow run.

Option B — Build locally using WSL (Ubuntu)
1. Install WSL and an Ubuntu distribution (if not yet):

```powershell
wsl --install -d Ubuntu
```

2. Open WSL (Ubuntu) and prepare the environment:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv git openjdk-17-jdk zip unzip build-essential zlib1g-dev libssl-dev libffi-dev liblzma-dev libjpeg-dev libsdl2-dev

python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install cython
pip install buildozer
```

3. From the project folder (mounted under `/mnt/d/Taj Al-Itqan`), run:

```bash
# optional: edit buildozer.spec if needed
buildozer -v android debug
```

4. The generated APK will be in `bin/`.

Notes & Troubleshooting
- If the build fails due to missing NDK/SDK, buildozer will attempt to download them; ensure the runner has sufficient disk space (~10+ GB).
- If `p4a.branch` causes issues, we set it to `master` in `buildozer.spec`.
- Ensure `source.include_exts` includes `ttf` so bundled fonts are packaged (already configured).
- On Android 11+, `WRITE_EXTERNAL_STORAGE` is constrained. The app now uses `user_data_dir` for DB and cards to avoid needing broad storage permissions.

Scripts
- `scripts/make_keystore.sh` — create JKS keystore and print base64 (Linux/macOS)
- `scripts/make_keystore.ps1` — create JKS keystore and print base64 (Windows PowerShell)

If you want, I can:
- Push these changes to GitHub (needs your credentials or you can run the git commands locally),
- Or trigger a local WSL build now if you permit me to run commands in your terminal.
