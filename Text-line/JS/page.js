// document.addEventListener('DOMContentLoaded', function(){
    function w3_open() {
        document.getElementById("mySidebar").style.width = "100%";
        document.getElementById("mySidebar").style.display = "block";
      }
      
      function w3_close() {
        document.getElementById("mySidebar").style.display = "none";
      }
    var properties = document.getElementById("ReadMode");
    var propertiesBool = false;
    properties.addEventListener("click",function(){
        var foo = document.getElementById("change-menu");
        if(propertiesBool == false)
        {
            foo.style.display = "flex";
            propertiesBool = true;

        }
        else{
            foo.style.display = "none";
            propertiesBool = false;
        }
    })
    function openNav() {
        document.getElementById("mySidenav").style.width = "100%";
      }
      
      /* Close/hide the sidenav */
      function closeNav() {
        document.getElementById("mySidenav").style.width = "0";
      }
    var check = false;
    
    function myFunction(x) {
        x.classList.toggle("change");
        if (check == true){
            closeNav();
            check = false
        }
        else{
            openNav();
            check = true;
        }
    }
    var prevScrollpos = window.pageYOffset;
    window.onscroll = function() {
      var currentScrollPos = window.pageYOffset;
      if (prevScrollpos > currentScrollPos) {
        document.getElementById("NavBar").style.top = "0";
      } else {
        document.getElementById("NavBar").style.top = "-50px";
      }
      prevScrollpos = currentScrollPos;
    }
    var PlusAaBtn = document.getElementById("AaPlus");
    PlusAaBtn.addEventListener("click", function() {
        var obj = document.getElementsByTagName("ul");
        // style = window.getComputedStyle(obj, null).getPropertyValue('font-size');
        // currentSize = parseFloat(style);
        console.log(obj)
        // obj.style.fontSize = (currentSize + 1) +'px';
        // var obj = document.getElementsByTagName("li");
        // style = window.getComputedStyle(obj, null).getPropertyValue('font-size');
        // currentSize = parseFloat(style);
        // obj.style.fontSize = (currentSize + 1) +'px';
        // var obj = document.getElementsByTagName("br");
        // style = window.getComputedStyle(obj, null).getPropertyValue('font-size');
        // currentSize = parseFloat(style);
        // obj.style.fontSize = (currentSize + 1) +'px';
        // var obj = document.getElementsByTagName("h2");
        // style = window.getComputedStyle(obj, null).getPropertyValue('font-size');
        // currentSize = parseFloat(style);
        // obj.style.fontSize = (currentSize + 1) +'px';

    })
    var MinusAaBtn = document.getElementById("AaMinus");
    MinusAaBtn.addEventListener("click", function() {
        var obj = document.getElementById("text");
        style = window.getComputedStyle(obj, null).getPropertyValue('font-size');
        currentSize = parseFloat(style);
        obj.style.fontSize = (currentSize - 1) +'px';
    })
    var whiteBtn = document.getElementById("White");
    whiteBtn.addEventListener("click",function() {
        var obj = document.getElementsByTagName("body")[0];
        obj.style.backgroundColor = "white";
        obj.style.color = "black";
        for(var i=0; i<=4; i+=1)
        {
            document.getElementsByTagName("button")[i].style.borderColor = "white";
        }
        
    })
    var blackBtn = document.getElementById("Black");
    blackBtn.addEventListener("click",function() {
        var obj = document.getElementsByTagName("body")[0];
        obj.style.backgroundColor = "black";
        obj.style.color = "rgb(170,170,170)";
        document.getElementById("change-menu-title").style.color = "black";
        for(var i=0; i <= 4; i+=1)
        {
            document.getElementsByTagName("button")[i].style.borderColor = "black";
        }

    })
    var SepiaBtn = document.getElementById("Sepia");
    SepiaBtn.addEventListener("click",function() {
        var obj = document.getElementsByTagName("body")[0];
        obj.style.backgroundColor = "rgb(252,241,214)";
        obj.style.color = "rgb(98,75,45)";
        for(var i=0; i <= 3; i+=1)
        {
            document.getElementsByTagName("button")[i].style.borderColor = "rgb(252,241,214)";
        }
    })
    document.getElementById("search").addEventListener('mouseover', function(){
        document.getElementById("search").innerHTML = "Tìm kiếm " + '<i class="fas fa-search"></i>';
    })
    document.getElementById("search").addEventListener('mouseout', function(){
        document.getElementById("search").innerHTML = '<i class="fas fa-search"></i>'
    })

    document.getElementById("menu").addEventListener('mouseover', function(){
        document.getElementById("menu").innerHTML = "Menu " + '<i class="fas fa-bars"></i>';
    })
    document.getElementById("menu").addEventListener('mouseout', function(){
        document.getElementById("menu").innerHTML = '<i class="fas fa-bars"></i>'
    })

    document.getElementById("test").addEventListener('mouseover', function(){
        document.getElementById("test").innerHTML = "Kiểm tra " + '<i class="far fa-file-alt"></i>';
    })
    document.getElementById("test").addEventListener('mouseout', function(){
        document.getElementById("test").innerHTML = '<i class="far fa-file-alt"></i>'
    })
    
    document.getElementById("navigate").addEventListener('mouseover', function(){
        document.getElementById("navigate").innerHTML = "Đi đến " + '<i class="fas fa-location-arrow"></i>';
    })
    document.getElementById("navigate").addEventListener('mouseout', function(){
        document.getElementById("navigate").innerHTML = '<i class="fas fa-location-arrow"></i>'
    })

    document.getElementById("ReadMode").addEventListener('mouseover', function(){
        document.getElementById("ReadMode").innerHTML = "Chế độ đọc " + 'Aa';
    })
    document.getElementById("ReadMode").addEventListener('mouseout', function(){
        document.getElementById("ReadMode").innerHTML = 'Aa'
    })
    
//})