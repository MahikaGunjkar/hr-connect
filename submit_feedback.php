<?php
// Check if the form is submitted using the POST method
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve the employee ID from the form data
    $employeeId = $_POST["eid"];
    $rating = $_POST["rating"];
    $workLifeBalance = $_POST["work-life-balance"];
    $relationWithManager = $_POST["relation-with-manager"];
    $accomplishments = $_POST["accomplishments"];
    $goalsMetOrExceeded = $_POST["comments"];
    $receiveFeedback = $_POST["comments"];
    $workSatisfaction = $_POST["work-satisfaction"];
    $workLifeBalanceFactors = $_POST["work-life-balance-factors"];
    $supportFrequency = $_POST["eff"];
    $personalInterests = $_POST["personal-interests"];
    $policiesRating = $_POST["policies"];
    $strategiesUsed = $_POST["strategies-used"];
    $majorChanges = $_POST["major-changes"];
    $collabRating = $_POST["collab"];
    $teamEnvironmentRating = $_POST["team-environment"];
    $skillsTraining = $_POST["skills-training"];
    $experienceRating = $_POST["rate-experience"];
    $improvementSuggestions = $_POST["improvement-suggestions"];
    $meetingOption = $_POST["meetingOption"];
    if (isset($_POST['submitForm']));
    // You can perform further validation or processing here

    // For demonstration purposes, let's just echo the employee ID
    echo "Employee ID: " . $employeeId;
    echo "Rating: $rating <br>";
    echo "Work-Life Balance: $workLifeBalance <br>";
    echo "Relation with Manager: $relationWithManager <br>";
    echo "Accomplishments: $accomplishments <br>";
    echo "Goals Met or Exceeded: $goalsMetOrExceeded <br>";
    echo "Receive Enough Feedback: $receiveFeedback <br>";
    echo "Work Satisfaction: $workSatisfaction <br>";
    echo "Work-Life Balance Factors: $workLifeBalanceFactors <br>";
    echo "Support Frequency: $supportFrequency <br>";
    echo "Personal Interests Rating: $personalInterests <br>";
    echo "Policies Rating: $policiesRating <br>";
    echo "Strategies Used: $strategiesUsed <br>";
    echo "Major Changes: $majorChanges <br>";
    echo "Team Collaboration Rating: $collabRating <br>";
    echo "Team Environment Rating: $teamEnvironmentRating <br>";
    echo "Skills Training Needs: $skillsTraining <br>";
    echo "Experience Rating: $experienceRating <br>";
    echo "Improvement Suggestions: $improvementSuggestions <br>";
    echo "Selected Meeting Option: $meetingOption <br>";
    echo "Form has been submitted: $isset <br>";
    echo '<div id="thankYouMessage" class="thank-you-message">
            Thank you for submitting the form!
          </div>';
} else {
    // Redirect or handle the situation where the form is not submitted via POST
    echo "Form not submitted";
}
?>
