from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh-so-secret'

debug = DebugToolbarExtension(app)


@app.route('/')
def home_page():
    """Show home page"""
    questions = story.prompts
    return render_template('home.html', questions=questions)


@app.route('/story')
def story_page():
    """Show story page"""
    your_story = story.generate(request.args)
    return render_template('story.html', your_story=your_story)
