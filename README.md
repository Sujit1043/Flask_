# Webhook Receiver for GitHub Events

This project is part of a developer assessment assignment to demonstrate the use of **GitHub webhooks**, **Flask**, and **MongoDB** to build a simple real-time event tracker.

---

## Assignment Objective

- Create a webhook listener that receives GitHub events (`push`, `pull_request`, and optionally `merge`) from a separate repository.
- Store the events in MongoDB with a defined schema.
- Display the latest events on a simple, auto-refreshing frontend.
- Keep frontend data updated every 15 seconds.
- Show only the **essential data** in a **clean format**.

## Repositories

This project is split into two repositories:

| Repo            | Description |
|-----------------|-------------|
| [`action-repo`](https://github.com/Sujit1043/action-repo) | Triggers GitHub events (push, PR, merge) |
| [`webhook-repo`](https://github.com/Sujit1043/webhook-repo)     | Flask app receiving and displaying events |

---

## Tech Stack
- Backend:Python, Flask
- Database: MongoDB (local or Atlas)
- Frontend: HTML + Flask templating
- Deployment/Test Tool:** [ngrok](https://ngrok.com/) for exposing localhost to GitHub
- GitHub Integration: Webhooks


##  MongoDB Schema

```json
{
  "event_type": "push" | "pull_request" | "merge",
  "author": "Travis",
  "from_branch": "feature-x",
  "to_branch": "main",
  "timestamp": ISODate("2021-04-01T09:30:00Z")
}
