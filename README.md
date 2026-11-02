# nolffan.github.io

The project site for [nolfsrc](https://github.com/nolffan/nolfsrc),
[nolf2src](https://github.com/nolffan/nolf2src),
[cjacksrc](https://github.com/nolffan/cjacksrc) and
[lithtools](https://github.com/nolffan/lithtools).

A [Jekyll](https://jekyllrb.com) site: GitHub Pages builds it from this
branch on every push, so there is nothing to build by hand.

| File | What it holds |
|---|---|
| `index.md` | the header, "The approach" cards, the closing sections (Markdown body) and the footer |
| `_projects/*.md` | one file per project: its section's text (Markdown body), and in the front matter its title, screenshots and progress figures; `order` sets where it appears |
| `_config.yml` | the site's title and description |
| `_layouts/default.html` | the page template |
| `style.css`, `img/` | the styling and the screenshots |

A project with `tools:` in its front matter (lithtools) is shown as a grid of
cards; one with `progress:` gets the progress panel. The progress figures
are copied by hand from the Progress table in each project's README.

To preview locally (needs Docker): `make serve`, then open
<http://localhost:4000>. `make build` builds into `_site/`.
