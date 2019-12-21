window.define = window.define || ace.define;
function instructionPop() {
    var popup = document.getElementById("myPopup");
    popup.classList.toggle("show");
  }
  function instructionPop2() {
    var popup = document.getElementById("myPopup2");
    popup.classList.toggle("show");
  }
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
    document.getElementById("demo").innerHTML = +hours + " h : " +
        minutes + " m : " + seconds + " s";

    // If the count down is over, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("demo").innerHTML = "EXPIRED";
    }
}, 1000);
$(function() {
    var editor = ace.edit("codeeditor"),
        session = editor.getSession(),
        Range = require("ace/range").Range,
        range = new Range(0, 4, 3, 15),
        markerId = session.addMarker(range, "readonly-highlight");

    session.setMode("ace/mode/javascript");
    editor.keyBinding.addKeyboardHandler({
        handleKeyboard: function(data, hash, keyString, keyCode, event) {
            if (hash === -1 || (keyCode <= 40 && keyCode >= 37)) return false;

            if (intersects(range)) {
                return { command: "null", passEvent: false };
            }
        }
    });

    before(editor, 'onPaste', preventReadonly);
    before(editor, 'onCut', preventReadonly);

    range.start = session.doc.createAnchor(range.start);
    range.end = session.doc.createAnchor(range.end);
    range.end.$insertRight = true;

    function before(obj, method, wrapper) {
        var orig = obj[method];
        obj[method] = function() {
            var args = Array.prototype.slice.call(arguments);
            return wrapper.call(this, function() {
                return orig.apply(obj, args);
            }, args);
        }

        return obj[method];
    }

    function intersects(range) {
        return editor.getSelectionRange().intersects(range);
    }

    function preventReadonly(next, args) {
        if (intersects(range)) return;
        next();
    }
});