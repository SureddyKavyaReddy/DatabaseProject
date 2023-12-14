<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Post Detail</title>
</head>
<body>
    <h1>Post Detail</h1>
    <p>Title: {{ post['title'] }}</p>
    <p>Content: {{ post['content'] }}</p>
    <!-- Add more details as needed -->
    <p>
        <a href="/user/{{ post['user_id'] }}">Back to User</a> |
        <a href="/post/{{ post['id'] }}/edit">Edit Post</a> |
        <a href="/post/{{ post['id'] }}/delete">Delete Post</a>
    </p>
</body>
</html>
