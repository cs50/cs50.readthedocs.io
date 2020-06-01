BUILDDIR = _build
SOURCEDIR = .
SPHINXBUILD = sphinx-build
SPHINXOPTS =

.PHONY: help
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: depends
depends:
	pip install -r requirements.txt

.PHONY: Makefile
%: Makefile
	rm -rf "$(BUILDDIR)"
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
