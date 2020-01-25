
// record.addEventListener("click", function() {dispBlockAndNone("check-record", "record")}, false);
// checkRecord = document.getElementById("check-record");
// checkRecord.addEventListener("click", function() {dispBlockAndNone("record", "check-record")}, false);

enterText.addEventListener("input", function() {
	if (enterText.value.length >= 1) {
		checkText.style.display = "block";
	} else {
		checkText.style.display = "none";
	}}, false);

// upload.addEventListener("click", function() {dispBlockAndNone("check-upload", "upload")}, false);
// checkUpl = document.getElementById("check-upload");
// checkUpl.addEventListener("click", function() {dispBlockAndNone("upload", "check-upload")}, false);

menuBtnUpl = document.getElementById("menu-btn-upload");
menuBtnText = document.getElementById("menu-btn-text");
menuBtnRec = document.getElementById("menu-btn-record");
menuBtnUpl.onclick = e => {
	methodButton.innerHTML = "Uploading";
	uploading.style.display = "inline-block";
	texting.style.display = "none";
	recording.style.display = "none";
}
menuBtnText.onclick = e => {
	methodButton.innerHTML = "Texting";
	uploading.style.display = "none";
	texting.style.display = "inline-block";
	recording.style.display = "none";
}
menuBtnRec.onclick = e => {
	methodButton.innerHTML = "Recording";
	uploading.style.display = "none";
	texting.style.display = "none";
	recording.style.display = "inline-block";
}

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
        checkRecord.style.display = "inline-block";
    }
    function sendData(data) {}

    record.onclick = e => {
    	console.log('I was clicked')
    	record.disabled = true;
    	record.style.backgroundColor = "blue"
    	stopRecord.disabled = false;
    	// checkRecord.style.display = "none";
    	audioChunks = [];
    	rec.start();
    }
    stopRecord.onclick = e => {
    	console.log("I was clicked")
    	record.disabled = false;
    	stop.disabled = true;
    	checkRecord.style.visibility = "visible";
    	record.style.backgroundColor = "red";
    	rec.stop();
    }