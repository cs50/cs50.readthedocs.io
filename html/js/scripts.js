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
});
