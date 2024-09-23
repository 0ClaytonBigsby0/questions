document.addEventListener('DOMContentLoaded', () => {
  fetchQuestions();
});

function fetchQuestions() {
  fetch('/showme/api/questions/')
    .then(response => response.json())
    .then(data => {
      const container = document.getElementById('questions-container');
      container.innerHTML = ''; // Clear existing content
      data.forEach(question => {
        const questionElement = document.createElement('div');
        questionElement.classList.add('question-item');
        questionElement.innerHTML = `
          <p><strong>Q:</strong> ${question.question}</p>
          <button onclick="toggleAnswer(this)">Show Answer</button>
          <p class="answer" style="display: none;"><strong>A:</strong> ${question.answer}</p>
        `;
        container.appendChild(questionElement);
      });
    })
    .catch(error => {
      console.error('Error fetching questions:', error);
      document.getElementById('questions-container').innerHTML = '<p>Failed to load questions</p>';
    });
}

function toggleAnswer(button) {
  const answerParagraph = button.nextElementSibling;
  answerParagraph.style.display = 'block';
  button.style.display = 'none'; // Hide the button
}