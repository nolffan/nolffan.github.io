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
