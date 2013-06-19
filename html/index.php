<?php

    require(__DIR__ . "/../includes/config.php");

    // get requested article's YAML and HTML
    list($yaml, $html) = getArticle($_SERVER["SCRIPT_URL"], true);

?>

<!DOCTYPE html>

<html>
    <head>
        <script type="text/javascript" src="//use.typekit.net/unc2dip.js"></script>
        <script type="text/javascript">try{Typekit.load();}catch(e){}</script>

        <!-- http://yuilibrary.com/yui/docs/cssreset/ -->
        <link href="/lib/yui-3.10.0/build/cssreset/cssreset-min.css" rel="stylesheet"/>

        <!-- http://yuilibrary.com/yui/docs/cssbase/ -->
        <link href="/lib/yui-3.10.0/build/cssbase/cssbase-min.css" rel="stylesheet"/>

        <!-- https://github.com/pie4dan/CodeRay-GitHub-Theme/blob/master/coderay.css -->
        <link href="/css/coderay.css" rel="stylesheet"/>

        <!-- https://github.com/asciidoctor/asciidoctor/blob/master/stylesheets/asciidoctor.css -->
        <link href="/css/asciidoctor.css" rel="stylesheet"/>

        <link href="/css/styles.scss" rel="stylesheet"/>

        <!-- http://jquery.com/download/ -->
        <script src="/lib/jquery-1.10.1.min.js"></script>

        <script src="/js/scripts.js"></script>

        <title>
            <?php
                if (http_response_code() !== 403 && isset($data["yaml"]["title"])) {
                    print(htmlspecialchars($data["yaml"]["title"]) . " / ");
                }
                print("CS50 Manual");

            ?>
        </title>
    </head>

    <body>
        <div id="background"></div>
        <div id="container" <?php if ($_SERVER["SCRIPT_URL"] != "/") { echo 'class="not-main"'; } else { echo 'class="main"'; } ?>>
            <div id="container-background"></div>
            <div id="search-wrapper">
                <script>
                    (function() {
                        var cx = '017253632348184728259:-z318fz0ofk';
                        var gcse = document.createElement('script');
                        gcse.type = 'text/javascript';
                        gcse.async = true;
                        gcse.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') +
                            '//www.google.com/cse/cse.js?cx=' + cx;
                        var s = document.getElementsByTagName('script')[0];
                        s.parentNode.insertBefore(gcse, s);
                    })();
                </script>
                <gcse:search></gcse:search>  
            </div>
            <?php if (isset($yaml["title"])): ?>
                <h1 class="manual"><a href="/">CS50 Manual</a></h1>
                <?php if ($_SERVER["SCRIPT_URL"] != "/"): ?>
                    <h1 class="page-title"><?= htmlspecialchars($yaml["title"]) ?></h1>
                <?php endif; ?>
                <?= $html ?>
            <?php endif ?>
        </div>

        <script>

            var _gaq = _gaq || [];
            _gaq.push(['_setAccount', 'UA-8162502-39']);
            _gaq.push(['_trackPageview']);

            (function() {
              var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
              ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
              var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
            })();

        </script>

    </body>
</html>
