from flask import Flask,render_template,request,url_for
import requests
app=Flask(__name__)
@app.route('/',methods=['POST','GET'])
def hello():
    if request.method=='POST':
        dailyrate=request.form['a']
        dfm=request.form['b']
        ef=request.form['r1']
        es=request.form['d']
        hr=request.form['e']
        mr=request.form['f']
        ttlr=request.form['g']
        ycm=request.form['h']
        print(ef)
        try:
            dailyrate=int(dailyrate)
            dfm=int(dfm)
            ef=int(ef)
            es=int(es)
            hr=int(hr)
            mr=int(mr)
            ttlr=int(ttlr)
            ycm=int(ycm)
        except:
            return render_template('data.html',err_msg='Enter Valid Data')
        url = "https://jamvd4z3fi.execute-api.us-east-1.amazonaws.com/employe/"
        payload = " {\"data\":\"" + str(dailyrate) + ',' + str(dfm) + ',' + str(ef) + ',' + str(es) + ',' + str(hr) + ',' + str(mr) + ',' + str(ttlr) + ',' + str(ycm) + "\"" + "}"

        headers = {
            'X-Amz-Content-Sha256': 'beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3',
            'X-Amz-Date': '20201009T132000Z',
            'Authorization': '',
            'Content-Type': 'text/plain'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        response=response.text.encode('utf8')
        response=str(response)
        print(response)
        result=response[2:-1]
        print(result)
        return render_template('data.html',result=str(result))
    else:
        return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True)
