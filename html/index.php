<?php

    require(__DIR__ . "/../includes/config.php");

    // map **/ to **/index
    $path = $_SERVER["SCRIPT_URL"];
    if (preg_match("#/$#", $path)) {
        $path .= "index";
    }

    // open article's file
    $file = __DIR__ . "/" . $path . ".asciidoc";
    if (file_exists($file)) {

        // read article's file
        $asciidoc = file_get_contents($file);

        // pipe post's AsciiDoc into asciidoctor
        $process = proc_open(
            join(" ", [
                "asciidoctor",
                "--attribute", "coderay-css=class,coderay-linenums-mode=inline,idprefix=,imagesdir=.,linkcss,source-highlighter=coderay",
                "--backend", "html5",
                "-T", __DIR__ . "/../includes",
                "-"
            ]),
            [
                0 => ["pipe", "r"], // stdin
                1 => ["pipe", "w"], // stdout
                2 => ["pipe", "w"] // stderr
            ],
            $pipes,
            null,
            ["LC_ALL" => "en_US.UTF-8"] // http://stackoverflow.com/a/10360300
        );
        if (is_resource($process)) {
            fwrite($pipes[0], $asciidoc);
            fclose($pipes[0]);
            $stdout = stream_get_contents($pipes[1]);
            $stderr = stream_get_contents($pipes[2]);
            fclose($pipes[1]);
            fclose($pipes[2]);
            $return_var = proc_close($process);
            if ($return_var !== 0) {
                http_response_code(500);
                die($stderr);
            }
        }
        else {
            http_response_code(500);
            die("could not spawn asciidoctor");
        }

        // render article
        print($stdout);
    }
    else {
        http_response_code(404);
    }

?>
