var lang = "Java"
var e = ace.edit("codeeditor")
e.getSession().setMode("ace/mode/java");
e.setFontSize("15px");

e.setTheme("ace/theme/monokai")


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
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(questionName).style.display = "block";
    evt.currentTarget.className += " active";
}

function runCode() {
    if (e.getValue() != "") {
        $('.loader').show();
        var ajaxMins = new Date().getMinutes();
        var ajaxSecs = new Date().getSeconds();
        var ajaxMS = new Date().getMilliseconds();
        $.ajax({
            type: 'POST',
            url: 'compile_run/',
            dataType: 'json',
            cache: false,
            async: true,
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}',
                code: e.getValue(),
                input: $('#input').val(),
                language_id: document.getElementById("language").value,
            },
            success: function(json) {
                $('.loader').hide();
                $('#output').html(json.msg);
            }
        }).done(function() {
            var ajaxMins2 = new Date().getMinutes() - ajaxMins;
            var ajaxSecs2 = (new Date().getSeconds() % 60) - ajaxSecs;
            var ajaxMS2 = new Date().getMilliseconds() - ajaxMS;
            console.log(ajaxSecs2, " seconds");
        });
    } else {
        $('#output').html("Don't submit empty code");
    }
}