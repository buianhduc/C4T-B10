var a=document.getElementById("song_container")
a.addEventListener("click",function(e){
    var element = e.target
    var div = element.parentNode;
    console.log(div)
});

var delbtn = document.getElementsByClassName("delBtn")
for (var i = 0; i<delbtn.length; i+=1)
{
    var delBTN = delbtn[i]
    delBTN.addEventListener('click', function(e){
        var del = e.target
        var div = del.parentNode;
        div.remove();
    });
}

var edit = document.getElementsByClassName("editBtn")
for (var i = 0; i<edit.length; i+=1)
{
    var edit_btn = edit[i]
    edit_btn.addEventListener('click', function(e){
        var edit_btn = e.target
        console.log(e.path[1].attributes[1].value)
    });
}

var more = document.getElementsByClassName("moreBtn")
for (var i = 0; i<more.length; i+=1)
{
    var more_btn = more[i]
    more_btn.addEventListener('click',function(e){
        more_btn = e.target
        console.log(e.path[1].attributes[1].value)
        console.log(e.path[1].attributes[2].value)
        console.log(e.path[1].attributes[3].value)
    });
}