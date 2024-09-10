<?php
header("X-CSUC: YV9tYW5kaV9iaWFyX3NlZ2VycnJyfQ==");
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hacker Web</title>
    <style>
        body {
            background-color: black;
            color: lime;
            font-family: "Courier New", Courier, monospace;
        }

        h1 {
            text-align: center;
            font-size: 3em;
            margin-top: 20%;
        }

        .terminal {
            text-align: center;
            font-size: 1.5em;
            margin-top: 20px;
        }

        .blinking-cursor {
            font-weight: 100;
            font-size: 1.5em;
            color: lime;
            -webkit-animation: 1s blink step-end infinite;
            animation: 1s blink step-end infinite;
        }

        @keyframes blink {
            from, to {
                color: transparent;
            }
            50% {
                color: lime;
            }
        }
    </style>
</head>
<body>
    <h1>Welcome to Hacker Web</h1>
    
    <div class="terminal">
        <span id="terminal-text">Initializing...</span><span class="blinking-cursor">|</span>
    </div>

    <script>
        if (performance.navigation.type == performance.navigation.TYPE_RELOAD) {
            console.log("%cFlag 1 : Q1NVQ3tKYW5nYW5fbHVw", "color: lime; font-size: 20px;");
        } else {
            console.log("Tutorial cara segar di web donk wkwk?");
        }

        var terminalText = document.getElementById("terminal-text");
        var messages = [
            "Connecting to the server...",
            "Access granted",
            "Initializing system...",
            "Welcome, hacker!"
        ];
        var messageIndex = 0;
        var charIndex = 0;

        function typeMessage() {
            if (charIndex < messages[messageIndex].length) {
                terminalText.innerHTML += messages[messageIndex].charAt(charIndex);
                charIndex++;
                setTimeout(typeMessage, 100);
            } else {
                charIndex = 0;
                messageIndex++;
                if (messageIndex < messages.length) {
                    terminalText.innerHTML += "<br>";
                    setTimeout(typeMessage, 500);
                }
            }
        }

        setTimeout(typeMessage, 1000);
    </script>
</body>
</html>
