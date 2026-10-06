#!/usr/bin/env bash
# Push the Rose site (main) to RoseCompanion/rosecompanion.github.io using the agent-studio GitHub token.
set -euo pipefail
set -a; . /root/agent-studio/.env; set +a
B64=$(printf 'x-access-token:%s' "$GITHUB_TOKEN" | base64 -w0)
cd /root/rose-site
git -c http.extraheader="Authorization: Basic $B64" push -q https://github.com/RoseCompanion/rosecompanion.github.io.git main
echo "rose-site: pushed $(git log --oneline -1)"
