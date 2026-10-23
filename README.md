# truesource-demo-ai-gateway

A demo application for [TrueSource Viewer](https://github.com/nkuhn-vmw/truesource-viewer-hub-edition).
It is not meant to run: `requirements.txt` and the Dockerfile pin versions on purpose, so that the
viewer has something to find.

- **`litellm` 1.107.0, the release compromised on PyPI on 2026-10-21** (OSV `MAL-2026-2144`). Its
  wheels installed a credential stealer and a remote code loader; PyPI removed it the same day, so
  it can no longer be installed. LiteLLM is not in TrueSource at all, which is the point: the
  viewer shows it as "Not in TrueSource" and flags the version as malicious.
  The last safe release is 1.106.2.
- Python libraries TrueSource does carry, in versions with known vulnerabilities: `fastapi`
  0.109.0, `python-multipart` 0.0.6, `requests` 2.31.0.
- `python:3.12.0-slim`: an old Python 3.12 image.

This repository contains no malicious code: only the version pins.

References: [LiteLLM's incident report](https://docs.litellm.ai/blog/security-incident-oct-21-2026),
[OSV MAL-2026-2144](https://osv.dev/vulnerability/MAL-2026-2144).
