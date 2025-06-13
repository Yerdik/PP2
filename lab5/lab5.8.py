def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])
snake = "my_variable_name"
camel = snake_to_camel(snake)
print("CamelCase:", camel)
