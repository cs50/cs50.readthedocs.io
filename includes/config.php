<?php

    // ensure $_SESSION exists
    session_start();

    // require PHP 5.4
    if (version_compare(PHP_VERSION, "5.4.0", "<")) {
        trigger_error("requires PHP 5.4.0 or higher", E_USER_ERROR);
    }

    // yum install php-pecl-yaml
    if (!extension_loaded("yaml")) {
        trigger_error("missing yaml extension module", E_USER_ERROR);
    }

    // gem install asciidoctor
    if (!file_exists("/usr/local/bin/asciidoctor")) {
        trigger_error("missing asciidoctor", E_USER_ERROR);
    }

    // gem install coderay
    if (!file_exists("/usr/local/bin/coderay")) {
        trigger_error("missing coderay", E_USER_ERROR);
    }

    // gem install sass
    if (!file_exists("/usr/local/bin/sass")) {
        trigger_error("missing sass", E_USER_ERROR);
    }

    // default time zone
    date_default_timezone_set("America/New_York");

    // require functions
    require_once(__DIR__ . "/functions.php");

?>
