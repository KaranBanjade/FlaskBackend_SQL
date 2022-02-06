from email.policy import strict
from flask import Flask, request, jsonify
# Flask for framework

# Request for parsing requests
# jsonify to parse json objects
import os

# Init app
app = Flask(__name__)

import Bugs.bugsRoute

# Run Server
if __name__ == '__main__':
    app.run(debug=True, port=3005)

    #  return res.json({
    #             data: null,
    #             errors: {
    #                 message: `Report Email not sent`
    #             }
