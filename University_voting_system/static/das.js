document.addEventListener('DOMContentLoaded', function() {
    const voteButtons = document.querySelectorAll('.vote-button');
    const userFaculty = 'science'; // Replace with actual user's faculty
    const userHall = 'hall1'; // Replace with actual user's hall
  
    let votedCategories = {};
  
    voteButtons.forEach(button => {
      button.addEventListener('click', function() {
        const category = button.getAttribute('data-category');
        const candidate = button.getAttribute('data-candidate');
  
        // Check if the user is allowed to vote in this category
        if (category.startsWith('hall') && userHall !== category) {
          alert('You are not eligible to vote in this hall.');
          return;
        } else if (!category.startsWith('hall') && userFaculty !== category) {
          alert('You are not eligible to vote in this faculty.');
          return;
        }
  
        // Check if the user has already voted in this category
        if (votedCategories[category]) {
          alert('You have already voted in this category.');
          return;
        }
  
        // Record the vote
        votedCategories[category] = candidate;
        alert(`You have voted for ${candidate} in the ${category} category.`);
  
        // Disable all vote buttons in this category
        document.querySelectorAll(`.vote-button[data-category="${category}"]`).forEach(btn => {
          btn.disabled = true;
          btn.style.backgroundColor = '#ccc';
          btn.style.cursor = 'not-allowed';
        });
      });
    });
  });
  