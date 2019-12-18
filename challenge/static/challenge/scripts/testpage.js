window.define = window.define || ace.define;
var lang = "Java"
ace.require("ace/ext/language_tools");
    var editor = ace.edit("codeeditor");
    editor.session.setMode("ace/mode/c_cpp");
    editor.setTheme("ace/theme/monokai");
    editor.setFontSize("15px");
    editor.renderer.setScrollMargin(10, 10);
    // enable autocompletion and snippets
    editor.setOptions({
        enableBasicAutocompletion: true,
        enableSnippets: true,
        enableLiveAutocompletion: true,
    });
alert(u_id);
    $(window).load(function() {
        var u_id

        console.log(u_id);
console.log(c_id);
console.log(u); });
    
// Set the date we're counting down to
var countDownDate = new Date(end_time).getTime();

// Update the count down every 1 second
var x = setInterval(function() {

    // Get today's date and time
    var now = new Date().getTime();

    // Find the distance between now and the count down date
    var distance = countDownDate - now;

    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Output the result in an element with id="demo"
    document.getElementById("demo").innerHTML = hours + " : " +
        minutes + " : " + seconds;

    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("demo").innerHTML = "EXPIRED";
    }
}, 1000);

function openQuestion(evt, questionName) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
        // tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(questionName).style.display = "block";
    evt.currentTarget.className += " active";
}
function selectLang() {
    lang = document.getElementById("language").value;
    if (lang == "Java") {
        editor.getSession().setMode("ace/mode/java");
        editor.setValue("Java");
    }
    else if (lang == "C" || lang == "C++" ) {
        editor.getSession().setMode("ace/mode/c_cpp");
        editor.setValue("#include");
    }
    else if(lang == "C#"){
        editor.getSession().setMode("ace/mode/csharp");
        editor.setValue("import");
    }
    else if(lang=="Python"){
        editor.getSession().setMode("ace/mode/python");
        editor.setValue("def new():");

    }
}



