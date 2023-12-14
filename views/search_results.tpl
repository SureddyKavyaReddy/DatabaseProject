<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Results</title>
</head>
<body>
    <h1>Search Results</h1>
    <p>Search Query: {{ query }}</p>

    % if posts:
        <h2>Search Results</h2>
        <p>Posts found:</p>
        <ul>
            % for post in posts:
                <li>
                    <a href="/user/{{ post['user_id'] }}/post/{{ post['id'] }}">{{ post['title'] }}</a> |
                    <!-- other post details or actions -->
                </li>
            % end
        </ul>
    % else:
        <p>No posts found for the query: {{ query }}</p>
    % end
</body>
</html>
