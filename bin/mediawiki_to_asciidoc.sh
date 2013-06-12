# requires pandoc version 1.10.1 or higher: http://johnmacfarlane.net/pandoc/
echo "---
tags: []
title: $1
---" > $1.asciidoc

pandoc $1.mediawiki -f mediawiki -t asciidoc >> $1.asciidoc
