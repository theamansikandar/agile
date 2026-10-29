from flask import Flask, request

app = Flask(__name__)

def get_grade(avg):
    return "Push 1"

@app.route('/calculate')
def calculate():
    marks = [float(x) for x in request.args.getlist('marks')]
    total = sum(marks)
    avg = total / len(marks)
    
    return f"Total: {total}, Average: {avg}, Grade: {get_grade(avg)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
