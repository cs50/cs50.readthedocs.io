BUILDDIR = _build
SOURCEDIR = .
SPHINXBUILD = sphinx-build
SPHINXOPTS =

.PHONY: all
all: depends dirhtml serve

.PHONY: depends
depends:
	pip install -r requirements.txt

.PHONY: help
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: serve
serve:
	http-server -i 0 _build/dirhtml/

.PHONY: Makefile
%: Makefile
	rm -rf "$(BUILDDIR)"
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
