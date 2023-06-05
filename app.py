from flask import Flask, render_template, request
import config
import aiapi
import openai

# chat-bot model
COMPLETIONS_MODEL = "text-davinci-003"

# your api key goes here
openai.api_key = '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'

def page_not_found(e):
  return render_template('404.html'), 404


app = Flask(__name__)

app.register_error_handler(404, page_not_found)


@app.route('/', methods = ['POST', 'GET'])
def index():
    
    if request.method == 'POST':
      prompt = request.form['prompt']
      answer = aiapi.get_response_of_text(prompt)
      return answer

    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)
