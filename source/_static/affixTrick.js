
$(document).ready(function(){
	
	// Local TOC.
	$(".bs-sidenavNew ul").addClass("nav nav-list");
	$(".bs-sidenavNew > ul > li > a").addClass("nav-header");

	if ($(".section").first().outerHeight()>($("#sidebar").outerHeight()+60)){
	console.log("NEW affix");
		/*$jqTheme("#sidebar").affix({
			offset: {
				top: 0,
				bottom: function () {
					return (this.bottom = $('.footer').outerHeight(true))
				}
			}
		});

		setInterval(function(){
			$(".section").first().css("min-height", $("#sidebar").outerHeight()+25);
		}, 1000);*/
	}
	
});

