#!/usr/bin/env bash
# Historical OpenClaw-era GarageLogs article generator — intentionally retired.
#
# This script previously sourced an obsolete .openclaw/.secrets Gemini credential
# and generated article bodies through an external provider. Current M5/Hermes
# GarageLogs content uses Wren's local model via the `wren-garagelogs-blog-live`
# workflow instead. Keeping this fail-closed stub preserves historical context
# without allowing a stale secret/provider path to be revived accidentally.
set -euo pipefail

echo "RETIRED: use the wren-garagelogs-blog-live Hermes workflow; this old external-provider generator is disabled." >&2
exit 2
