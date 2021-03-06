//global vars
var container;
var files;


window.onload = function(){
    container=$('.container');
    refresh_files();
   
}
function refresh_files(){
    $.ajax({
        type: 'GET',
        url: '/ajax/files',
        success: function(data){
            if(files==undefined){
                files=data;
                render_files(files);
            }else{
                    container.empty();
                    files=data;
                    render_files(files);
                }        
        }
    });
}
function render_files(files){
    var template = $("#item_template").html();
    $.each(files,function(i,file){
        var temp = template.replace("{{file_type}}",file.thumbnail);
        temp = temp.replace(/{{file_name}}/g,file.name);
        temp = temp.replace(/{{file_location}}/g,file.location);
        container.append(temp);
        //console.log("appended: " + temp);
    });
}


//refresh files


window.setInterval(function(){
    refresh_files();
},1000);