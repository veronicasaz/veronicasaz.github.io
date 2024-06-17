<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Personal Webpage</title>
  <style>
    /* CSS Reset */
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }

    body {
      font-family: 'Arial', sans-serif;
      background-color: #DBF9DB;
      color: #333;
    }

    .container {
      width: 95%;
      max-width: 1200px;
      margin: 20px auto;
      padding: 20px;
      background-color: #fff;
      box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
      border-radius: 10px;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 20px;
      background: linear-gradient(90deg, #4682b4, #DBF9DB);
      border-radius: 10px 10px 0 0;
      color: white;
    }

    header h1 {
      margin: 0;
      font-size: 2em;
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
      width: 40px;
      height: 24px;
      background-color: #ccc;
      border-radius: 34px;
      transition: background-color 0.3s;
    }

    .toggle-container label::before {
      content: "";
      position: absolute;
      top: 2px;
      left: 2px;
      width: 20px;
      height: 20px;
      background-color: white;
      border-radius: 50%;
      transition: 0.3s;
    }

    .toggle-container input:checked + label::before {
      transform: translateX(16px);
    }

    .toggle-container input:checked + label {
      background-color: #2196F3;
    }

    nav {
      display: flex;
      justify-content: center;
      background-color: #DBE9FA;
      padding: 15px 0;
      border-radius: 0 0 10px 10px;
    }

    nav a {
      margin: 0 15px;
      text-decoration: none;
      color: #033E3E;
      font-weight: bold;
      transition: color 0.3s;
    }

    nav a:hover {
      color: #4682b4;
    }

    .tab-content {
      display: none;
      padding: 20px;
      background-color: #f0f8ff;
      border: 3px solid #DBE9FA;
      color: #033E3E;
      border-top: none;
      border-radius: 0 0 10px 10px;
    }

    .tab-content.active {
      display: block;
      animation: fadeIn 0.5s;
    }

    @keyframes fadeIn {
      from {
        opacity: 0;
      }
      to {
        opacity: 1;
      }
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

    hr {
      border: none;
      border-top: 3px double #333;
      color: #333;
      overflow: visible;
      text-align: center;
      height: 5px;
    }

    a {
      color: #4682b4;
      text-decoration: none;
    }

    a:hover {
      text-decoration: underline;
    }

    .tab-content ol {
      margin-left: 30px;
    }
  </style>
  <script>
    function openTab(event, tabName) {
      var i, tabContent, tabLinks;
      tabContent = document.getElementsByClassName("tab-content");
      for (i = 0; i < tabContent.length; i++) {
        tabContent[i].classList.remove("active");
      }
      tabLinks = document.getElementsByTagName("a");
      for (i = 0; i < tabLinks.length; i++) {
        tabLinks[i].className = tabLinks[i].className.replace(" active", "");
      }
      document.getElementById(tabName).classList.add("active");
      event.currentTarget.className += " active";
    }

    function toggleDarkMode() {
      document.body.classList.toggle("dark-mode");
    }

    document.addEventListener("DOMContentLoaded", function () {
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
      <a href="javascript:void(0);" class="tab-link" onclick="openTab(event, 'Chapters')">Ph.D. Chapters</a>
    </nav>
    <div id="CV" class="tab-content">
      <h2>Curriculum Vitae</h2>
      <br>
      <p><a href="https://www.linkedin.com/in/veronica-saz-ulibarrena/">Linkedin</a>
      <br>
      <!-- <a href="Curriculum Vitae.pdf" download>CurriculumVitae.pdf</a> -->
      CV
      </p>
    </div>
    <div id="Research" class="tab-content">
      <h1><i>Research</i></h1>
      <br>
      <p>My research has been focused on the fields of interplanetary trajectory optimization (bachelor's and Master's thesis), 
        celestial dynamics and chaotic problems (Ph.D.) and Machine Learning (Master's thesis and Ph.D.). </p>
      <p> Here, I provide a summary of those and links to the corresponding publications</p>
      <br>
      <hr>
      <br>
      <h3>Bachelor's Thesis</h3>
      <br>
      <hr>
      <br>
      <h3>Master's Thesis</h3>
      <p>
      <i>Low-Thrust Interplanetary Trajectory Optimization Using Pre-Trained Artificial Neural Network Surrogates, 2021. </i>
      <a href="https://repository.tudelft.nl/islandora/object/uuid%3A09c8d317-4f4f-4cb9-9778-bc77b1dd8e59">Link to thesis</a>
      <br><br>
      <b>Abstract</b>
      <br>
      The use of low-thrust propulsion for interplanetary missions requires the implementation of new methods for the
      preliminary design of their trajectories. This thesis proposes a method using the Monotonic Basin Hopping global
      optimization algorithm to find feasible trajectories with optimum use of the mass of fuel for the case in which the
      trajectory is modeled using the Sims-Flanagan transcription method. Due to the large computational time required to find
      the global optimum, Artificial Neural Networks have been used to predict the objective value and feasibility terms of
      the local minimum. Therefore, the procedure to set up a working regression Artificial Neural Network is studied as well
      as its transferability to predict values outside the trained limits and for different missions. In addition to this, the
      use of pre-training is analyzed to improve the performance of the network without increasing the size of the training
      database.
      </p>
      <br>
      <hr>
      <br>
      <h3>Ph.D. Thesis</h3>
      <p>
      <i>Solving the gravitational N-body problem using Machine Learning</i>.
      </p>
      <ol>
          <br>
        <li><b>Introduction</b>: <i>Applications of Machine Learning for the simulation of celestial mechanics.</i></li>
        <li>
        <b>Chapter 1</b>: Saz Ulibarrena<i> et al., A hybrid approach for solving the gravitational N-body problem with Artificial Neural Networks, 2024.</i> 
        <a href="https://www.sciencedirect.com/science/article/pii/S0021999123006915">Link to publication</a>
        </li>
        <li><b>Chapter 2</b>: Horn <i> et al., A Generalized Framework of Neural Networks for Hamiltonian Systems, 2024.</i> <a href="">Link to publication</a></li>
        <li><b>Chapter 3</b>: Saz Ulibarrena<i> et al., Physics-based Reinforcement Learning for the integration of the
        chaotic gravitational N-body problem, 2024.</i>
        <a href="https://www.sciencedirect.com/science/article/pii/S0021999123006915">Link to publication</a>
        </li>        
        <li><b>Chapter 4</b>:</li>
        <li><b>Others</b>: 
          Beckers <i>et al., Individual chaotic behaviour of the S-stars in the Galactic centre, 2024.</i>
        <a href= "https://www.aanda.org/articles/aa/abs/2024/05/aa48361-23/aa48361-23.html">Link to publication</a>
          Horn et  al. Structure-Preserving Neural Networks for the N-body Problem, 2022.https://research.tue.nl/en/publications/structure-preserving-neural-networks-for-the-n-body-problem">Link to publication</a>
        </li>
      </ol>
    </div>
    <div id="Personal" class="tab-content">
      <h2>About me</h2>
      <br>
      <p>Here you can add your personal information.</p>
      <img src="your-image-url.jpg" alt="Your Image" style="max-width: 100%; height: auto;">
    </div>
    <div id="Chapters" class="tab-content">
    <p>
        <a href="HybridIntegration_Veronica_Revised2.pdf" download>Chapter 1</a>
        <br>
        <a href="aanda.pdf" download>Chapter 3</a>
        </p>
    </div>
  </div>

</body>

</html>