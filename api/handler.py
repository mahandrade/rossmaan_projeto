from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()

import pandas as pd
import pickle

from Flask            import Flask, request, Response
from rossmann.Rossmann import Rossmann

#loading model
model = pickle.load( open ('/home/mari/projetoss/model/model_rossmann.pkl', 'rb'))
#rossmann = pickle.load( open ('/home/mari/projetoss/api/Rossmann.pkl', 'rb'))

# initialise API
app = flask(_name_)

@app.route( '/rossmann/predict', methods=['POST'])
def rossman_predict():
    test_json = request.get_json()
    
    if test_json: # there is data
        if isintace(test_json, dict ): #unique example
            test_raw = pd.DataFrame(test_json, index= [0] )
        else: #multiple example
            test_raw = pd.DataFrame( test_json, columns= test_json[0].keys() )
        #Instantiate Rossmann class
        pipeline = Rossmann()
                                    
        #data clean
        df1 = pipeline.data_cleaning( test_raw
        )
        #
        df2 = pipeline.data_cleaning( df1 )                            
        #
        df3 = pipeline.data_cleaning( df2 )
        #
        df_response = df1 = pipeline.get_prediction( model, test_raw, df3 )
       
        return df_response
                                    
    else:
        return Response('{}', status=200, mimetype='application/json')
                                    
if _name_==__main__:
    app.run('0.0.0.0')
