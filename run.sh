set -e
podman build -t wallet-test .
podman run -it --rm -e REPO_URI="sqlite://:memory:", wallet-test python test_askar.py
