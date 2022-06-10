
"""
          AUTHOR : GAUTAM CHANDRA SAHA
          DATE & TIME: Fri, June 10,2022 AT 22:32 
          DESCRIPTION:

"""


from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
import gpfetcher

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


port = 5050


def main():
    @app.route('/')
    def home():
        return jsonify({"home": "hone for gpfetcher"})

    @app.route('/gpfetcher/scraper/<string:username>', methods=['GET'])
    def get(username):
        
        response = gpfetcher.scrape(username)


        return jsonify(
            {username: response}
        )

    app.run(port=port)


if __name__ == "__main__":
    main()