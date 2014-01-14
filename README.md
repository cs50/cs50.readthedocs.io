# Installation

*Assumes [CS50 Appliance 19](https://manual.cs50.net/appliance/19/).*

Inside appliance as `root`:

    sudo su -
    gem install asciidoctor coderay tilt 
    yum install php-pecl-yaml
    chmod 755 /usr/local/bin/*
    chmod 644 /usr/local/share/gems/specifications/sass*
    gem install sass
    exit

Inside appliance as `jharvard`:

    cd ~/vhosts
    git clone git@github.com:cs50/manual50.git manual.cs50.net
    cd manual.cs50.net
    ./bin/chmod

Outside appliance (assuming Mac):

    sudo su -
    echo "w.x.y.z manual.cs50.net" >> /etc/hosts # where w.x.y.z is appliance's IP address
    exit

# Troubleshooting

## Fixing Permissions

    chmod 700 ~/vhosts/manual.cs50.net/bin/chmod
    ~/vhosts/manual.cs50.net/bin/chmod

# Usage

To create a new article using, e.g., `vim`:

    cd ~/vhosts/manual.cs50.net/html
    vim foo.asciidoc

The contents of `foo.asciidoc` should be, e.g.:

    ---
    title: Foo
    ---

    Foo is a...

where `title` constitutes "YAML front matter" (i.e., metadata), and everything below ---\n is AsciiDoc.

See http://powerman.name/doc/asciidoc for an AsciiDoc cheatsheet.

# Style

## Headers

For headers use this format:

    == Level 1
    Text.

    === Level 2
    Text.

    ==== Level 3
    Text.

    ===== Level 4
    Text.

# Deployment

*requires that your SSH key be added to `build.x.cs50.net`*

    git remote add production ssh://ec2-user@build.x.cs50.net/home/ec2-user/var/manual50.git # once
    git push production master # thereafter

# References

* [AsciiDoc cheatsheet](http://powerman.name/doc/asciidoc)
* [How can I use asciidoc conf file](http://discuss.asciidoctor.org/How-can-I-use-asciidoc-conf-file-tp1005p1062.html)
