<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Personal Webpage</title>
  <style>
    body {
      font-family: Serif, sans-serif;
      background-color: #DBF9DB;
      color: #333;
      margin: 0;
      padding: 0;
    }

    .container {
      width: 98%;
      max-width: 1200px;
      margin: 0 auto;
      padding: 0px;
      background-color: #DBF9DB;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      text-align: center;
      padding: 20px;
      background: linear-gradient(90deg, #4682b4, #DBF9DB);
      color: white;
    }

    header h1 {
      margin: 0;
      color: white;
    }

    .toggle-container {
      display: flex;
      align-items: center;
    }

    .toggle-container input[type="checkbox"] {
      display: none;
    }

    .toggle-container label {
      cursor: pointer;
      position: relative;
      display: inline-block;
      width: 38px;
      height: 22px;
      background-color: #ccc;
      border-radius: 34px;
    }

    .toggle-container label::before {
      content: "";
      position: absolute;
      top: 1px;
      left: 1px;
      width: 20px;
      height: 20px;
      background-color: white;
      border-radius: 50%;
      transition: 0.4s;
    }

    .toggle-container input:checked+label::before {
      transform: translateX(15px);
    }

    .toggle-container input:checked+label {
      background-color: #2196F3;
    }

    nav {
      display: flex;
      justify-content: center;
      background-color: #DBE9FA;
      padding: 10px 0;
    }

    nav a {
      margin: 0 15px;
      text-decoration: none;
      color: #033E3E;
      font-weight: bold;
    }

    nav a:hover {
      text-decoration: underline;
    }

    .tab-content {
      display: none;
      padding: 20px;
      background-color: #f0f8ff;
      border: 3px solid #DBE9FA;
      color: #033E3E;
      border-top: none;
    }

    .tab-content.active {
      display: block;
    }

    .dark-mode {
      background-color: #2C3539;
      color: white;
    }

    .dark-mode header {
      background: linear-gradient(90deg, #222, #3B9C9C);
    }

    .dark-mode nav {
      background-color: #3B9C9C;
    }

    .dark-mode nav a {
      color: white;
    }

    .dark-mode .tab-content {
      background-color: #2C3539;
      border-color: #666;
      color: white;
    }

    .dark-mode .container {
      background-color: #2C3539;
      box-shadow: none;
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
        function toggleDarkMode() {
            document.body.classList.toggle("dark-mode");
        }
        document.addEventListener("DOMContentLoaded", function() {
            document.getElementById("defaultOpen").click();
            document.getElementById("darkModeToggle").addEventListener("change", toggleDarkMode);
        });
  </script>
</head>

<body>

  <div class="container">
    <header>
      <h1><i>Veronica Saz Ulibarrena</i></h1>
      <div class="toggle-container">
        <input type="checkbox" id="darkModeToggle">
        <label for="darkModeToggle"></label>
      </div>
    </header>
    <nav>
      <a href="javascript:void(0);" class="tab-link" onclick="openTab(event, 'Personal')">About me</a>
      <a href="javascript:void(0);" class="tab-link" onclick="openTab(event, 'CV')" id="defaultOpen">Curriculum
        Vitae</a>
      <a href="javascript:void(0);" class="tab-link" onclick="openTab(event, 'Research')">Research</a>
    </nav>
    <div id="CV" class="tab-content">
      <h2>Curriculum Vitae</h2>
      <p>Here you can add your curriculum vitae details.</p>
    </div>
    <div id="Research" class="tab-content">
      <h2>Research</h2>
      <p>Here you can add details about your research.</p>
      <h3>Bachelor's Thesis</h3>
      <h3>Master's Thesis</h3>
      <h3>Ph.D. Thesis</h3>

      <ol>
        <li>Introduction:</li>
        <li>Chapter 1: </li>
        <li>Chapter 2:</li>
        <li>Chapter 3:</li>
        <li>Chapter 4:</li>
      </ol>
    </div>
    <div id="Personal" class="tab-content">
      <h2>About me</h2>
      <p>Here you can add your personal information.</p>
      <img src="your-image-url.jpg" alt="Your Image" style="max-width: 100%; height: auto;">
    </div>
  </div>

</body>

</html>