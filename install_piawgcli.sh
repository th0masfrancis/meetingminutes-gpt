#!/bin/bash

# Step 1: Install Go
GO_VERSION="1.17.5"
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

if [ "$ARCH" = "x86_64" ]; then
  ARCH="amd64"
elif [ "$ARCH" = "aarch64" ]; then
  ARCH="arm64"
else
  echo "Unsupported architecture. Exiting."
  exit 1
fi

GO_DOWNLOAD_URL="https://dl.google.com/go/go${GO_VERSION}.${OS}-${ARCH}.tar.gz"
GO_INSTALL_DIR="/usr/local"

echo "Downloading and installing Go ${GO_VERSION}..."
curl -L -o /tmp/go.tar.gz "${GO_DOWNLOAD_URL}"
sudo tar -C "${GO_INSTALL_DIR}" -xzf /tmp/go.tar.gz
rm /tmp/go.tar.gz

echo 'export PATH=$PATH:/usr/local/go/bin' >> "${HOME}/.bashrc"
export PATH=$PATH:/usr/local/go/bin

# Step 2: Set up Go workspace
echo "Setting up Go workspace..."
mkdir -p "${HOME}/go"
echo 'export GOPATH=${HOME}/go' >> "${HOME}/.bashrc"
export GOPATH="${HOME}/go"
echo 'export PATH=$PATH:${GOPATH}/bin' >> "${HOME}/.bashrc"
export PATH=$PATH:${GOPATH}/bin

# Step 3: Install Git (if not already installed)
if ! command -v git >/dev/null; then
  echo "Installing Git..."
  if [ "$OS" = "linux" ]; then
    sudo apt-get update
    sudo apt-get install -y git
  elif [ "$OS" = "darwin" ]; then
    # Assumes Homebrew is installed on macOS
    brew install git
  else
    echo "Unsupported operating system. Exiting."
    exit 1
  fi
else
  echo "Git is already installed."
fi

# Step 4: Clone piawgcli repository
REPO_URL="https://gitlab.com/ddb_db/piawgcli.git"
REPO_PATH="${GOPATH}/src/gitlab.com/ddb_db/piawgcli"
echo "Cloning piawgcli repository..."
git clone "${REPO_URL}" "${REPO_PATH}"

# Step 5: Change to the project directory
cd "${REPO_PATH}"

# Step 6: Install dependencies and build the project
echo "Building piawgcli project..."
go build

echo "Script complete"

