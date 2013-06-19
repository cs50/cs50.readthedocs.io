$(document).ready(function() {
    // fix ordered lists so that they are numbered correctly
    $("#toc li > ol").each(function(i, e) {
        var $parent = $(e).parent();
        $(e).appendTo($parent.prev());
        $parent.remove();
    });
});
