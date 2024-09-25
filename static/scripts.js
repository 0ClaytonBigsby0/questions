document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('start-quiz-btn').addEventListener('click', startQuiz);
});

let currentQuestionIndex = 0;
let score = 0;
let questions = [];

function startQuiz() {
  document.getElementById('start-container').style.display = 'none';
  document.getElementById('questions-container').style.display = 'block';
  fetchQuestions();
}

function fetchQuestions() {
  fetch('/showme/api/questions/')
    .then(response => response.json())
    .then(data => {
      questions = data;
      currentQuestionIndex = 0; // Start with the first question
      score = 0; // Reset score
      displayQuestion(questions[currentQuestionIndex]);
    })
    .catch(error => {
      console.error('Error fetching questions:', error);
      document.getElementById('questions-container').innerHTML = '<p>Failed to load questions</p>';
    });
}

function displayQuestion(question) {
  const container = document.getElementById('questions-container');
  container.innerHTML = ''; // Clear the previous question

  const questionElement = document.createElement('div');
  questionElement.classList.add('question-item');
  questionElement.innerHTML = `
    <p><strong>Q:</strong> ${question.question}</p>
    <form>
      <input type="radio" name="answer" value="${question.option1}"> ${question.option1}<br>
      <input type="radio" name="answer" value="${question.option2}"> ${question.option2}<br>
      <input type="radio" name="answer" value="${question.option3}"> ${question.option3}<br>
    </form>
    <button onclick="checkAnswer()">Submit Answer</button>
  `;
  container.appendChild(questionElement);
}

function checkAnswer() {
  const selectedAnswer = document.querySelector('input[name="answer"]:checked');
  if (!selectedAnswer) {
    alert('Please select an answer!');
    return;
  }

  const correctAnswer = questions[currentQuestionIndex].correct_answer;
  const userAnswer = selectedAnswer.value;

  if (userAnswer === correctAnswer) {
    score++;
  }

  currentQuestionIndex++;

  if (currentQuestionIndex < questions.length) {
    displayQuestion(questions[currentQuestionIndex]);
  } else {
    displayResults();
  }
}

function displayResults() {
  const container = document.getElementById('questions-container');
  container.innerHTML = `
    <div class="quiz-results">
      <h3>Quiz Completed!</h3>
      <p>Your score is ${score} out of ${questions.length}.</p>
    </div>
  `;
}
