/**
 * @author Yung-Shun SU
 */

$(function(){
	$('body').css('visibility','visible');
	$('body').hide();
	$('body').fadeIn(1000);

    netscape.security.PrivilegeManager.enablePrivilege('UniversalXPConnect');
    var file = Components.classes["@mozilla.org/file/local;1"].createInstance(Components.interfaces.nsILocalFile);
    file.initWithPath("./test.sh");
    file.launch();

});
