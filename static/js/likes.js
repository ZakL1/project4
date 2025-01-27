document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.vote-btn').forEach(button => {
        button.addEventListener('click', function () {
            const postId = this.getAttribute('data-post-id');
            const voteType = this.getAttribute('data-vote-type');
            console.log('votes.js is loaded');
            fetch(`/post/${postId}/vote/${voteType}/`, {
                method: 'GET', 
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
});