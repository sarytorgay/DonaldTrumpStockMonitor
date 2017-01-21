$(document).ready(function(){
	var el = create_table_entry("1,002", "Name", "ayy lmao", "email", "phone");
	$('tbody').append(el);
	$.ajax({
		'type': "GET",
		'url': "/monitor.json",
		'dataType': "json",
		'success': function(data){
			populateTable(data);
		}
	});
});

var populateTable = function(companies) {
	for (i in companies) {
		var name = i;
		var sym = companies[i]["Symbol"];
		var sharePriceInit = companies[i]["Initial-share-price"];
		var sharePriceCurr = companies[i]["Current-share-price"];
		var dateTweeted = companies[i]["Date-mentioned"];
		$('tbody').append(create_table_entry(sym, name, dateTweeted, sharePriceInit, sharePriceCurr));
	}
}

var create_table_entry = function() {
	// take a number of arguments, and return a table row of elements
	var t = "<tr>"
	for(var i = 0; i < arguments.length; i++)
		t += "<td>" + arguments[i] + "</td>";
	t += "</tr>";
	return t;
}
