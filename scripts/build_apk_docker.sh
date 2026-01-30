#!/usr/bin/env bash
# Simple helper to build the Android debug APK locally using Docker
set -euo pipefail
REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"

docker image inspect kivy/buildozer:latest >/dev/null 2>&1 || docker pull kivy/buildozer:latest

echo "Running buildozer (docker)..."
docker run --rm -v "$REPO_ROOT":/home/user/hostcwd -w /home/user/hostcwd kivy/buildozer:latest buildozer android debug

echo "Done. Find APK in $REPO_ROOT/bin/"
