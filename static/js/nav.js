
function openUpload(){
    $("#upload_overlay").slideDown(200);
    document.getElementById("upload_overlay").style.height="100%";
    document.getElementById("upload").innerHTML="Close";
    document.getElementById("upload").onclick=closeUpload;
    document.getElementById("upload").style.zIndex=2;
    console.log("Opened");
}
function closeUpload(){
    $("#upload_overlay").slideUp(200);
    document.getElementById("upload_overlay").style.height="0%";
    document.getElementById("upload").innerHTML="Upload";
    document.getElementById("upload").onclick=openUpload;
    console.log("closed");
}