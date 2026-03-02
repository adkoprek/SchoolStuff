#!/usr/bin/env bash

set -e

# ---------- Styling ----------
GREEN="\033[1;32m"
BLUE="\033[1;34m"
RED="\033[1;31m"
YELLOW="\033[1;33m"
RESET="\033[0m"

line() {
  echo -e "${BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
}

section() {
  line
  echo -e "${GREEN}$1${RESET}"
  line
}

error() {
  echo -e "${RED}❌ $1${RESET}"
}

success() {
  echo -e "${GREEN}✅ $1${RESET}"
}

info() {
  echo -e "${YELLOW}➜ $1${RESET}"
}

# ---------- Check git repo ----------
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  error "Not inside a git repository."
  exit 1
fi

# ---------- Timestamp ----------
timestamp=$(date "+%Y-%m-%d:%H-%M-%S")
message="Uploaded data for ${timestamp}"

section "Git Upload"

info "Repository: $(git rev-parse --show-toplevel)"
info "Commit message: \"$message\""
echo

# ---------- Status ----------
section "Current Changes"
git status --short || true
echo

# ---------- Add ----------
section "Adding Files"
git add .
success "Files staged."
echo

# ---------- Check if anything to commit ----------
if git diff --cached --quiet; then
  info "Nothing to commit."
  exit 0
fi

# ---------- Commit ----------
section "Creating Commit"

if git commit -m "$message"; then
  success "Commit created successfully!"
else
  error "Commit failed."
  exit 1
fi

echo

# ---------- Summary ----------
section "Last Commit Summary"
git log -1 --stat
echo

# ---------- Push (if possible) ----------
section "Pushing to Remote"

# Check if a remote exists
if git remote get-url origin >/dev/null 2>&1; then
  current_branch=$(git branch --show-current)

  info "Remote detected: origin"
  info "Branch: $current_branch"

  # Try pushing, but don't fail script if it doesn't work
  if git push -u origin "$current_branch"; then
    success "Pushed successfully!"
  else
    info "Push failed (no permission, offline, or conflict). Skipping."
  fi
else
  info "No remote repository configured. Skipping push."
fi

echo
success "Done 🚀"
