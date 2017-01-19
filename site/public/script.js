$(document).on('ready', function(){
	create_table_entry("Name", "email", "phone");
});

var create_table_entry = function() {
	for(var i = 0; i < arguments.length; i++)
		console.log(arguments[i]);
}
