async function fetchEvents() {
    const response = await fetch('/events');
    const events = await response.json();
    const feed = document.getElementById('feed');
    feed.innerHTML = '';

    events.forEach(event => {
        const li = document.createElement('li');
        const date = new Date(event.timestamp).toUTCString();

        if (event.event_type === 'push') {
            li.textContent = `${event.author} pushed to "${event.to_branch}" on ${date}`;
        } else if (event.event_type === 'pull_request') {
            li.textContent = `${event.author} submitted a pull request from "${event.from_branch}" to "${event.to_branch}" on ${date}`;
        } else if (event.event_type === 'merge') {
            li.textContent = `${event.author} merged branch "${event.from_branch}" to "${event.to_branch}" on ${date}`;
        }

        feed.appendChild(li);
    });
}

fetchEvents();
setInterval(fetchEvents, 15000);
