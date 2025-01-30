document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.vote-btn').forEach(button => {
        button.addEventListener('click', function () {
            const postId = this.getAttribute('data-post-id');
            const voteType = this.getAttribute('data-vote-type');
            console.log('votes.js is loaded');

            fetch(`/post/${postId}/vote/${voteType}/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken'), // Include CSRF token
                },
                body: JSON.stringify({}),
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    document.querySelector(`#upvote-count-${postId}`).innerText = data.upvotes;
                    document.querySelector(`#downvote-count-${postId}`).innerText = data.downvotes;
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });

    // Helper function to get CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
