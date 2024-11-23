from flask import Flask, request

app = Flask(__name__)

@app.route('/loot', methods=['POST'])
def upload_file():
    # Check if the file is part of the form data
    if 'file' not in request.files:
        return 'No file part', 400
    
    # Retrieve the file from the request
    file = request.files['file']
    
    # Print file details for debugging
    print(f"Received file: {file.filename}")
    
    # Save the uploaded file as-is to a temporary path
    file_path = f'./{file.filename}'  # Save to the current directory temporarily
    file.save(file_path)
    
    # Open the file and read its content in binary mode
    with open(file_path, 'rb') as f:
        content = f.read()  # Read the binary content
    
    # Decode the content from UTF-16 to UTF-8 (removes BOM)
    decoded_content = content.decode('utf-16')  # Decode from UTF-16
    
    # Save the content as UTF-8
    utf8_file_path = f'./{file.filename}_utf8.txt'
    with open(utf8_file_path, 'w', encoding='utf-8') as utf8_file:
        utf8_file.write(decoded_content)  # Save as UTF-8
    
    # Log the first 100 characters of the decoded content for debugging
    print(f"First 100 characters of the decoded content: {decoded_content[:100]}")
    
    return f'File uploaded successfully! UTF-8 version saved as {utf8_file_path}', 200

if __name__ == '__main__':
    app.run(port=9001)
