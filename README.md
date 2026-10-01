# Tiggy Bestmann

Public site: https://auraofintelligence.github.io/tiggy-bestmann/
Repository: https://github.com/auraofintelligence/tiggy-bestmann

A separate ten-page partner site for Australian Sire. Tiggy is the happy-go-lucky fool, artist and student of life.

The direction is fun and frivolous, with world travel and relationships at its centre. Different continents and cultures, outback gatherings, high society, sports, festivals, Aura retreats and creative work give the journey its variety. Trips are busy and time-limited, with work to do and plenty of fun around it. A sand sports, outdoor cinema and festival hub brings several interests together. Adult female characters are in their twenties and thirties, including visibly pregnant women. Tiggy keeps Luke's mature long-haired likeness. The site uses ten new generated heroes and an original generated favicon.

## Local preview

Run `python -m http.server 4174 --bind 127.0.0.1` in this directory. Open http://127.0.0.1:4174/.

Australian Sire's public partner site is https://auraofintelligence.github.io/australiansire/. The partner destination can be changed with the `SIRE_PARTNER_URL` environment variable before building.

## Build and check

Run `python scripts/build.py`, then `python scripts/check.py` and `node --check assets/site.js`.

The normal build uses Python's standard library. Page text lives in `scripts/build.py`, with shared styles and interactions in `assets/`. Generated HTML and finished images are included, so opening the files directly also works.

`scripts/prepare_artwork.py` is a one-time asset preparation tool using Pillow and the local original paths in `artwork-manifest.json`. It is not required to build or view the site. The original likeness photographs remain outside the repository.

## Status

Published from the public GitHub repository through GitHub Pages. The images are imagined scenes. No finished books, songs or real events are claimed by this profile.

See `SOURCES.md`, `ARTWORK.md` and `REVIEW.md` for the brief, provenance and verification.

## Publication and licence

GitHub Actions builds and checks the site, then publishes only the HTML, assets and licence. Main-branch pushes update the public site.

The [Strange But True Public Source Licence](LICENCE.md) allows attributed personal and non-commercial use; commercial rights remain reserved to Luke Nathan Hayes.

Both character sites link to Story Forge, Loose Goose Comedy Engine and Man and Mind, with reciprocal links on those sites.
