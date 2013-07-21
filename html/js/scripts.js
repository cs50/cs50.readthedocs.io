$(document).ready(function() {
    // fix ordered lists so that they are numbered correctly
    $("#toc li > ol").each(function(i, e) {
        var $parent = $(e).parent();
        $(e).appendTo($parent.prev());
        $parent.remove();
    });

    $('#container .sect1').each(function(i, e) {
        $(e).addClass('label-' + (i % 6 + 1));
    });

    $('#container > #content > .ulist > ul > li, #container.main #preamble > .sectionbody > .ulist > ul >li').each(function(i, e) {
        $(e).addClass('label-' + (i % 6 + 1));
    });

    var bg = "/img/bg" + new Date().getDay() + ".jpg";

    $('#background').css({
       "background": "url(" + bg + ") no-repeat center center fixed", 
       "-webkit-background-size": "cover",
       "-moz-background-size": "cover",
       "-o-background-size": "cover",
       "background-size": "cover",
       "filter": "progid:DXImageTransform.Microsoft.AlphaImageLoader(src='" + bg + "', sizingMethod='scale')",
       "-ms-filter": "\"progid:DXImageTransform.Microsoft.AlphaImageLoader(src='#{$value}', sizingMethod='scale')\""
    });
});
