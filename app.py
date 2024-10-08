from flask import Flask, render_template, request

app = Flask(__name__)

# Define some basic positive and negative words for the sentiment analysis
positive_words = ['happy', 'great', 'awesome', 'fantastic', 'good']
negative_words = ['sad', 'bad', 'terrible', 'horrible', 'awful']

@app.route('/', methods=['GET', 'POST'])
def index():
    background_color = "white"
    
    if request.method == 'POST':
        text = request.form['inputText'].lower()
        sentiment_score = 0

        # Check for positive words
        for word in positive_words:
            if word in text:
                sentiment_score += 1

        # Check for negative words
        for word in negative_words:
            if word in text:
                sentiment_score -= 1

        # Change background color based on sentiment score
        if sentiment_score > 0:
            background_color = "#d4edda"  # Green for positive
        elif sentiment_score < 0:
            background_color = "#f8d7da"  # Red for negative
        else:
            background_color = "#fff3cd"  # Yellow for neutral

    return render_template('index.html', background_color=background_color)

if __name__ == '__main__':
    app.run(debug=True)
