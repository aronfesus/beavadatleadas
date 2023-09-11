import os
import tempfile
import subprocess
import unittest
import sys
from importlib import import_module
from werkzeug.utils import secure_filename
from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key'  # Change this to a secret key for your app

# Define a folder to store uploaded Python files
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Function to import and test the uploaded module
def do_module_test(file_path):
    try:
        # Remove the file extension to get the module name
        module_name = os.path.splitext(os.path.basename(file_path))[0]

        module_directory = 'uploads'  # Replace with the actual path
        sys.path.insert(0, module_directory)

        # Import the uploaded module dynamically
        uploaded_module = import_module(module_name)

        contains_odd_input_lists= [[1,2,3,4,5,6,7,8,9],[2,4,6,8],[1]]
        contains_odd_expected_lists = [True,False,True]

        # You can now use functions or variables from the uploaded module
        result = contains_odd_check(uploaded_module,contains_odd_input_lists,contains_odd_expected_lists)  # Replace with actual usage
        
        return f'Uploaded module result: {result}'
    except Exception as e:
        return f'Error importing or testing the uploaded module: {str(e)}'

# Route for uploading Python files
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        # Check if the file is empty
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if not file.filename.endswith('.py'):
            flash('Only .py files are allowed')
            return redirect(request.url)
        
        if file:
            try:
                # Create a temporary directory to store the uploaded file
                file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
                file.save(file_path)

                # Run tests on the uploaded Python file
                test_result = do_module_test(file_path)
                
                flash(test_result)

            except Exception as e:
                flash(f'Error: {str(e)}')

            return redirect(request.url)

    return render_template('upload.html')

def contains_odd_check(module,input_lists,expected_lists):
    accept = []
    for inp,exp in zip(input_lists,expected_lists):
        try:
            out = module.contains_odd(inp)
        except:
            return "Error"
        if out == exp:
            accept.append(True)
        else:
            accept.append(False)
        
    return '0' if False in accept else '1'

if __name__ == '__main__':
    app.run(debug=True)
