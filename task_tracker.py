from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data structures to store categories and tasks
categories = []
tasks = {}

# Route to render the index page
@app.route('/')
def index():
    return render_template('index.html', categories=categories, tasks=tasks)

# Route to handle category creation
@app.route('/create_category', methods=['POST'])
def create_category():
    global categories
    category_name = request.form['categoryName']
    if category_name not in categories:
        categories.append(category_name)
        tasks[category_name] = []  # Initialize tasks list for the new category
    return redirect(url_for('index'))

# Route to handle category update
@app.route('/update_category', methods=['POST'])
def update_category():
    global categories, tasks
    old_category_name = request.form['oldCategoryName']
    new_category_name = request.form['newCategoryName']
    if old_category_name in categories:
        categories[categories.index(old_category_name)] = new_category_name
        tasks[new_category_name] = tasks.pop(old_category_name, [])
    return redirect(url_for('index'))

# Route to handle category deletion
@app.route('/delete_category', methods=['POST'])
def delete_category():
    global categories, tasks
    delete_category_name = request.form['deleteCategoryName']
    if delete_category_name in categories:
        categories.remove(delete_category_name)
        tasks.pop(delete_category_name, None)
    return redirect(url_for('index'))

# Route to handle task creation
@app.route('/create_task', methods=['POST'])
def create_task():
    global tasks
    task_title = request.form['taskTitle']
    task_description = request.form['taskDescription']
    task_priority = request.form['taskPriority']
    task_reminder = request.form['taskReminder']
    selected_category = request.form['taskPriorityCategory']

    if selected_category in tasks:
        tasks[selected_category].append({
            'title': task_title,
            'description': task_description,
            'priority': task_priority,
            'reminder': task_reminder
        })
    else:
        tasks[selected_category] = [{
            'title': task_title,
            'description': task_description,
            'priority': task_priority,
            'reminder': task_reminder
        }]

    return redirect(url_for('index'))

# Route to handle task update
@app.route('/update_task', methods=['POST'])
def update_task():
    # Handle task update
    return redirect(url_for('index'))

# Route to handle task deletion
@app.route('/delete_task', methods=['POST'])
def delete_task():
    # Handle task deletion
    return redirect(url_for('index'))

# Route to handle setting task priority
@app.route('/set_task_priority', methods=['POST'])
def set_task_priority():
    # Handle setting task priority
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
