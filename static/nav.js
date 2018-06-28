
function openUpload(){
    document.getElementById("upload_overlay").style.height="100%";
    document.getElementById("upload").innerHTML="Close";
    document.getElementById("upload").onclick=closeUpload;
    document.getElementById("upload").style.zIndex=2;
    console.log("Opened");
}
function closeUpload(){
    document.getElementById("upload_overlay").style.height="0%";
    document.getElementById("upload").innerHTML="Upload";
    document.getElementById("upload").onclick=openUpload;
    console.log("closed");
}