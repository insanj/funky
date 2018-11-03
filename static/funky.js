var the_socket = io.connect(null, {port: location.port, rememberTransport: false});

document.getElementById('prompt_input').onkeydown = function(event) {
    var e = event || window.event;
    if(e.keyCode == 13) {
    	the_text = document.getElementById('prompt_input').value;
    	document.getElementById('prompt_input').value = ""; 
        //console.log(the_text);
        the_socket.emit("prompt_input", {"text" : the_text})
    }
}

the_socket.on("text_response", function(socket_data) {
	var new_text = socket_data["text"];
	var existing_text = document.getElementById('text_display').innerHTML;
	var replacement_text = null;
	if (socket_data["flag"] == true) {
		replacement_text = "<pre><span style='color:red;'>" + new_text + "</span>" + existing_text + "</pre>";
	} else {
		replacement_text = "<pre>" + new_text + existing_text + "</pre>";
	}
	document.getElementById('text_display').innerHTML = replacement_text;
	//console.log(replacement_text);
});