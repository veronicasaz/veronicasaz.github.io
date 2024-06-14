<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Personal Webpage</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            color: #333;
            margin: 0;
            padding: 0;
        }
        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
            background-color: #ffffff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        header {
            text-align: center;
            padding: 20px 0;
            background-color: #4682b4;
            color: white;
        }
        header h1 {
            margin: 0;
            color: white;
        }
        nav {
            display: flex;
            justify-content: center;
            background-color: #87ceeb;
            padding: 10px 0;
        }
        nav a {
            margin: 0 15px;
            text-decoration: none;
            color: white;
            font-weight: bold;
        }
        nav a:hover {
            text-decoration: underline;
        }
        .tab-content {
            display: none;
            padding: 20px;
            background-color: #f0f8ff;
            border: 1px solid #87ceeb;
            border-top: none;
        }
        .tab-content.active {
            display: block;
        }
    </style>
    <script>
        function openTab(event, tabName) {
            var i, tabContent, tabLinks;
            tabContent = document.getElementsByClassName("tab-content");
            for (i = 0; i < tabContent.length; i++) {
                tabContent[i].style.display = "none";
            }
            tabLinks = document.getElementsByTagName("a");
            for (i = 0; i < tabLinks.length; i++) {
                tabLinks[i].className = tabLinks[i].className.replace(" active", "");
            }
            document.getElementById(tabName).style.display = "block";
            event.currentTarget.className += " active";
        }
        document.addEventListener("DOMContentLoaded", function() {
            document.getElementById("defaultOpen").click();
        });
    </script>
</head>
<body>

    <div class="container">
        <header>
            <h1>John Doe's Personal Webpage</h1>
        </header>
        <nav>
            <a href="javascript:void(0);" class="tab-link" onclick="openTab(event, 'CV')" id="defaultOpen">Curriculum Vitae</a>
            <a href="javascript:void(0);" class="tab-link" onclick="openTab(event, 'Research')">Research</a>
            <a href="javascript:void(0);" class="tab-link" onclick="openTab(event, 'Personal')">Personal Information</a>
        </nav>
        <div id="CV" class="tab-content">
            <h2>Curriculum Vitae</h2>
            <p>Here you can add your curriculum vitae details.</p>
        </div>
        <div id="Research" class="tab-content">
            <h2>Research</h2>
            <p>Here you can add details about your research.</p>
        </div>
        <div id="Personal" class="tab-content">
            <h2>Personal Information</h2>
            <p>Here you can add your personal information.</p>
        </div>
    </div>

</body>
</html>