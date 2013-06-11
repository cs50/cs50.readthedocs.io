# Installation

*Assumes [CS50 Appliance 17](https://manual.cs50.net/CS50_Appliance_17).*

Inside appliance as `root`:

    sudo su -
    yum install php-pecl-yaml
    gem install asciidoctor coderay sass
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

To create a new post using, e.g., `vim`:

    cd ~/vhosts/manual.cs50.net/html
    vim foo.asciidoc

The contents of `foo.asciidoc` should be, e.g.:

    ---
    tags: [quizzes]
    title: How to Proctor
    ---

    Once upon a time...

where `tags` and `title` constitute "YAML front matter" (i.e., metadata).

# Deployment

*requires that your SSH key be added to `build.x.cs50.net`*

    git remote add production ssh://ec2-user@build.x.cs50.net/home/ec2-user/var/manual50.git # once
    git push production master # thereafter

# References

* [AsciiDoc cheatsheet](http://powerman.name/doc/asciidoc)
