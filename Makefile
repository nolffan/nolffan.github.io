# Preview the site locally, built as GitHub Pages builds it (needs Docker).
# GitHub Pages itself builds the site from the branch on every push.
IMAGE := ruby:3.3
# Gems are kept in a docker volume, so the second run is quick.
RUN   := docker run --rm -u $(shell id -u):$(shell id -g) -e HOME=/tmp \
         -v nolffan-site-gems:/gems -e BUNDLE_PATH=/gems \
         -v "$(CURDIR)":/site -w /site

.PHONY: build serve clean gems
gems:             # the gem volume, owned by us
	docker run --rm -v nolffan-site-gems:/gems $(IMAGE) chown $(shell id -u):$(shell id -g) /gems
build: gems       ## build into _site/
	$(RUN) $(IMAGE) sh -c 'bundle install --quiet && bundle exec jekyll build'
serve: gems       ## serve on http://localhost:4000, rebuilding on change
	$(RUN) -p 4000:4000 $(IMAGE) sh -c 'bundle install --quiet && bundle exec jekyll serve --host 0.0.0.0 --livereload'
clean:            ## remove the build output
	rm -rf _site .jekyll-cache

# ---------------------------------------------------------------------------
# The binary explorer's data (explorer/<repo>/, _data/explorer/<repo>.json),
# from each project's own build: run `make` in the project first, and push
# its commit, since the source links name it (or pass ARGS=--unpushed).
#   make explorer                  every project
#   make explorer-nolf2src         one
#   make explorer-avp2src ARGS=--only=PHCShell.dll,PHObject.lto
SRC      ?= $(HOME)/src
EXPLORER := nolfsrc avp2src nolf2src cjacksrc tron20src lithtools
explorer_nolfsrc   := --title "No One Lives Forever"
explorer_avp2src   := --title "Aliens versus Predator 2"
explorer_nolf2src  := --title "No One Lives Forever 2"
explorer_cjacksrc  := --title "Contract J.A.C.K."
explorer_tron20src := --title "Tron 2.0"
explorer_lithtools := --title "lithtools: the Talon tools" --subdir legacy/talon

.PHONY: explorer $(EXPLORER:%=explorer-%)
explorer: $(EXPLORER:%=explorer-%)    ## regenerate the explorer for every project
$(EXPLORER:%=explorer-%): explorer-%:
	python3 tools/explorer/gen.py --repo $(SRC)/$* $(explorer_$*) $(ARGS)
