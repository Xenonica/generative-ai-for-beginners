# Prompts
# You are a coding assistant which specializes in Python and Flask framework
# Help me improve the following code i have provided. Before you give me an answer, think step by step and list out the improvement you had made in bullet form
# Give improvements to the code. Limit up to 5 improvements if possible
# Output
#Perfect — here are 5 focused improvements to your Flask code, keeping it concise and relevant:

# ✅ 5 Improvements
# Use render_template_string for auto HTML escaping:
# Prevents potential injection when rendering user input.
# Safer than returning raw f-string.

# Add type hints to function signatures:
# Improves code readability and helps with editor/tooling support.

# Set host='0.0.0.0' in app.run():
# Makes the app accessible on your local network — useful for testing across devices.

# Set debug=True only during development:
# Helps with live reloading and debugging, but should not be used in production.

# Convert name to a safe string explicitly:
# Prevents accidental type injection or NoneType issues.


from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    name = request.args.get('name', 'World')
    safe_name = str(name)
    return render_template_string('<h1>Hello, {{ name }}!</h1>', name=safe_name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# Let me know if you want to go further — like using render_template with actual HTML files or adding more routes!