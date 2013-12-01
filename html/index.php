<?php

    require(__DIR__ . "/../includes/config.php");

    // get requested article's YAML and HTML, else 404
    if (false === (list($yaml, $html) = getArticle($_SERVER["SCRIPT_URL"], true))) {
        http_response_code(404);
    }
?>

<!DOCTYPE html>

<html>
    <head>

        <!-- asciidoctor -a coderay-css=class,linkcss,source-highlighter=coderay -b html5 -D . /dev/null -->
        <link href="/css/asciidoctor.css" rel="stylesheet"/>
        <link href="/css/asciidoctor-coderay.css" rel="stylesheet"/>

        <!-- http://jquery.com/download/ -->
        <script src="/lib/jquery-1.10.1.min.js"></script>

        <title>
            <?php

                if (http_response_code() !== 403 && isset($data["yaml"]["title"])) {
                    print(htmlspecialchars($data["yaml"]["title"]) . " / ");
                }
                print("CS50 Manual");

            ?>
        </title>
    </head>

    <body class="article toc2 toc-left">

        <div>
            <script>
                (function() {
                    var cx = '017253632348184728259:xgoc3uuwm2s';
                    var gcse = document.createElement('script');
                    gcse.async = true;
                    gcse.src = (document.location.protocol == 'https:' ? 'https:' : 'http:') +
                        '//www.google.com/cse/cse.js?cx=' + cx;
                    var s = document.getElementsByTagName('script')[0];
                    s.parentNode.insertBefore(gcse, s);
                })();
            </script>
            <gcse:search></gcse:search>  
        </div>

        <?php

            if (isset($yaml["title"])) {
                if ($_SERVER["SCRIPT_URL"] != "/") {
                    print("<h1>" . htmlspecialchars($yaml["title"]) . "</h1>");
                }
                print($html);
            }

        ?>

        <div id="copyright">Copyright &#169; <?= date("Y") ?>, CS50</div>

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
