
// record = document.getElementById("record");
// record.addEventListener("click", function() {dispBlockAndNone("check-record", "record")}, false);
// checkRecord = document.getElementById("check-record");
// checkRecord.addEventListener("click", function() {dispBlockAndNone("record", "check-record")}, false);

textS = document.getElementById("text-s");
textS.addEventListener("input", function() {
	if (textS.value.length >= 1) {
		document.getElementById("check-text-s").style.display = "block";
	} else {
		document.getElementById("check-text-s").style.display = "none";
	}}, false);

// upload = document.getElementById("upload");
// upload.addEventListener("click", function() {dispBlockAndNone("check-upload", "upload")}, false);
// checkUpl = document.getElementById("check-upload");
// checkUpl.addEventListener("click", function() {dispBlockAndNone("upload", "check-upload")}, false);


function dispBlockAndNone(dBlock, dNone) {
	console.log("aaaaaaaaaaaa");
	document.getElementById(dBlock).style.display = "block";
	document.getElementById(dNone).style.display = "none";
};





navigator.mediaDevices.getUserMedia({audio:true})
    .then(stream => {handlerFunction(stream)})
	
	function handlerFunction(stream) {
    	rec = new MediaRecorder(stream);
        rec.ondataavailable = e => {
        	audioChunks.push(e.data);
        	if (rec.state == "inactive") {
            	let blob = new Blob(audioChunks, {type:'audio/mpeg-3'});
            	recordedAudio.src = URL.createObjectURL(blob);
            	recordedAudio.controls=true;
            	recordedAudio.autoplay=true;
            	sendData(blob)
            }
        }
    }
    function sendData(data) {}

    record.onclick = e => {
    	console.log('I was clicked')
    	record.disabled = true;
    	record.style.backgroundColor = "blue"
    	stopRecord.disabled = false;
    	audioChunks = [];
    	rec.start();
    }
    stopRecord.onclick = e => {
    	console.log("I was clicked")
    	record.disabled = false;
    	stop.disabled = true;
    	record.style.backgroundColor = "red"
    	rec.stop();
    }