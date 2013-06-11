<?php

    require_once(__DIR__ . "/../includes/config.php");

    // sass
    header("Content-Type: text/css");
    if (file_exists(__DIR__ . $_SERVER["SCRIPT_URL"])) {
        print(shell_exec("/usr/local/bin/sass --no-cache " . escapeshellarg(__DIR__ . $_SERVER["SCRIPT_URL"])));
    }

?>
